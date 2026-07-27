export interface Point {
  x: number;
  y: number;
}

export interface Size {
  width: number;
  height: number;
}

export interface ZoomTransform extends Point {
  scale: number;
}

export const MIN_SCALE = 1;
export const MAX_SCALE = 5;

const clamp = (value: number, minimum: number, maximum: number) =>
  Math.min(maximum, Math.max(minimum, value));

const clampPan = (value: number, maximum: number) =>
  maximum === 0 ? 0 : clamp(value, -maximum, maximum);

export const clampScale = (scale: number) =>
  clamp(scale, MIN_SCALE, MAX_SCALE);

export const midpoint = (first: Point, second: Point): Point => ({
  x: (first.x + second.x) / 2,
  y: (first.y + second.y) / 2,
});

export const distance = (first: Point, second: Point) =>
  Math.hypot(second.x - first.x, second.y - first.y);

export const clampTransform = (
  transform: ZoomTransform,
  imageSize: Size,
  stageSize: Size,
): ZoomTransform => {
  const scale = clampScale(transform.scale);

  if (scale === MIN_SCALE) return { scale, x: 0, y: 0 };

  const maximumX = Math.max(
    0,
    (imageSize.width * scale - stageSize.width) / 2,
  );
  const maximumY = Math.max(
    0,
    (imageSize.height * scale - stageSize.height) / 2,
  );

  return {
    scale,
    x: clampPan(transform.x, maximumX),
    y: clampPan(transform.y, maximumY),
  };
};

export const zoomBetweenPoints = (
  current: ZoomTransform,
  requestedScale: number,
  from: Point,
  to: Point,
  imageSize: Size,
  stageSize: Size,
): ZoomTransform => {
  const currentScale = clampScale(current.scale);
  const nextScale = clampScale(requestedScale);
  const ratio = nextScale / currentScale;

  return clampTransform(
    {
      scale: nextScale,
      x: to.x + (current.x - from.x) * ratio,
      y: to.y + (current.y - from.y) * ratio,
    },
    imageSize,
    stageSize,
  );
};
