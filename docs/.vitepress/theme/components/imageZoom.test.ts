import { describe, expect, it } from "vitest";

import {
  clampScale,
  clampTransform,
  distance,
  MAX_SCALE,
  midpoint,
  MIN_SCALE,
  zoomBetweenPoints,
} from "./imageZoom";

describe("image zoom geometry", () => {
  it("clamps zoom to the supported range", () => {
    expect(clampScale(0.5)).toBe(MIN_SCALE);
    expect(clampScale(3)).toBe(3);
    expect(clampScale(7)).toBe(MAX_SCALE);
  });

  it("calculates pointer midpoint and distance", () => {
    expect(midpoint({ x: 0, y: 10 }, { x: 20, y: 30 })).toEqual({
      x: 10,
      y: 20,
    });
    expect(distance({ x: 0, y: 0 }, { x: 3, y: 4 })).toBe(5);
  });

  it("keeps the same content point beneath a stationary zoom anchor", () => {
    expect(
      zoomBetweenPoints(
        { scale: 1, x: 0, y: 0 },
        2,
        { x: 100, y: 50 },
        { x: 100, y: 50 },
        { width: 800, height: 600 },
        { width: 800, height: 600 },
      ),
    ).toEqual({ scale: 2, x: -100, y: -50 });
  });

  it("moves the anchored content point with a changing pinch midpoint", () => {
    expect(
      zoomBetweenPoints(
        { scale: 1, x: 0, y: 0 },
        2,
        { x: 0, y: 0 },
        { x: 20, y: 10 },
        { width: 800, height: 600 },
        { width: 800, height: 600 },
      ),
    ).toEqual({ scale: 2, x: 20, y: 10 });
  });

  it("clamps translation to the scaled image edges", () => {
    expect(
      clampTransform(
        { scale: 2, x: 900, y: -500 },
        { width: 800, height: 600 },
        { width: 800, height: 600 },
      ),
    ).toEqual({ scale: 2, x: 400, y: -300 });
  });

  it("centers an image on axes where it is smaller than the stage", () => {
    expect(
      clampTransform(
        { scale: 2, x: 120, y: -80 },
        { width: 400, height: 200 },
        { width: 1000, height: 800 },
      ),
    ).toEqual({ scale: 2, x: 0, y: 0 });
  });

  it("resets translation when zoom returns to one", () => {
    expect(
      clampTransform(
        { scale: 0.75, x: 100, y: -100 },
        { width: 800, height: 600 },
        { width: 800, height: 600 },
      ),
    ).toEqual({ scale: 1, x: 0, y: 0 });
  });
});
