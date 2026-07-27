import { mount, type VueWrapper } from "@vue/test-utils";
import { nextTick } from "vue";
import { afterEach, beforeEach, describe, expect, it } from "vitest";

import ImageLightbox from "./ImageLightbox.vue";

let wrapper: VueWrapper | undefined;

const mountLightbox = async () => {
  const mountTarget = document.createElement("div");
  document.body.append(mountTarget);
  wrapper = mount(ImageLightbox, { attachTo: mountTarget });
  await nextTick();
};

const createDocImage = ({
  alt = "WorkBuddy 操作截图",
  linked = false,
  optedOut = false,
  roleButton = false,
}: {
  alt?: string;
  linked?: boolean;
  optedOut?: boolean;
  roleButton?: boolean;
} = {}) => {
  let doc = document.querySelector<HTMLElement>(".VPDoc .vp-doc");

  if (!doc) {
    const page = document.createElement("main");
    page.className = "VPDoc";
    doc = document.createElement("article");
    doc.className = "vp-doc";
    page.append(doc);
    document.body.append(page);
  }

  const image = document.createElement("img");
  image.src = "/assets/example.png";
  image.alt = alt;

  if (optedOut) image.setAttribute("data-no-zoom", "");
  if (roleButton) image.setAttribute("role", "button");

  if (linked) {
    const link = document.createElement("a");
    link.href = image.src;
    link.append(image);
    doc.append(link);
  } else {
    doc.append(image);
  }

  return image;
};

const openWithClick = async (image: HTMLImageElement) => {
  image.click();
  await nextTick();
};

const createRect = (
  left: number,
  top: number,
  width: number,
  height: number,
): DOMRect =>
  ({
    x: left,
    y: top,
    left,
    top,
    width,
    height,
    right: left + width,
    bottom: top + height,
    toJSON: () => ({}),
  }) as DOMRect;

const readPreviewTransform = (preview: HTMLImageElement) => {
  const match = preview.style.transform.match(
    /translate3d\(([-\d.]+)px, ([-\d.]+)px, 0(?:px)?\) scale\(([-\d.]+)\)/,
  );

  if (!match) return null;

  return {
    x: Number(match[1]),
    y: Number(match[2]),
    scale: Number(match[3]),
  };
};

const stubLightboxGeometry = () => {
  const stage = document.querySelector<HTMLElement>(
    ".wb-image-lightbox__stage",
  );
  const preview = stage?.querySelector<HTMLImageElement>("img");

  if (!stage || !preview) throw new Error("Lightbox geometry is unavailable");

  stage.getBoundingClientRect = () => createRect(0, 0, 1000, 800);
  preview.getBoundingClientRect = () => {
    const scale = readPreviewTransform(preview)?.scale ?? 1;
    return createRect(100, 100, 800 * scale, 600 * scale);
  };

  return { preview, stage };
};

const dispatchPointer = (
  target: HTMLElement,
  type: "pointerdown" | "pointermove" | "pointerup",
  pointerId: number,
  clientX: number,
  clientY: number,
) => {
  target.dispatchEvent(
    new PointerEvent(type, {
      bubbles: true,
      button: 0,
      cancelable: true,
      clientX,
      clientY,
      pointerId,
      pointerType: "touch",
    }),
  );
};

beforeEach(() => {
  document.body.innerHTML = "";
  document.body.className = "";
});

afterEach(() => {
  wrapper?.unmount();
  wrapper = undefined;
  document.body.innerHTML = "";
  document.body.className = "";
});

describe("ImageLightbox", () => {
  it("decorates eligible images and excludes existing interactions", async () => {
    const plainImage = createDocImage();
    const linkedImage = createDocImage({ linked: true });
    const optedOutImage = createDocImage({ optedOut: true });
    const existingButtonImage = createDocImage({ roleButton: true });

    await mountLightbox();

    expect(plainImage.dataset.wbZoomable).toBe("");
    expect(plainImage.getAttribute("tabindex")).toBe("0");
    expect(plainImage.getAttribute("role")).toBe("button");
    expect(plainImage.getAttribute("aria-label")).toContain("WorkBuddy 操作截图");
    expect(linkedImage.dataset.wbZoomable).toBeUndefined();
    expect(optedOutImage.dataset.wbZoomable).toBeUndefined();
    expect(existingButtonImage.dataset.wbZoomable).toBeUndefined();
  });

  it("opens on click and closes with Escape while restoring focus", async () => {
    const image = createDocImage();
    await mountLightbox();

    await openWithClick(image);

    const dialog = document.querySelector<HTMLElement>('[role="dialog"]');
    const preview = dialog?.querySelector<HTMLImageElement>("img");
    const closeButton = dialog?.querySelector<HTMLButtonElement>("button");

    expect(dialog).not.toBeNull();
    expect(preview?.src).toBe(image.src);
    expect(document.body.classList.contains("wb-lightbox-open")).toBe(true);
    expect(document.activeElement).toBe(closeButton);

    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" }));
    await nextTick();

    expect(document.querySelector('[role="dialog"]')).toBeNull();
    expect(document.body.classList.contains("wb-lightbox-open")).toBe(false);
    expect(document.activeElement).toBe(image);
  });

  it.each(["Enter", " "])("opens from the %s key", async (key) => {
    const image = createDocImage({ alt: "键盘打开示例" });
    await mountLightbox();
    image.focus();

    image.dispatchEvent(new KeyboardEvent("keydown", { key, bubbles: true }));
    await nextTick();

    expect(document.querySelector('[role="dialog"]')).not.toBeNull();
  });

  it("closes only when the backdrop itself is clicked", async () => {
    const image = createDocImage();
    await mountLightbox();
    await openWithClick(image);

    const overlay = document.querySelector<HTMLElement>(".wb-image-lightbox");
    const preview = overlay?.querySelector<HTMLImageElement>("img");

    preview?.click();
    await nextTick();
    expect(document.querySelector('[role="dialog"]')).not.toBeNull();

    overlay?.dispatchEvent(new MouseEvent("click", { bubbles: true }));
    await nextTick();
    expect(document.querySelector('[role="dialog"]')).toBeNull();
  });

  it("decorates images added after client-side navigation", async () => {
    await mountLightbox();

    const image = createDocImage({ alt: "路由切换后的截图" });
    await new Promise((resolve) => queueMicrotask(resolve));

    expect(image.dataset.wbZoomable).toBe("");
  });

  it("zooms with the wheel and resets when reopened", async () => {
    const image = createDocImage();
    await mountLightbox();
    await openWithClick(image);

    const { preview, stage } = stubLightboxGeometry();
    const wheelEvent = new WheelEvent("wheel", {
      bubbles: true,
      cancelable: true,
      clientX: 500,
      clientY: 400,
      deltaY: -120,
    });

    stage.dispatchEvent(wheelEvent);
    await nextTick();

    expect(wheelEvent.defaultPrevented).toBe(true);
    expect(readPreviewTransform(preview)?.scale).toBeGreaterThan(1);
    expect(
      document.querySelector(".wb-image-lightbox__scale")?.textContent,
    ).not.toBe("100%");

    document
      .querySelector<HTMLButtonElement>(".wb-image-lightbox__close")
      ?.click();
    await nextTick();
    await openWithClick(image);

    const reopenedPreview = document.querySelector<HTMLImageElement>(
      ".wb-image-lightbox__stage img",
    );
    expect(reopenedPreview?.style.transform).toBe(
      "translate3d(0px, 0px, 0px) scale(1)",
    );
  });

  it("drags a wheel-zoomed image within its bounds", async () => {
    const image = createDocImage();
    await mountLightbox();
    await openWithClick(image);

    const { preview, stage } = stubLightboxGeometry();
    stage.dispatchEvent(
      new WheelEvent("wheel", {
        bubbles: true,
        cancelable: true,
        clientX: 500,
        clientY: 400,
        deltaY: -400,
      }),
    );
    await nextTick();

    dispatchPointer(stage, "pointerdown", 1, 500, 400);
    dispatchPointer(stage, "pointermove", 1, 560, 440);
    dispatchPointer(stage, "pointerup", 1, 560, 440);
    await nextTick();

    const transform = readPreviewTransform(preview);
    expect(transform?.x).toBeCloseTo(60);
    expect(transform?.y).toBeCloseTo(40);
  });

  it("uses two pointers to zoom and follow the pinch midpoint", async () => {
    const image = createDocImage();
    await mountLightbox();
    await openWithClick(image);

    const { preview, stage } = stubLightboxGeometry();
    dispatchPointer(stage, "pointerdown", 1, 400, 400);
    dispatchPointer(stage, "pointerdown", 2, 600, 400);
    dispatchPointer(stage, "pointermove", 2, 700, 420);
    await nextTick();

    const transform = readPreviewTransform(preview);
    expect(transform?.scale).toBeCloseTo(1.5, 1);
    expect(transform?.x).toBeCloseTo(50);
    expect(transform?.y).toBeCloseTo(10);
  });
});
