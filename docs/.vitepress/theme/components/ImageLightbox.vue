<script setup lang="ts">
import { computed, nextTick, onMounted, onUnmounted, ref } from "vue";

import {
  clampTransform,
  distance,
  midpoint,
  MIN_SCALE,
  zoomBetweenPoints,
  type Point,
  type Size,
  type ZoomTransform,
} from "./imageZoom";

const imageSelector = ".VPDoc .vp-doc img";
const interactiveContainerSelector = 'a, button, [data-no-zoom]';
const buttonRoleSelector = '[role="button"]';

const isOpen = ref(false);
const imageSrc = ref("");
const imageAlt = ref("");
const closeButton = ref<HTMLButtonElement | null>(null);
const stage = ref<HTMLElement | null>(null);
const preview = ref<HTMLImageElement | null>(null);
const zoomTransform = ref<ZoomTransform>({ scale: 1, x: 0, y: 0 });
const isDragging = ref(false);

let triggerImage: HTMLImageElement | null = null;
let contentObserver: MutationObserver | undefined;

const activePointers = new Map<number, Point>();

interface GestureGeometry {
  imageSize: Size;
  stageCenter: Point;
  stageSize: Size;
}

interface DragSnapshot {
  geometry: GestureGeometry;
  pointerId: number;
  startPoint: Point;
  startTransform: ZoomTransform;
}

interface PinchSnapshot {
  geometry: GestureGeometry;
  pointerIds: [number, number];
  startDistance: number;
  startMidpoint: Point;
  startTransform: ZoomTransform;
}

let dragSnapshot: DragSnapshot | undefined;
let pinchSnapshot: PinchSnapshot | undefined;

const decoratedImages = new Map<
  HTMLImageElement,
  {
    tabindex: string | null;
    role: string | null;
    ariaLabel: string | null;
  }
>();

const dialogLabel = computed(() =>
  imageAlt.value ? `图片预览：${imageAlt.value}` : "图片预览",
);
const zoomPercentage = computed(() =>
  Math.round(zoomTransform.value.scale * 100),
);
const isZoomed = computed(() => zoomTransform.value.scale > MIN_SCALE);
const previewStyle = computed(() => ({
  transform: `translate3d(${zoomTransform.value.x}px, ${zoomTransform.value.y}px, 0px) scale(${zoomTransform.value.scale})`,
}));

const isZoomableImage = (
  target: EventTarget | null,
): target is HTMLImageElement => {
  if (!(target instanceof HTMLImageElement) || !target.matches(imageSelector)) {
    return false;
  }

  if (target.closest(interactiveContainerSelector)) return false;

  const buttonRole = target.closest(buttonRoleSelector);
  return !buttonRole || (buttonRole === target && "wbZoomable" in target.dataset);
};

const decorateImage = (image: HTMLImageElement) => {
  if (!isZoomableImage(image) || decoratedImages.has(image)) return;

  decoratedImages.set(image, {
    tabindex: image.getAttribute("tabindex"),
    role: image.getAttribute("role"),
    ariaLabel: image.getAttribute("aria-label"),
  });

  image.dataset.wbZoomable = "";
  image.setAttribute("tabindex", "0");
  image.setAttribute("role", "button");
  image.setAttribute(
    "aria-label",
    image.alt ? `放大查看：${image.alt}` : "放大查看图片",
  );
};

const decorateImages = () => {
  for (const image of document.querySelectorAll<HTMLImageElement>(imageSelector)) {
    decorateImage(image);
  }

  for (const image of decoratedImages.keys()) {
    if (!image.isConnected) decoratedImages.delete(image);
  }
};

const focusCloseButton = async () => {
  await nextTick();
  closeButton.value?.focus({ preventScroll: true });
};

const resetZoom = () => {
  zoomTransform.value = { scale: 1, x: 0, y: 0 };
  activePointers.clear();
  dragSnapshot = undefined;
  pinchSnapshot = undefined;
  isDragging.value = false;
};

const readGestureGeometry = (): GestureGeometry | null => {
  if (!stage.value || !preview.value) return null;

  const stageRect = stage.value.getBoundingClientRect();
  const previewRect = preview.value.getBoundingClientRect();
  const scale = zoomTransform.value.scale;

  if (
    stageRect.width <= 0 ||
    stageRect.height <= 0 ||
    previewRect.width <= 0 ||
    previewRect.height <= 0
  ) {
    return null;
  }

  return {
    imageSize: {
      width: previewRect.width / scale,
      height: previewRect.height / scale,
    },
    stageCenter: {
      x: stageRect.left + stageRect.width / 2,
      y: stageRect.top + stageRect.height / 2,
    },
    stageSize: {
      width: stageRect.width,
      height: stageRect.height,
    },
  };
};

const relativeToStageCenter = (point: Point, center: Point): Point => ({
  x: point.x - center.x,
  y: point.y - center.y,
});

const pointFromPointer = (event: PointerEvent): Point => ({
  x: event.clientX,
  y: event.clientY,
});

const startDragSnapshot = (pointerId: number) => {
  const startPoint = activePointers.get(pointerId);
  const geometry = readGestureGeometry();

  if (!startPoint || !geometry) return;

  dragSnapshot = {
    geometry,
    pointerId,
    startPoint,
    startTransform: { ...zoomTransform.value },
  };
  pinchSnapshot = undefined;
  isDragging.value = isZoomed.value;
};

const startPinchSnapshot = () => {
  const entries = Array.from(activePointers.entries()).slice(0, 2);
  const geometry = readGestureGeometry();

  if (entries.length !== 2 || !geometry) return;

  const [[firstId, first], [secondId, second]] = entries;
  const startDistance = distance(first, second);

  if (startDistance === 0) return;

  pinchSnapshot = {
    geometry,
    pointerIds: [firstId, secondId],
    startDistance,
    startMidpoint: relativeToStageCenter(
      midpoint(first, second),
      geometry.stageCenter,
    ),
    startTransform: { ...zoomTransform.value },
  };
  dragSnapshot = undefined;
  isDragging.value = true;
};

const handleWheel = (event: WheelEvent) => {
  const geometry = readGestureGeometry();

  if (!geometry) return;

  const eventPoint = {
    x: Number.isFinite(event.clientX) ? event.clientX : geometry.stageCenter.x,
    y: Number.isFinite(event.clientY) ? event.clientY : geometry.stageCenter.y,
  };
  const anchor = relativeToStageCenter(
    eventPoint,
    geometry.stageCenter,
  );
  const requestedScale =
    zoomTransform.value.scale * Math.exp(-event.deltaY * 0.002);

  zoomTransform.value = zoomBetweenPoints(
    zoomTransform.value,
    requestedScale,
    anchor,
    anchor,
    geometry.imageSize,
    geometry.stageSize,
  );
};

const handlePointerDown = (event: PointerEvent) => {
  if (event.pointerType === "mouse" && event.button !== 0) return;

  event.preventDefault();
  activePointers.set(event.pointerId, pointFromPointer(event));
  (event.currentTarget as HTMLElement).setPointerCapture?.(event.pointerId);

  if (activePointers.size === 1) startDragSnapshot(event.pointerId);
  else if (activePointers.size === 2) startPinchSnapshot();
};

const handlePointerMove = (event: PointerEvent) => {
  if (!activePointers.has(event.pointerId)) return;

  activePointers.set(event.pointerId, pointFromPointer(event));

  if (activePointers.size >= 2 && pinchSnapshot) {
    const [firstId, secondId] = pinchSnapshot.pointerIds;
    const first = activePointers.get(firstId);
    const second = activePointers.get(secondId);

    if (!first || !second) return;

    const currentDistance = distance(first, second);
    const currentMidpoint = relativeToStageCenter(
      midpoint(first, second),
      pinchSnapshot.geometry.stageCenter,
    );
    const requestedScale =
      pinchSnapshot.startTransform.scale *
      (currentDistance / pinchSnapshot.startDistance);

    zoomTransform.value = zoomBetweenPoints(
      pinchSnapshot.startTransform,
      requestedScale,
      pinchSnapshot.startMidpoint,
      currentMidpoint,
      pinchSnapshot.geometry.imageSize,
      pinchSnapshot.geometry.stageSize,
    );
    isDragging.value = true;
    return;
  }

  if (!dragSnapshot || dragSnapshot.pointerId !== event.pointerId) return;
  if (dragSnapshot.startTransform.scale === MIN_SCALE) return;

  const currentPoint = activePointers.get(event.pointerId);

  if (!currentPoint) return;

  zoomTransform.value = clampTransform(
    {
      scale: dragSnapshot.startTransform.scale,
      x:
        dragSnapshot.startTransform.x +
        currentPoint.x -
        dragSnapshot.startPoint.x,
      y:
        dragSnapshot.startTransform.y +
        currentPoint.y -
        dragSnapshot.startPoint.y,
    },
    dragSnapshot.geometry.imageSize,
    dragSnapshot.geometry.stageSize,
  );
  isDragging.value = true;
};

const handlePointerEnd = (event: PointerEvent) => {
  const target = event.currentTarget as HTMLElement;

  if (target.hasPointerCapture?.(event.pointerId)) {
    target.releasePointerCapture?.(event.pointerId);
  }

  activePointers.delete(event.pointerId);
  dragSnapshot = undefined;
  pinchSnapshot = undefined;

  if (activePointers.size === 1) {
    const [remainingId] = activePointers.keys();
    startDragSnapshot(remainingId);
  } else {
    isDragging.value = false;
  }
};

const openImage = (image: HTMLImageElement) => {
  resetZoom();
  triggerImage = image;
  imageSrc.value = image.currentSrc || image.src;
  imageAlt.value = image.alt;
  isOpen.value = true;
  document.body.classList.add("wb-lightbox-open");
  void focusCloseButton();
};

const closeImage = async () => {
  if (!isOpen.value) return;

  const imageToRefocus = triggerImage;
  resetZoom();
  isOpen.value = false;
  imageSrc.value = "";
  imageAlt.value = "";
  triggerImage = null;
  document.body.classList.remove("wb-lightbox-open");

  await nextTick();
  imageToRefocus?.focus({ preventScroll: true });
};

const handleDocumentClick = (event: MouseEvent) => {
  if (!isOpen.value && isZoomableImage(event.target)) {
    openImage(event.target);
  }
};

const handleDocumentKeydown = (event: KeyboardEvent) => {
  if (isOpen.value) {
    if (event.key === "Escape") {
      event.preventDefault();
      void closeImage();
    } else if (event.key === "Tab") {
      event.preventDefault();
      void focusCloseButton();
    }

    return;
  }

  if (
    (event.key === "Enter" || event.key === " ") &&
    isZoomableImage(event.target)
  ) {
    event.preventDefault();
    openImage(event.target);
  }
};

const handleBackdropClick = (event: MouseEvent) => {
  if (event.target === event.currentTarget) void closeImage();
};

const restoreDecoratedImages = () => {
  for (const [image, original] of decoratedImages) {
    delete image.dataset.wbZoomable;

    for (const [attribute, value] of [
      ["tabindex", original.tabindex],
      ["role", original.role],
      ["aria-label", original.ariaLabel],
    ] as const) {
      if (value === null) image.removeAttribute(attribute);
      else image.setAttribute(attribute, value);
    }
  }

  decoratedImages.clear();
};

onMounted(() => {
  decorateImages();
  document.addEventListener("click", handleDocumentClick);
  document.addEventListener("keydown", handleDocumentKeydown);

  contentObserver = new MutationObserver(decorateImages);
  contentObserver.observe(document.body, { childList: true, subtree: true });
});

onUnmounted(() => {
  contentObserver?.disconnect();
  document.removeEventListener("click", handleDocumentClick);
  document.removeEventListener("keydown", handleDocumentKeydown);
  document.body.classList.remove("wb-lightbox-open");
  resetZoom();
  restoreDecoratedImages();
});
</script>

<template>
  <Teleport to="body">
    <Transition name="wb-lightbox">
      <div
        v-if="isOpen"
        class="wb-image-lightbox"
        role="dialog"
        aria-modal="true"
        :aria-label="dialogLabel"
        @click="handleBackdropClick"
      >
        <button
          ref="closeButton"
          class="wb-image-lightbox__close"
          type="button"
          aria-label="关闭图片预览"
          @click="closeImage"
        >
          <span aria-hidden="true">×</span>
        </button>

        <div
          ref="stage"
          class="wb-image-lightbox__stage"
          :class="{
            'is-zoomed': isZoomed,
            'is-dragging': isDragging,
          }"
          @click="handleBackdropClick"
          @wheel.prevent="handleWheel"
          @pointerdown="handlePointerDown"
          @pointermove="handlePointerMove"
          @pointerup="handlePointerEnd"
          @pointercancel="handlePointerEnd"
        >
          <img
            ref="preview"
            :src="imageSrc"
            :alt="imageAlt"
            :style="previewStyle"
            draggable="false"
            @click.stop
          >
        </div>

        <p class="wb-image-lightbox__hint" aria-hidden="true">
          <span class="wb-image-lightbox__scale">{{ zoomPercentage }}%</span>
          滚轮 / 双指缩放 · 拖拽查看
          <span class="wb-image-lightbox__key">ESC</span>
          关闭
        </p>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.wb-image-lightbox {
  position: fixed;
  z-index: 200;
  inset: 0;
  display: grid;
  width: 100vw;
  height: 100vh;
  height: 100dvh;
  padding: 48px 3vw;
  place-items: center;
  overflow: hidden;
  background: rgb(9 11 8 / 94%);
  backdrop-filter: blur(10px);
  cursor: zoom-out;
}

.wb-image-lightbox__stage {
  display: grid;
  width: 94vw;
  height: calc(100vh - 104px);
  height: calc(100dvh - 104px);
  place-items: center;
  overflow: visible;
  touch-action: none;
  cursor: default;
}

.wb-image-lightbox__stage img {
  display: block;
  width: auto;
  max-width: 94vw;
  height: auto;
  max-height: calc(100vh - 104px);
  max-height: calc(100dvh - 104px);
  border: 2px solid var(--wb-acid);
  border-radius: 3px;
  object-fit: contain;
  background: #fff;
  box-shadow: 8px 8px 0 rgb(216 242 56 / 22%);
  transform-origin: center;
  transition: transform 80ms ease-out;
  user-select: none;
  will-change: transform;
}

.wb-image-lightbox__stage.is-zoomed {
  cursor: grab;
}

.wb-image-lightbox__stage.is-dragging {
  cursor: grabbing;
}

.wb-image-lightbox__stage.is-dragging img {
  transition: none;
}

.wb-image-lightbox__close {
  position: fixed;
  z-index: 1;
  top: max(18px, env(safe-area-inset-top));
  right: max(18px, env(safe-area-inset-right));
  display: grid;
  width: 52px;
  height: 52px;
  padding: 0;
  place-items: center;
  border: 2px solid var(--wb-acid);
  border-radius: 2px;
  color: #11130e;
  background: var(--wb-acid);
  box-shadow: 4px 4px 0 #fff;
  cursor: pointer;
  transition: transform 140ms ease, box-shadow 140ms ease;
}

.wb-image-lightbox__close span {
  font-size: 38px;
  font-weight: 400;
  line-height: 1;
  transform: translateY(-2px);
}

.wb-image-lightbox__close:hover,
.wb-image-lightbox__close:focus-visible {
  outline: 0;
  box-shadow: 6px 6px 0 #fff;
  transform: translate(-2px, -2px);
}

.wb-image-lightbox__hint {
  position: fixed;
  right: 0;
  bottom: max(14px, env(safe-area-inset-bottom));
  left: 0;
  margin: 0;
  color: rgb(255 255 255 / 76%);
  font-size: 12px;
  font-weight: 650;
  letter-spacing: 0.04em;
  text-align: center;
  pointer-events: none;
}

.wb-image-lightbox__scale,
.wb-image-lightbox__key {
  display: inline-block;
  padding: 2px 6px;
  border: 1px solid rgb(216 242 56 / 62%);
  font-family: var(--wb-pixel);
  font-size: 9px;
  font-weight: 400;
}

.wb-image-lightbox__scale {
  min-width: 46px;
  margin-right: 8px;
  border-color: var(--wb-acid);
  color: #11130e;
  background: var(--wb-acid);
}

.wb-image-lightbox__key {
  margin-right: 4px;
  margin-left: 10px;
  color: var(--wb-acid);
}

.wb-lightbox-enter-active,
.wb-lightbox-leave-active {
  transition: opacity 180ms ease;
}

.wb-lightbox-enter-active .wb-image-lightbox__stage,
.wb-lightbox-leave-active .wb-image-lightbox__stage {
  transition: transform 180ms ease, opacity 180ms ease;
}

.wb-lightbox-enter-from,
.wb-lightbox-leave-to {
  opacity: 0;
}

.wb-lightbox-enter-from .wb-image-lightbox__stage,
.wb-lightbox-leave-to .wb-image-lightbox__stage {
  opacity: 0;
  transform: scale(0.975);
}

@media (max-width: 640px) {
  .wb-image-lightbox {
    padding: 58px 10px 46px;
  }

  .wb-image-lightbox__stage {
    width: calc(100vw - 20px);
    height: calc(100vh - 104px);
    height: calc(100dvh - 104px);
  }

  .wb-image-lightbox__stage img {
    max-width: calc(100vw - 20px);
    max-height: calc(100vh - 104px);
    max-height: calc(100dvh - 104px);
  }

  .wb-image-lightbox__close {
    top: max(10px, env(safe-area-inset-top));
    right: max(10px, env(safe-area-inset-right));
    width: 44px;
    height: 44px;
    box-shadow: 3px 3px 0 #fff;
  }

  .wb-image-lightbox__close span {
    font-size: 32px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .wb-image-lightbox,
  .wb-image-lightbox__stage,
  .wb-image-lightbox__stage img,
  .wb-image-lightbox__close {
    transition: none !important;
  }
}
</style>
