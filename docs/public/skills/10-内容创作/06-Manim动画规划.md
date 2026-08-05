---
name: manim-composer
description: |
  Create educational math/science videos in the 3Blue1Brown style using ManimGL.
  Combines visual storytelling principles with correct ManimGL implementation.
  Trigger when: User mentions "manim", "manimgl", "animation", "explainer video",
  "visualize", or wants to create mathematical animations.
---

# ManimGL Visual Explainer Skill

Create educational math/science videos in the 3Blue1Brown style. The key insight:
**visuals and narration are one inseparable thing** -- the words tell you what to
notice, the visuals show you why it's true, and they sync so understanding clicks
at the right moment.

## IMPORTANT: ManimGL Only

**Always use ManimGL, never ManimCE.**

```python
from manimlib import *  # NOT 'from manim import *'
```

- Import: `from manimlib import *`
- CLI: `manimgl`
- Package: `pip install manimgl`
- Scene class: `InteractiveScene` (not `Scene` from ManimCE)
- Creation animation: `ShowCreation` (not `Create`)
- LaTeX: `Tex(R"\pi")` (not `MathTex(r"\pi")`)
- Camera: `self.frame` (not `self.camera.frame` in newer versions)
- Fix to screen: `mob.fix_in_frame()` (not `self.add_fixed_in_frame_mobjects()`)

### Translating ManimCE Code (common online)

| ManimCE (DON'T use) | ManimGL (DO use) |
|----------------------|------------------|
| `from manim import *` | `from manimlib import *` |
| `manim` CLI | `manimgl` CLI |
| `MathTex(r"\pi")` | `Tex(R"\pi")` |
| `Scene` | `InteractiveScene` |
| `Create(mob)` | `ShowCreation(mob)` |
| `self.camera.frame` | `self.frame` |
| `self.add_fixed_in_frame_mobjects(mob)` | `mob.fix_in_frame()` |

---

## Core Principles

### 1. The Visual IS The Explanation

Bad: "Here's the equation, let me animate it appearing"
Good: "Here's a visual metaphor that makes the equation obvious"

The visuals should make concepts **undeniable**. When you see a grid transform
and watch basis vectors land somewhere, matrix multiplication MUST work the way
it does. There's nothing to memorize.

### 2. Questions Before Answers

Raise a question visually, let viewer wonder, reveal answer visually. Never
explain something the viewer isn't curious about yet. Create the gap first.

### 3. Algebra is "Horrible"

Show the geometric/visual understanding first. Then show the algebra as a
consequence. This positions visuals as primary, symbols as secondary.

### 4. Transform, Don't Replace

When possible, morph one visual into another rather than cutting. This shows the
CONNECTION between ideas.

```python
# BAD: cut between equations
self.play(FadeOut(eq1))
self.play(FadeIn(eq2))

# GOOD: morph to show relationship
self.play(TransformMatchingTex(eq1, eq2))
```

### 5. Color is Meaning

Consistent color coding throughout. In linear algebra:
- i-hat / x-component: green (X_COLOR)
- j-hat / y-component: red (Y_COLOR)
- k-hat / z-component: blue (Z_COLOR)
- Important results: yellow
- Transformations: teal, pink for different matrices

### 6. Concrete Then Abstract

Start with a specific example. THEN say "this works generally." Never start with
the general formula.

---

## The Composition Process

When asked to explain concept X:

### Step 1: Find the Visual Metaphor

Ask: "What physical/spatial thing behaves like this abstract concept?"

- Linear transformation: "smooshing space" while keeping grid parallel
- Matrix multiplication: applying one transformation then another
- Determinant: how much area/volume scales
- Derivative: slope of tangent = zoom in until curve looks straight
- Eigenvector: vector that stays on its span during transformation

The metaphor should make the math feel INEVITABLE, not arbitrary.

### Step 2: Design the Reveal Sequence

Pattern: Setup, Question, Build, Payoff.

1. **Setup**: Establish visual vocabulary (grid, basis vectors)
2. **Question**: What are we trying to understand?
3. **Build**: Show the visual step by step
4. **Payoff**: The "aha" moment

### Step 3: Write the Joint Script

For each beat, write BOTH:
- **NARRATION**: What are you saying?
- **VISUAL**: What is the viewer seeing?
- **WHY**: Why does this visual make the concept click?

### Step 4: Implement in ManimGL

Each `self.play()` is roughly one beat. Add `self.wait()` for pauses to let
insights land.

---

## ManimGL Quick Reference

### Basic Scene Structure

```python
from manimlib import *

class MyScene(InteractiveScene):
    def construct(self):
        circle = Circle(color=BLUE)
        self.play(ShowCreation(circle))
        self.wait()
```

### Interactive Development (ManimGL's killer feature)

```bash
manimgl scene.py MyScene -se 15   # Enter interactive mode at line 15
manimgl scene.py MyScene -w       # Write to file
manimgl scene.py MyScene -l       # Low quality (fast)
```

In the shell:
```python
checkpoint_paste()             # Run clipboard code with animations
checkpoint_paste(skip=True)    # Run instantly (no animations)
checkpoint_paste(record=True)  # Record while running
```

### LaTeX with Tex Class

```python
# Use capital R raw strings
formula = Tex(R"\int_0^1 x^2 \, dx = \frac{1}{3}")

# Color mapping
equation = Tex(R"E = mc^2", t2c={"E": BLUE, "m": GREEN, "c": YELLOW})

# Color after creation
formula.set_color_by_tex("n", BLUE)

# Text with inline math
sentence = TexText("The area is ", R"$\pi r^2$", ".")
```

### Camera Control

```python
frame = self.frame  # or self.camera.frame

# 2D: zoom and pan
self.play(frame.animate.scale(0.5))          # Zoom in
self.play(frame.animate.move_to(target))     # Pan

# 3D: reorient(theta, phi, gamma, center, height)
frame.reorient(20, 70)                       # Isometric view
self.play(frame.animate.reorient(60, 45))    # Animated rotation

# Fix 2D labels during 3D camera movement
title.fix_in_frame()

# Continuous rotation
frame.add_updater(lambda m, dt: m.increment_theta(20 * dt))
```

### Backstroke for Readability

```python
label = Tex(R"f(x)")
label.set_backstroke(BLACK, 5)  # Black outline behind text
```

### Post-Render Overflow Check (REQUIRED)

**After every render, run the overflow checker on the output video:**

```bash
python3 ~/.claude/skills/manim-composer/utilities/check_overflow.py <video.mp4>
```

This samples ~1 frame/second and checks for content clipped at frame edges.
If it reports FAIL, fix the layout and re-render. Do not deliver a video that fails.

---

## BEFORE COMPOSING: Required Reading & Research

**Do this before writing any scene code.** The SKILL.md gives you the principles
and one worked example. The reference repos give you Grant's actual patterns.

### Step 1: Search 3b1b's video code for inspiration

**3b1b's full video source code is cloned locally.** Search it for patterns relevant to
your topic before composing anything.

```
~/repos/3b1b/videos/    # 407 Python files, every 3b1b video (2015-2026)
~/repos/3b1b/manim/     # The ManimGL engine source + example_scenes.py
```

**How to search:**
- Use Grep to find scenes related to your topic:
  `Grep pattern="scatter\|residual\|regression" path="~/repos/3b1b/videos/"`
- Use Glob to browse a year: `Glob pattern="~/repos/3b1b/videos/_2024/**/*.py"`
- Read interesting files to study composition patterns, visual techniques, updater usage

**What to look for:**
- How Grant structures scenes for similar concepts (data viz, transforms, algebra)
- His updater patterns, camera work, color schemes, timing
- How he decomposes a concept into visual beats
- Helper functions and reusable patterns in `custom/` directory

**Key directories in the videos repo:**
- `_2016/eola/` -- Essence of Linear Algebra (the classic series)
- `_2024/transformers/` -- Attention/transformers explainer
- `_2024/linalg/` -- More linear algebra content
- `_2025/laplace/` -- Laplace transform
- `_2025/grover/` -- Grover's algorithm
- `_2018/fourier.py` -- Fourier series
- `custom/` -- Reusable components (Pi creatures, backdrops, drawings)

**IMPORTANT:** The video code uses `from manim_imports_ext import *` and video-specific
helpers. Don't copy code literally -- study the COMPOSITION and adapt to standard
`from manimlib import *` APIs.

### Step 2: Read the annotated scenes

Read [references/eola-annotated-scenes.md](references/eola-annotated-scenes.md) --
Annotated scenes from the EOLA series with NARRATION/VISUAL/WHY comment blocks.
Uses older APIs (don't copy literally), but the COMPOSITION PATTERNS are gold.

### Step 3: Read the API rules for your topic

Read the relevant rules/ files for ManimGL API (scenes, animations, transforms, tex,
camera, etc.) to get the code right.

### Step 4: Pick the narrative structure

Read [references/narrative-patterns.md](references/narrative-patterns.md) to pick the
right story shape (Mystery->Resolution, Build->Payoff, Two Perspectives->Unity, etc.)

---

## Composition Rules (from studying 3b1b's actual video code)

These patterns make the difference between "animated math" and "visual explanation":

### Labels sync with transforms
Text appears WITH the visual action, not before or after. When the grid rotates,
the label "90 degree rotation" appears during the rotation. The viewer reads AND
sees simultaneously.

### One protagonist object per concept
Pick ONE visual object that embodies the concept. For determinants: the unit square
(watch its area change). For linear transforms: the basis vectors (watch where they
land). For derivatives: the tangent line (watch it appear as you zoom in). Everything
else is supporting cast.

### Questions get answered by watching, not explaining
Don't narrate "matrix multiplication is not commutative." Instead: show M1*M2 applied
to the grid. Then show M2*M1. The grids look different. That's the proof. The viewer
saw it. Add "???" then morph to "≠". The narration just names what happened.

### Curved paths for conceptual swaps
When two things swap (M1*M2 vs M2*M1), use `path_arc` so the viewer sees them
crossing. A straight swap is invisible. A curved swap is a visual argument.

### Formula emerges from geometry
The ad-bc formula for determinants should emerge from watching parallelogram area
change, not appear and then get "verified." Geometry first, algebra as consequence.

### Continuity reveals structure
det=0 means area collapses to a line. Negative det means orientation flips. These
aren't separate facts -- they're what happens when you smoothly move through the
space of transformations. Show the continuous change.

---

## Worked Example: The Derivative (correct ManimGL)

This shows the full composition pattern applied to "derivative = slope of tangent =
zoom in until the curve looks straight." Study the STRUCTURE, not just the code.

```python
from manimlib import *
# =============================================================================
# SCENE 1: TheQuestion
# -----------------------------------------------------------------------------
# NARRATION: "What does it mean to take the derivative of a function?
#            We write df/dx, but what IS that?"
#
# VISUAL: Curve appears. Formula df/dx fades in with a question mark.
# WHY: Create the gap. The viewer now WANTS to know. Don't answer yet.
# =============================================================================
class TheQuestion(InteractiveScene):
    def construct(self):
        axes = Axes(x_range=[-1, 5], y_range=[-1, 4])
        curve = axes.get_graph(lambda x: 0.15 * x**2, color=BLUE)

        self.play(ShowCreation(axes), run_time=1)
        self.play(ShowCreation(curve), run_time=1.5)

        formula = Tex(R"\frac{df}{dx}", R"\;= \;?")
        formula[0].set_color(YELLOW)
        formula.to_edge(UP)
        formula.set_backstroke(BLACK, 5)

        self.play(Write(formula))
        self.wait(2)  # Let the question land


# =============================================================================
# SCENE 2: ZoomReveal
# -----------------------------------------------------------------------------
# NARRATION: "Pick a point. Now zoom in. Keep zooming. The curve...
#            starts to look like a straight line."
#
# VISUAL: Dot on curve. Camera zooms in smoothly. Curve flattens to a line.
# WHY: This IS the derivative. Not a formula -- a visual fact. When you zoom
#      in far enough, every smooth curve is locally linear. The slope of
#      that line is df/dx. The viewer SEES this, so the formula is obvious.
# =============================================================================
class ZoomReveal(InteractiveScene):
    def construct(self):
        axes = Axes(x_range=[-1, 5], y_range=[-1, 4])
        curve = axes.get_graph(lambda x: 0.15 * x**2, color=BLUE)
        self.add(axes, curve)

        # Protagonist: the point we're zooming into
        x_val = 2.5
        dot = Dot(axes.c2p(x_val, 0.15 * x_val**2), color=YELLOW)
        dot.set_z_index(1)
        self.play(FadeIn(dot, scale=0.5))

        label = Tex(R"x = 2.5")
        label.next_to(dot, UR, buff=0.15)
        label.set_backstroke(BLACK, 5)
        self.play(Write(label))
        self.wait()

        # THE ZOOM -- the concept IS the visual
        frame = self.frame
        self.play(
            frame.animate.set_height(1.5).move_to(dot),
            run_time=4,  # Slow -- let the viewer watch the curve straighten
        )
        self.wait(2)  # Pause. Let it land. "It looks like a line."

        # Now show the tangent -- it matches what the zoomed curve looks like
        tangent = axes.get_graph(
            lambda x: 0.75 * (x - x_val) + 0.15 * x_val**2,
            color=GREEN,
        )
        self.play(ShowCreation(tangent), run_time=1.5)

        slope_label = Tex(R"\text{slope} = \frac{df}{dx}")
        slope_label.set_color(GREEN)
        slope_label.next_to(dot, RIGHT, buff=0.1)
        slope_label.scale(0.15)  # Small because we're zoomed in
        slope_label.set_backstroke(BLACK, 3)
        self.play(Write(slope_label))
        self.wait(2)


# =============================================================================
# SCENE 3: TheFormula
# -----------------------------------------------------------------------------
# NARRATION: "So the derivative is just the slope of this tangent line.
#            Rise over run. df over dx."
#
# VISUAL: Zoom back out. Tangent line visible. Rise/run triangle appears.
#         df/dx label morphs from question mark to the actual slope value.
# WHY: Formula is now OBVIOUS because the viewer already saw the geometry.
#      They're not memorizing -- they're recognizing.
# =============================================================================
class TheFormula(InteractiveScene):
    def construct(self):
        axes = Axes(x_range=[-1, 5], y_range=[-1, 4])
        curve = axes.get_graph(lambda x: 0.15 * x**2, color=BLUE)
        x_val = 2.5
        tangent = axes.get_graph(
            lambda x: 0.75 * (x - x_val) + 0.15 * x_val**2,
            color=GREEN,
        )
        dot = Dot(axes.c2p(x_val, 0.15 * x_val**2), color=YELLOW)
        dot.set_z_index(1)
        self.add(axes, curve, tangent, dot)

        # Rise/run triangle -- the geometry that IS the formula
        x0, x1 = 2.0, 3.0
        y0 = 0.75 * (x0 - x_val) + 0.15 * x_val**2
        y1 = 0.75 * (x1 - x_val) + 0.15 * x_val**2

        run_line = Line(axes.c2p(x0, y0), axes.c2p(x1, y0), color=RED)
        rise_line = Line(axes.c2p(x1, y0), axes.c2p(x1, y1), color=YELLOW)

        run_label = Tex(R"dx", color=RED)
        run_label.next_to(run_line, DOWN, buff=0.1)
        run_label.set_backstroke(BLACK, 4)

        rise_label = Tex(R"df", color=YELLOW)
        rise_label.next_to(rise_line, RIGHT, buff=0.1)
        rise_label.set_backstroke(BLACK, 4)

        self.play(ShowCreation(run_line), ShowCreation(rise_line))
        self.play(Write(run_label), Write(rise_label))
        self.wait()

        # The payoff: formula morphs from question to answer
        question = Tex(R"\frac{df}{dx} = \;?")
        question.to_edge(UP)
        question.set_backstroke(BLACK, 5)
        self.play(Write(question))
        self.wait()

        answer = Tex(R"\frac{df}{dx} = 0.75")
        answer.to_edge(UP)
        answer.set_backstroke(BLACK, 5)
        self.play(TransformMatchingTex(question, answer))
        self.wait(2)
```

### What to notice in this example

1. **Scene 1 creates the gap.** It asks a question and stops. No answer yet.
2. **Scene 2 is the concept.** The zoom IS the derivative. Not a picture of it -- it IS it.
   When the curve straightens, df/dx becomes visually obvious.
3. **Scene 3 harvests the formula.** The algebra is a CONSEQUENCE of the visual. Rise/run
   triangle maps directly to df/dx. The "?" morphs to "0.75" -- the question from Scene 1
   gets answered.
4. **Protagonist object**: the dot. Everything happens relative to it.
5. **Timing matters**: the 4-second zoom is slow ON PURPOSE. The insight needs time to land.
6. **Labels sync with action**: slope_label appears right after the tangent line, not before.

---

## Output Format

When using this skill, produce a Python file following the worked example above:

1. **Scene class per major beat** (not one giant scene)
2. **Comment blocks** showing NARRATION, VISUAL, WHY for each scene -- these are
   the COMPOSITION, not just labels. WHY must explain what makes this visual click.
3. **Consistent color coding** throughout (same concept = same color always)
4. **Protagonist object** that carries the concept (one per scene/section)
5. **Questions raised then answered** visually (create gap, let it breathe, fill it)
6. **Morphing over cutting** -- TransformMatchingTex, not FadeOut/FadeIn
7. **Timing with intention** -- slow for insights (2-4s), fast for setup (0.5-1s)
8. **Labels sync with action** -- text appears DURING the visual, not before
9. **Run overflow check after render** -- see "Post-Render Overflow Check" above. Fix and re-render if it fails.

---

## When NOT to Use This Approach

- **Pure computation tutorials** -- if teaching an algorithm step-by-step, a screencast may be better
- **Simple facts** -- don't animate "2+2=4"
- **Already visual topics** -- if the concept is already a picture, you might not need elaborate animation

Use this skill when there's an abstract concept that becomes obvious with the right visual metaphor.

---

## Reference Files

### 3b1b Source Repos (local clones -- search these!)
- `~/repos/3b1b/videos/` -- **Every 3b1b video's source code** (2015-2026, 407 .py files, ~494k lines)
- `~/repos/3b1b/manim/` -- **ManimGL engine source** + `example_scenes.py`
- Grant's own CLAUDE.md is at `~/repos/3b1b/videos/CLAUDE.md` -- read it for his patterns

### Composition & Narrative
- [references/narrative-patterns.md](references/narrative-patterns.md) -- Six narrative structures for math explainers
- [references/scene-examples.md](references/scene-examples.md) -- Scene breakdown examples (dot product, Fourier, matrices)
- [references/visual-techniques.md](references/visual-techniques.md) -- Visual patterns, timing, color palettes, layout
- [references/eola-annotated-scenes.md](references/eola-annotated-scenes.md) -- Annotated code from 3b1b's EOLA series (composition reference, uses older APIs)

### ManimGL API (verified correct)
- [rules/scenes.md](rules/scenes.md) -- InteractiveScene, Scene types, construct method
- [rules/tex.md](rules/tex.md) -- Tex class, raw strings, t2c color mapping
- [rules/animations.md](rules/animations.md) -- Animation classes, playing, timing
- [rules/creation-animations.md](rules/creation-animations.md) -- ShowCreation, Write, FadeIn
- [rules/transform-animations.md](rules/transform-animations.md) -- Transform, ReplacementTransform, TransformMatchingTex
- [rules/camera.md](rules/camera.md) -- frame.reorient(), Euler angles, fix_in_frame()
- [rules/interactive.md](rules/interactive.md) -- Interactive mode, checkpoint_paste()
- [rules/3d.md](rules/3d.md) -- 3D objects, surfaces, lighting
- [rules/mobjects.md](rules/mobjects.md) -- Mobject types, VMobject, Groups, positioning
- [rules/colors.md](rules/colors.md) -- Color constants, gradients, GLSL
- [rules/styling.md](rules/styling.md) -- Fill, stroke, opacity, backstroke

### Working Examples (standalone, runnable)
- [examples/](examples/) -- 30+ tested example files (3D surfaces, vector fields, equation transforms, etc.)

### Templates
- [templates/basic_scene.py](templates/basic_scene.py) -- Standard 2D scene
- [templates/interactive_scene.py](templates/interactive_scene.py) -- InteractiveScene with self.embed()
- [templates/3d_scene.py](templates/3d_scene.py) -- 3D scene with frame.reorient()
- [templates/math_scene.py](templates/math_scene.py) -- Mathematical derivations
- [templates/scenes-template.md](templates/scenes-template.md) -- Planning template for multi-scene videos

### Utilities
- [utilities/validation.py](utilities/validation.py) -- Catches off-screen content and overlaps before render

---

## License & Attribution

Example code adapted from [3Blue1Brown's video repository](https://github.com/3b1b/videos) by Grant Sanderson.

**License:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- Attribution required -- credit 3Blue1Brown and the adapter
- NonCommercial -- not for commercial use
- ShareAlike -- derivatives must use the same license
