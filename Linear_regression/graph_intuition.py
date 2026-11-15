"""
linear_regression_to_nn.py
==========================

"একটি সরল রেখা থেকে নিউরাল নেটওয়ার্ক"
Linear Regression → Neural Network, told slowly in 8 narrated scenes (Bengali).

Dataset used throughout:   x = 0, 1, 2, 3     y = 1, 3, 5, 7     (i.e. y = 2x + 1)

Quick start
-----------
    # one scene, fast preview
    manim -pql linear_regression_to_nn.py S02_Data

    # final quality, all scenes, stitched into one file
    bash render.sh

Scene order
-----------
    S01_Intro  S02_Data  S03_Line  S04_Noise
    S05_GradientDescent  S06_Neuron  S07_Network  S08_Modern

Notes
-----
* Bengali is rendered through Pango (never LaTeX), so conjuncts like ক্ষ / ন্ন
  shape correctly. A Bengali font must be installed on your machine:
  Noto Sans Bengali (Linux/Google Fonts), Hind Siliguri, Kalpurush (very common
  in Bangladesh), or Nirmala UI (Windows). The script auto-detects one; force
  it with BN_FONT_FORCE below.
* Maths is real LaTeX (MathTex), so a LaTeX install is required (Manim
  requirement anyway).
* Every number used on screen is computed with numpy, not hard-coded, so the
  least-squares fit and the gradient-descent steps are honest.
"""

from __future__ import annotations

import numpy as np
from manim import *

# --------------------------------------------------------------------------
# 0. Look & feel
# --------------------------------------------------------------------------
config.background_color = "#0E1116"

C_DATA = "#FFD166"    # data points
C_LINE = "#4CC9F0"    # the model / the line
C_FIT = "#06D6A0"     # good answer / optimum
C_BAD = "#EF476F"     # error, residuals
C_NEURON = "#B197FC"  # neurons
C_DIM = "#8B95A5"     # secondary text
C_EDGE = "#5A6472"    # network edges
C_AXIS = "#4A5261"    # axes

BENGALI_FONT_CANDIDATES = [
    "Noto Sans Bengali",   # Linux / Google Fonts
    "Hind Siliguri",       # Google Fonts
    "Kalpurush",           # extremely common on Bangla systems
    "Nirmala UI",          # Windows
    "Mukti Narrow",
    "Lohit Bengali",
    "Vrinda",
]
BN_FONT_FORCE = None       # e.g. "Kalpurush"


def _pick_bengali_font() -> str:
    if BN_FONT_FORCE:
        return BN_FONT_FORCE
    try:
        import manimpango
        installed = {f.lower() for f in manimpango.list_fonts()}
    except Exception:
        installed = set()
    for f in BENGALI_FONT_CANDIDATES:
        if f.lower() in installed:
            return f
    return BENGALI_FONT_CANDIDATES[0]


BN = _pick_bengali_font()


def bn(text: str, size: float = 32, color=WHITE, **kw) -> Text:
    """Bengali text (ligatures ON — that is what makes যুক্তাক্ষর render)."""
    return Text(text, font=BN, font_size=size, color=color,
                disable_ligatures=False, **kw)


# --------------------------------------------------------------------------
# 1. The data (all numbers below are computed, never faked)
# --------------------------------------------------------------------------
X = np.array([0.0, 1.0, 2.0, 3.0])
Y = np.array([1.0, 3.0, 5.0, 7.0])          # clean: y = 2x + 1
TRUE_W, TRUE_B = 2.0, 1.0

# the same four inputs, but with real-world noise
X_N = np.array([0.0, 1.0, 2.0, 3.0])
Y_N = np.array([0.8, 3.4, 4.6, 7.2])


def least_squares(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    w = float(np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2))
    b = float(y.mean() - w * x.mean())
    return w, b


W_FIT, B_FIT = least_squares(X_N, Y_N)


def sse(w: float, b: float, x: np.ndarray = X_N, y: np.ndarray = Y_N) -> float:
    return float(np.sum((y - (w * x + b)) ** 2))


# --------------------------------------------------------------------------
# 2. Building blocks
# --------------------------------------------------------------------------
def data_axes(x_range=(-0.5, 4.8, 1), y_range=(-0.7, 9.6, 1),
              x_length=7.4, y_length=4.3, num_size=22, center=ORIGIN) -> Axes:
    ax = Axes(
        x_range=list(x_range), y_range=list(y_range),
        x_length=x_length, y_length=y_length,
        axis_config=dict(color=C_AXIS, stroke_width=2.5, include_ticks=True,
                         tick_size=0.05, include_numbers=False),
    )
    ax.shift(center)
    labels = VGroup()
    for v in (0, 1, 2, 3, 4):
        labels.add(MathTex(str(v), font_size=num_size, color=C_DIM)
                   .next_to(ax.c2p(v, 0), DOWN, buff=0.16))
    for v in (2, 4, 6, 8):
        labels.add(MathTex(str(v), font_size=num_size, color=C_DIM)
                   .next_to(ax.c2p(0, v), LEFT, buff=0.16))
    ax.labels = labels
    return ax


def point(ax: Axes, x, y, color=C_DATA, r=0.075) -> Dot:
    return Dot(ax.c2p(x, y), radius=r, color=color)


def coord_label(ax: Axes, x, y, size=20, color=C_DIM, direction=UR) -> MathTex:
    return MathTex(f"({x:g},{y:g})", font_size=size, color=color) \
        .next_to(ax.c2p(x, y), direction, buff=0.09)


def model_line(ax: Axes, w: float, b: float, color=C_LINE, width=4.0) -> ParametricFunction:
    x_from = ax.x_range[0] + 0.35
    x_to = ax.x_range[1] - 0.35
    return ax.plot(lambda x: w * x + b, x_range=[x_from, x_to, 0.01],
                   color=color, stroke_width=width, use_smoothing=False)


def residual_picture(ax: Axes, x, y, w: float, b: float,
                     color=C_BAD, alpha=1.0) -> VGroup:
    """Dashed residual + the classic 'square of the error' for each point."""
    yscale = ax.y_length / (ax.y_range[1] - ax.y_range[0])
    grp = VGroup()
    for xi, yi in zip(x, y):
        yhat = w * xi + b
        r = yi - yhat
        grp.add(DashedLine(
            ax.c2p(xi, yi), ax.c2p(xi, yhat),
            color=color, stroke_width=2.0, dash_length=0.055,
            stroke_opacity=0.95 * alpha,
        ))
        if abs(r) > 0.02:
            side = 0.62 * abs(r) * yscale   # 0.62 is cosmetic: area is still ∝ r²
            sq = Square(side_length=side, stroke_color=color, stroke_width=1.2,
                        fill_color=color, fill_opacity=0.20 * alpha)
            sq.set_stroke(opacity=0.9 * alpha)
            base = ax.c2p(xi, min(yi, yhat))
            up = UP if r > 0 else DOWN
            sq.move_to(base + RIGHT * side / 2 + up * side / 2)
            grp.add(sq)
    return grp


def node(label=None, radius=0.40, color=C_NEURON, offset=ORIGIN) -> VGroup:
    c = Circle(radius=radius, color=color, stroke_width=2.5)
    parts = VGroup(c)
    if label is not None:
        t = label.copy() if isinstance(label, Mobject) else MathTex(label, font_size=30, color=WHITE)
        t.move_to(c.get_center())
        parts.add(t)
    parts.shift(offset)
    return parts


def connect(a: Mobject, b: Mobject, ra=0.40, rb=0.40,
            color=C_EDGE, width=2.0, opacity=0.75) -> Line:
    d = b.get_center() - a.get_center()
    u = d / np.linalg.norm(d)
    return Line(a.get_center() + u * ra, b.get_center() - u * rb,
                color=color, stroke_width=width, stroke_opacity=opacity)


def mid(a: Mobject, b: Mobject, shift_=UP * 0.24) -> np.ndarray:
    return (a.get_center() + b.get_center()) / 2 + shift_


# --------------------------------------------------------------------------
# 3. Scene base class: Bengali subtitles + safe updater swaps
# --------------------------------------------------------------------------
class NarratedScene(Scene):
    caption_size = 34

    def say(self, text, size=None, color=WHITE, run_time=0.7, hold=0.9):
        new = bn(text, size=size or self.caption_size, color=color) \
            .to_edge(DOWN, buff=0.34)
        if new.width > 13.2:
            new.scale_to_fit_width(13.2)
        anims = [FadeIn(new, shift=UP * 0.12)]
        old = getattr(self, "_cap", None)
        if old is not None:
            anims.append(FadeOut(old, shift=UP * 0.12))
        self.play(*anims, run_time=run_time)
        self._cap = new
        if hold:
            self.wait(hold)
        return new

    def drop_caption(self, run_time=0.5):
        old = getattr(self, "_cap", None)
        if old is not None:
            self.play(FadeOut(old, shift=DOWN * 0.12), run_time=run_time)
            self._cap = None

    def swap(self, old: Mobject, new: Mobject):
        """Hand a static stand-in over to a live (updater-driven) mobject."""
        self.add(new)
        self.remove(old)

    def fade_all(self, run_time=1.0):
        vis = [m for m in self.mobjects if not isinstance(m, ValueTracker)]
        if vis:
            self.play(*[FadeOut(m) for m in vis], run_time=run_time)
        self._cap = None


# ==========================================================================
# SCENE 1 — title
# ==========================================================================
class S01_Intro(Scene):
    def construct(self):
        t1 = bn("একটি সরল রেখা", size=64)
        t2 = bn("থেকে নিউরাল নেটওয়ার্ক", size=64, color=C_LINE)
        head = VGroup(t1, t2).arrange(DOWN, buff=0.30).move_to(UP * 0.95)

        sub = bn("লিনিয়ার রিগ্রেশন কীভাবে আধুনিক নিউরাল নেটওয়ার্কের শুরু", size=30, color=C_DIM)
        sub.next_to(head, DOWN, buff=0.75)
        if sub.width > 12.8:
            sub.scale_to_fit_width(12.8)

        rule = Line(LEFT * 3.2, RIGHT * 3.2, color=C_LINE,
                    stroke_width=1.6, stroke_opacity=0.5)
        rule.next_to(sub, DOWN, buff=0.55)

        self.play(FadeIn(t1, shift=UP * 0.35), run_time=1.4)
        self.play(FadeIn(t2, shift=UP * 0.35), run_time=1.2)
        self.wait(0.4)
        self.play(FadeIn(sub, shift=UP * 0.20), run_time=1.0)
        self.play(Create(rule), run_time=0.9)

        # teaser: the four dots and the line they live on
        ax = Axes(x_range=[-0.4, 3.9, 1], y_range=[0, 7.6, 1],
                  x_length=5.0, y_length=1.9, axis_config=dict(stroke_opacity=0))
        ax.move_to(DOWN * 2.45)
        teaser = ax.plot(lambda x: TRUE_W * x + TRUE_B, x_range=[-0.25, 3.35, 0.01],
                         color=C_LINE, stroke_width=3)
        dots = VGroup(*[Dot(ax.c2p(x, y), radius=0.065, color=C_DATA) for x, y in zip(X, Y)])
        self.play(Create(teaser), run_time=1.3)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.25), run_time=1.4)
        self.wait(1.4)

        self.play(FadeOut(VGroup(head, sub, rule, teaser, dots), shift=UP * 0.3), run_time=1.0)


# ==========================================================================
# SCENE 2 — the data
# ==========================================================================
class S02_Data(NarratedScene):
    def construct(self):
        ax = data_axes(center=UP * 0.45)
        xlab = MathTex("x", font_size=30, color=C_DIM).next_to(ax.c2p(4.45, 0), DR, buff=0.06)
        ylab = MathTex("y", font_size=30, color=C_DIM).next_to(ax.c2p(0, 9.3), UR, buff=0.02)

        self.say("ধরেন আপনার কাছে এমন কিছু ডাটা আছে", hold=1.2)

        self.play(Create(ax), FadeIn(ax.labels), FadeIn(xlab), FadeIn(ylab), run_time=1.6)
        self.wait(0.5)

        dots, labels = VGroup(), VGroup()
        for x, y in zip(X, Y):
            d, l = point(ax, x, y), coord_label(ax, x, y)
            self.play(GrowFromCenter(d), FadeIn(l, shift=UP * 0.1), run_time=0.65)
            self.wait(0.20)
            dots.add(d)
            labels.add(l)
        self.wait(0.4)

        self.say("চারটি ইনপুট — x = 0, 1, 2, 3", hold=0.8)
        self.say("আর প্রতিটির জন্য একটি করে আউটপুট — y = 1, 3, 5, 7", hold=1.0)

        table = VGroup(
            MathTex(r"x = 0,\ 1,\ 2,\ 3", font_size=32, color=C_DATA),
            MathTex(r"y = 1,\ 3,\ 5,\ 7", font_size=32, color=C_LINE),
        ).arrange(DOWN, buff=0.30, aligned_edge=LEFT)
        table.to_corner(UR, buff=0.55).shift(DOWN * 0.30)

        self.play(FadeIn(table, shift=LEFT * 0.2), run_time=1.0)
        self.say("মেশিনের কাজ — এই বিন্দুগুলোতে লুকিয়ে থাকা প্যাটার্নটি খুঁজে বের করা", hold=1.2)

        q = MathTex(r"x = 4 \ \Rightarrow\ y = ?", font_size=42, color=C_FIT)
        q.next_to(table, DOWN, buff=0.50, aligned_edge=RIGHT)

        guide = DashedLine(ax.c2p(4, 0), ax.c2p(4, 9.2), color=C_FIT,
                           stroke_width=1.6, dash_length=0.08, stroke_opacity=0.55)
        self.play(Create(guide), run_time=1.0)
        self.play(Write(q), run_time=1.2)
        self.say("প্রশ্ন — x = 4 হলে y কত হবে?", color=C_FIT, hold=1.8)

        self.fade_all(run_time=1.0)


# ==========================================================================
# SCENE 3 — the line that explains them
# ==========================================================================
class S03_Line(NarratedScene):
    def construct(self):
        ax = data_axes(center=UP * 0.45)
        dots = VGroup(*[point(ax, x, y) for x, y in zip(X, Y)])
        labels = VGroup(*[coord_label(ax, x, y) for x, y in zip(X, Y)])

        self.play(Create(ax), FadeIn(ax.labels), run_time=1.2)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.12),
                  LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.12), run_time=1.2)

        self.say("খেয়াল করুন — চারটি বিন্দুই একটি সরল রেখার উপর পড়েছে", hold=1.0)

        line = model_line(ax, TRUE_W, TRUE_B)
        self.play(Create(line), run_time=2.0)
        self.say("রেখাটি টানলে সব কটি বিন্দুকে ছুঁয়ে যায়", hold=0.9)
        self.play(LaggedStart(*[Indicate(d, scale_factor=1.7, color=WHITE) for d in dots],
                              lag_ratio=0.18), run_time=1.6)

        # --- the equation of a line ---
        eq = MathTex(r"\hat{y}", "=", "w", "x", "+", "b", font_size=52)
        eq[0].set_color(C_FIT)
        eq[2].set_color(C_DATA)
        eq[5].set_color(C_LINE)
        eq.to_corner(UR, buff=0.65).shift(DOWN * 0.45)

        self.play(Write(eq), run_time=1.4)
        self.say("সরল রেখার সমীকরণ — y-hat = w x যোগ b", hold=0.9)

        vals = MathTex(r"w = 2,\quad b = 1", font_size=40, color=C_DIM)
        vals.next_to(eq, DOWN, buff=0.45, aligned_edge=RIGHT)
        self.play(FadeIn(vals, shift=DOWN * 0.15), run_time=0.9)
        self.say("এখানে ঢাল w = 2, আর রেখাটি y-অক্ষকে ছোঁয় b = 1 বিন্দুতে", hold=1.0)

        concrete = MathTex(r"\hat{y} = 2x + 1", font_size=46, color=C_LINE)
        concrete.next_to(vals, DOWN, buff=0.40, aligned_edge=RIGHT)
        self.play(TransformFromCopy(eq, concrete), run_time=1.2)
        self.wait(0.6)

        # --- answer the question from scene 2 ---
        self.say("তাহলে উত্তর — x = 4 বসালে y-hat = 2 গুণ 4 যোগ 1 = 9", color=C_FIT, hold=0.6)

        pred = Dot(ax.c2p(4, 9), radius=0.09, color=C_FIT).set_fill(opacity=0.0)
        pred.set_stroke(C_FIT, 3)
        glow = Dot(ax.c2p(4, 9), radius=0.22, color=C_FIT).set_opacity(0.18)
        pred_lbl = MathTex(r"(4,\,9)", font_size=26, color=C_FIT).next_to(pred, UR, buff=0.10)
        dashed = DashedLine(ax.c2p(4, 0), ax.c2p(4, 9), color=C_FIT,
                            stroke_width=1.5, dash_length=0.07, stroke_opacity=0.5)

        self.play(Create(dashed), GrowFromCenter(pred), FadeIn(glow), FadeIn(pred_lbl), run_time=1.3)
        self.wait(1.6)
        self.say("অর্থাৎ মেশিন এখন নতুন ইনপুটের জন্যও উত্তর দিতে শিখে গেছে", color=C_FIT, hold=1.6)

        self.fade_all(run_time=1.0)


# ==========================================================================
# SCENE 4 — noise, residuals, loss
# ==========================================================================
class S04_Noise(NarratedScene):
    def construct(self):
        ax = data_axes(center=UP * 0.45)
        clean = VGroup(*[point(ax, x, y) for x, y in zip(X, Y)])
        noisy = VGroup(*[point(ax, x, y) for x, y in zip(X_N, Y_N)])

        self.play(Create(ax), FadeIn(ax.labels), FadeIn(clean), run_time=1.1)
        self.wait(0.3)

        self.say("বাস্তব জীবনের ডাটা কিন্তু এত পরিষ্কার হয় না — একটু শব্দ (noise) থাকে", hold=0.7)
        self.play(Transform(clean, noisy), run_time=1.8)
        self.play(LaggedStart(*[Indicate(d, scale_factor=1.6, color=C_BAD) for d in noisy],
                              lag_ratio=0.15), run_time=1.3)
        self.wait(0.4)

        # --- a deliberately bad line, driven by trackers ---
        w_tr, b_tr = ValueTracker(1.05), ValueTracker(0.55)
        static_line = model_line(ax, w_tr.get_value(), b_tr.get_value(), color=C_BAD)
        self.play(Create(static_line), run_time=1.2)
        line = always_redraw(lambda: model_line(ax, w_tr.get_value(), b_tr.get_value(),
                                                color=C_BAD))
        self.add(w_tr, b_tr)
        self.swap(static_line, line)
        self.say("তাহলে সবচেয়ে ভালো রেখাটি কোনটি? এই রেখাটি নিশ্চয়ই নয়", hold=0.9)

        # --- residuals, with squares appearing ---
        alpha_tr = ValueTracker(0.0)
        self.add(alpha_tr)
        res = always_redraw(lambda: residual_picture(
            ax, X_N, Y_N, w_tr.get_value(), b_tr.get_value(), alpha=alpha_tr.get_value()))
        self.add(res)
        self.play(alpha_tr.animate.set_value(1.0), run_time=1.8)
        self.say("প্রতিটি বিন্দু থেকে রেখার দূরত্ব হলো ভুল — residual", hold=1.0)
        self.say("ভুলটিকে বর্গ করলে একটি বড় ভুল আরও বেশি শাস্তি পায়", hold=1.0)

        # --- the loss read-out ---
        loss_label = MathTex(r"L(w,b)=\sum_{i}\left(y_i-\hat{y}_i\right)^2", font_size=38)
        loss_label.to_corner(UL, buff=0.65).shift(DOWN * 0.25)
        loss_eq = MathTex("=", font_size=38).next_to(loss_label, RIGHT, buff=0.14)
        loss_num = DecimalNumber(sse(w_tr.get_value(), b_tr.get_value()),
                                 num_decimal_places=2, font_size=38, color=C_BAD)
        loss_num.next_to(loss_eq, RIGHT, buff=0.14)

        self.play(Write(loss_label), FadeIn(loss_eq), FadeIn(loss_num), run_time=1.2)
        loss_num.add_updater(lambda m: m.set_value(
            sse(w_tr.get_value(), b_tr.get_value())))
        self.say("সব বর্গ যোগ করলে পাই loss — সংখ্যাটি যত ছোট, রেখা তত ভালো", hold=1.4)

        self.play(w_tr.animate.set_value(1.75), b_tr.animate.set_value(1.55), run_time=2.0)
        self.play(w_tr.animate.set_value(1.05), b_tr.animate.set_value(0.55), run_time=2.0)
        self.say("w আর b বদলালেই loss বদলায় — তাহলে সবচেয়ে ছোট loss কোথায়?", hold=1.2)

        self.drop_caption()
        self.fade_all(run_time=1.0)


# ==========================================================================
# SCENE 5 — gradient descent
# ==========================================================================
class S05_GradientDescent(NarratedScene):
    def construct(self):
        # ---------------- left: data + the line ----------------
        ax = data_axes(x_length=6.2, y_length=4.0, center=LEFT * 3.55 + UP * 0.55)
        dots = VGroup(*[point(ax, x, y, r=0.07) for x, y in zip(X_N, Y_N)])
        self.play(Create(ax), FadeIn(ax.labels), FadeIn(dots), run_time=1.0)

        # ---------------- right: the loss curve ----------------
        w_lo, w_hi = 0.6, 3.2
        L_max = max(sse(w, B_FIT) for w in np.linspace(w_lo, w_hi, 200))
        axL = Axes(
            x_range=[w_lo, w_hi, 0.5], y_range=[0, L_max * 1.10, L_max / 4],
            x_length=5.0, y_length=3.4,
            axis_config=dict(color=C_AXIS, stroke_width=2.5, include_ticks=True,
                             tick_size=0.05, include_numbers=False),
        )
        axL.move_to(RIGHT * 3.45 + UP * 0.45)
        axL_labs = VGroup(
            MathTex("w", font_size=30, color=C_DIM).next_to(axL.c2p(w_hi, 0), RIGHT, buff=0.14),
            MathTex(r"L(w)", font_size=28, color=C_DIM).next_to(axL.c2p(w_lo, L_max * 1.05), UP, buff=0.08),
        )
        curve = axL.plot(lambda w: sse(w, B_FIT), x_range=[w_lo, w_hi, 0.01],
                         color=C_LINE, stroke_width=3.5)
        self.play(Create(axL), FadeIn(axL_labs), run_time=1.0)
        self.play(Create(curve), run_time=1.6)
        self.say("loss আর w-এর সম্পর্ক — একটি বাঁকা রেখা, একটি উপত্যকার মতো", hold=0.8)
        self.say("সহজ রাখতে b ধরে রেখে শুধু w বদলাচ্ছি", hold=0.8)

        # ---------------- shared tracker ----------------
        w_tr = ValueTracker(1.05)
        b_tr = ValueTracker(B_FIT)
        self.add(w_tr, b_tr)

        static_line = model_line(ax, w_tr.get_value(), b_tr.get_value())
        self.play(Create(static_line), run_time=1.0)
        line = always_redraw(lambda: model_line(ax, w_tr.get_value(), b_tr.get_value()))
        self.swap(static_line, line)

        def loss_now():
            return sse(w_tr.get_value(), B_FIT)

        static_dot = Dot(axL.c2p(1.05, sse(1.05, B_FIT)), radius=0.085, color=C_FIT)
        self.play(GrowFromCenter(static_dot), run_time=0.6)
        mover = always_redraw(lambda: Dot(axL.c2p(w_tr.get_value(), loss_now()),
                                          radius=0.085, color=C_FIT))
        drop = always_redraw(lambda: DashedLine(
            axL.c2p(w_tr.get_value(), 0), axL.c2p(w_tr.get_value(), loss_now()),
            color=C_FIT, stroke_width=1.2, dash_length=0.05, stroke_opacity=0.45))
        self.swap(static_dot, VGroup(mover, drop))

        self.say("উপরে থেকে একটি বল গড়িয়ে নামালে যেখানে থামবে, সেটাই সবচেয়ে ছোট loss", hold=1.1)

        # ---------------- the update rule ----------------
        rule = MathTex(r"w \;\leftarrow\; w \;-\; \eta\,\frac{dL}{dw}", font_size=44)
        rule.to_corner(UR, buff=0.55)

        def gradient():
            return 2 * float(np.sum(X_N * (w_tr.get_value() * X_N + B_FIT - Y_N)))

        grad_lab = MathTex(r"\frac{dL}{dw} =", font_size=34, color=C_BAD)
        grad_num = DecimalNumber(gradient(), num_decimal_places=1, font_size=34,
                                 color=C_BAD, include_sign=True)
        grad_grp = VGroup(grad_lab, grad_num).arrange(RIGHT, buff=0.12)
        grad_grp.next_to(rule, DOWN, buff=0.42)

        self.play(Write(rule), run_time=1.2)
        self.play(FadeIn(grad_grp, shift=DOWN * 0.1), run_time=0.8)
        grad_num.add_updater(lambda m: m.set_value(gradient()))
        self.say("নিয়মটির নাম gradient descent — ঢালের উল্টো দিকে ছোট ছোট ধাপ", hold=1.1)

        # ---------------- actually descend ----------------
        eta = 0.02
        for _ in range(7):
            grad = 2 * float(np.sum(X_N * (w_tr.get_value() * X_N + B_FIT - Y_N)))
            new_w = float(np.clip(w_tr.get_value() - eta * grad, w_lo + 0.08, w_hi - 0.08))
            self.play(w_tr.animate.set_value(new_w), run_time=0.85, rate_func=smooth)
            self.wait(0.06)

        self.say("প্রতিটি ধাপে রেখাটি সেরা অবস্থানের দিকে এগিয়ে যাচ্ছে", hold=0.9)
        self.play(w_tr.animate.set_value(W_FIT), run_time=1.4, rate_func=smooth)
        self.play(Flash(axL.c2p(W_FIT, sse(W_FIT, B_FIT)), color=C_FIT,
                        line_length=0.16, num_lines=14, flash_radius=0.28), run_time=1.1)
        self.say(f"শেষে w ≈ {W_FIT:.2f},  b ≈ {B_FIT:.2f} — এটাই সবচেয়ে ভালো রেখা",
                 color=C_FIT, hold=1.6)

        self.drop_caption()
        self.fade_all(run_time=1.0)


# ==========================================================================
# SCENE 6 — the line is a neuron
# ==========================================================================
class S06_Neuron(NarratedScene):
    def construct(self):
        # ---- the familiar equation ------------------------------------------
        eq = MathTex(r"\hat{y}", "=", "w", r"\cdot", "x", "+", "b", font_size=52)
        eq[0].set_color(C_FIT)
        eq[2].set_color(C_DATA)
        eq[4].set_color(C_LINE)
        eq[6].set_color(C_LINE)
        eq.move_to(UP * 2.95)
        self.play(Write(eq), run_time=1.4)
        self.say("একই সমীকরণটিকে এবার একটু অন্যভাবে দেখি", hold=0.8)

        # ---- the same things, as a diagram ----------------------------------
        x_node = node(MathTex("x", font_size=34), radius=0.42, color=C_LINE)
        s_node = node(MathTex(r"\Sigma", font_size=34), radius=0.50, color=C_NEURON)
        out_node = node(MathTex(r"\hat{y}", font_size=34), radius=0.42, color=C_FIT)
        VGroup(x_node, s_node, out_node).arrange(RIGHT, buff=2.1).move_to(UP * 0.80)

        e1 = connect(x_node, s_node, 0.42, 0.50)
        e2 = connect(s_node, out_node, 0.50, 0.42)
        w_lab = MathTex("w", font_size=30, color=C_DATA).move_to(mid(x_node, s_node))
        b_lab = MathTex("+b", font_size=30, color=C_DATA).next_to(s_node, DOWN, buff=0.24)

        self.play(
            TransformFromCopy(eq[4], x_node[1]),
            TransformFromCopy(eq[2], w_lab),
            TransformFromCopy(eq[6], b_lab),
            TransformFromCopy(eq[0], out_node[1]),
            run_time=1.6,
        )
        self.play(Create(x_node[0]), Create(s_node[0]), Create(out_node[0]),
                  Create(e1), Create(e2), FadeIn(s_node[1]), run_time=1.4)
        self.wait(0.4)

        self.say("বাঁ দিকের x হলো ইনপুট, তীরের উপরের w হলো ওজন (weight)", hold=1.0)
        self.say("ভেতরের Σ চিহ্নটি সব ইনপুট যোগ করে, আর b হলো যোগ হওয়া পক্ষপাত (bias)", hold=1.1)
        self.say("ডান দিকের সংখ্যাটি উত্তর — অর্থাৎ ভবিষ্যদ্বাণী", hold=1.0)

        # ---- many inputs -----------------------------------------------------
        self.say("ইনপুট যদি একটি না হয়ে অনেকগুলো হয়?", hold=0.7)

        xs = VGroup(*[node(MathTex(f"x_{i}", font_size=28), radius=0.31, color=C_LINE)
                      for i in (1, 2, 3)])
        xs.arrange(DOWN, buff=0.52).next_to(s_node, LEFT, buff=2.45)
        ws = VGroup(*[MathTex(f"w_{i}", font_size=26, color=C_DATA) for i in (1, 2, 3)])
        dots3 = MathTex(r"\vdots", font_size=30, color=C_DIM).next_to(xs, DOWN, buff=0.12)

        # the original input x becomes x1, and two more appear below it
        self.play(FadeOut(e1), FadeOut(w_lab),
                  Transform(x_node, xs[0]),
                  FadeIn(xs[1]), FadeIn(xs[2]), FadeIn(dots3), run_time=1.4)

        edges = VGroup()
        for xi, wi in zip(xs, ws):
            edges.add(connect(xi, s_node, 0.31, 0.50, width=1.8))
            wi.move_to(mid(xi, s_node))
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.15),
                  LaggedStart(*[FadeIn(w) for w in ws], lag_ratio=0.15), run_time=1.4)

        formula = MathTex(r"z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b", font_size=42)
        formula.move_to(DOWN * 1.45)
        self.play(Write(formula), run_time=1.3)
        self.say("তাহলে হিসাব — সব ইনপুট গুণ নিজের ওজন, সব যোগ, শেষে যোগ b", hold=1.2)

        # ---- activation ------------------------------------------------------
        self.say("শেষে এই যোগফলটি একটি ফিল্টারের ভেতর দিয়ে যায়", hold=0.5)

        sig = node(MathTex(r"\sigma", font_size=36), radius=0.46, color=C_DATA)
        sig.next_to(s_node, RIGHT, buff=1.25)
        e3 = connect(s_node, sig, 0.50, 0.46)
        e4 = connect(sig, out_node, 0.46, 0.42)

        out_node.target = out_node.generate_target()
        out_node.target.next_to(sig, RIGHT, buff=1.05)
        e4_target = Line(sig.get_center() + RIGHT * 0.46,
                         out_node.target.get_center() - RIGHT * 0.42,
                         color=C_EDGE, stroke_width=2.0)

        self.play(FadeOut(e2), Create(e3), FadeIn(sig), MoveToTarget(out_node), run_time=1.1)
        e4 = Line(sig.get_center() + RIGHT * 0.46,
                  out_node.get_center() - RIGHT * 0.42, color=C_EDGE, stroke_width=2.0)
        self.play(Create(e4), run_time=0.7)

        act = MathTex(r"a = \sigma(z)", font_size=42, color=C_DATA).move_to(DOWN * 2.15)
        self.play(Write(act), run_time=1.0)
        self.say("এই ফিল্টারটির নাম activation function", hold=1.0)
        self.say("সিগমা যদি সরল পরিচয় (identity) হয়, তবে এটি আবার সেই লিনিয়ার রিগ্রেশনই", hold=1.2)

        self.drop_caption()
        badge = bn("একটি লিনিয়ার রিগ্রেশন = একটি নিউরন", size=34, color=C_NEURON)
        badge.move_to(DOWN * 2.95)
        box = SurroundingRectangle(badge, color=C_NEURON, buff=0.24,
                                   stroke_width=2, corner_radius=0.12)
        self.play(FadeIn(badge, shift=DOWN * 0.15), Create(box), run_time=1.2)
        self.wait(2.2)

        self.fade_all(run_time=1.0)


# ==========================================================================
# SCENE 7 — from one neuron to a network
# ==========================================================================
class S07_Network(NarratedScene):
    def construct(self):
        R = 0.32
        col_x = [-4.70, -1.55, 1.60, 4.70]
        sizes = [4, 5, 5, 3]
        center_y = UP * 0.40

        layers = []
        for s, cx in zip(sizes, col_x):
            col = VGroup(*[node(None, radius=R) for _ in range(s)])
            col.arrange(DOWN, buff=0.30).move_to(RIGHT * cx + center_y)
            layers.append(col)

        # --- one neuron → one layer ------------------------------------------
        one = node(None, radius=R).move_to(ORIGIN)
        self.play(GrowFromCenter(one), run_time=0.8)
        self.say("একটি নিউরন মানে একটি রিগ্রেশন", hold=0.7)

        self.play(
            Transform(one, layers[0][1]),
            LaggedStart(*[GrowFromCenter(n) for i, n in enumerate(layers[0]) if i != 1],
                        lag_ratio=0.2),
            run_time=1.4,
        )
        self.say("পাশাপাশি অনেকগুলো নিউরন বসালে হয় একটি লেয়ার", hold=1.0)

        # --- the rest of the network -----------------------------------------
        self.play(
            LaggedStart(*[GrowFromCenter(n) for col in layers[1:] for n in col],
                        lag_ratio=0.05),
            run_time=1.6,
        )
        edges = VGroup()
        for a, b in zip(layers[:-1], layers[1:]):
            for na in a:
                for nb in b:
                    edges.add(connect(na, nb, R, R, width=1.0, opacity=0.32))
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.01), run_time=2.8)
        self.say("আর স্তরে স্তরে সাজালে হয় একটি নিউরাল নেটওয়ার্ক", hold=1.2)

        tags = VGroup(
            bn("ইনপুট", size=24, color=C_LINE),
            bn("লুকানো স্তর", size=24, color=C_NEURON),
            bn("লুকানো স্তর", size=24, color=C_NEURON),
            bn("আউটপুট", size=24, color=C_FIT),
        )
        for t, cx in zip(tags, col_x):
            t.move_to(RIGHT * cx + DOWN * 2.55)
        self.play(FadeIn(tags, shift=UP * 0.1), run_time=1.0)

        wtag = MathTex("W", font_size=32, color=C_DATA).move_to(UP * 2.60 + RIGHT * 0.05)
        self.play(FadeIn(wtag), run_time=0.6)
        self.say("প্রতিটি তীরের গায়ে একটি করে ওজন — ঠিক আগের সেই w-এর মতোই", hold=1.2)

        # --- the output layer is plain linear regression ----------------------
        hl = VGroup(*[SurroundingRectangle(n[0], color=C_FIT, buff=0.07,
                                           stroke_width=2.5, corner_radius=0.16)
                      for n in layers[-1]])
        self.play(LaggedStart(*[Create(h) for h in hl], lag_ratio=0.15), run_time=1.4)
        self.say("শেষ স্তরটি ঠিক সেই একই কাজ করে — y-hat = W x যোগ b", color=C_FIT, hold=1.2)

        loss = MathTex(r"L=\tfrac{1}{n}\sum (y-\hat{y})^2", font_size=36, color=C_BAD)
        loss.to_corner(UR, buff=0.60).shift(DOWN * 0.10)
        self.play(Write(loss), run_time=1.0)
        self.say("আর যে loss আমরা আগে বানিয়েছি, সেটাই আজও ব্যবহৃত হয়", hold=1.2)

        self.say("শুধু একটি পার্থক্য — এখন প্রতি লেয়ারের মাঝে একটি বাঁকা ফিল্টার বসে", hold=1.3)
        self.play(*[Indicate(n[0], scale_factor=1.3, color=C_DATA)
                    for col in layers[1:-1] for n in col], run_time=2.2)
        self.say("এই বাঁকানোই নেটওয়ার্ককে সরল রেখার চেয়ে অনেক শক্তিশালী করে", hold=1.8)

        self.drop_caption()
        self.fade_all(run_time=1.0)


# ==========================================================================
# SCENE 8 — where that simple line ended up
# ==========================================================================
class S08_Modern(NarratedScene):
    def construct(self):
        self.say("আজকের আধুনিক নেটওয়ার্কে ঠিক এই জিনিসটাই বারবার ঘুরে ফিরে আসে", hold=1.0)

        def box(text, color=C_LINE, width=2.3, height=0.85, tsize=26):
            r = RoundedRectangle(corner_radius=0.12, width=width, height=height,
                                 color=color, stroke_width=2.2)
            t = Text(text, font_size=tsize, color=color)
            if t.width > width - 0.24:
                t.scale_to_fit_width(width - 0.24)
            t.move_to(r)
            return VGroup(r, t)

        chain = VGroup(box("Linear", C_LINE), box("ReLU", C_DATA),
                       box("Linear", C_LINE), box("Softmax", C_FIT))
        chain.arrange(RIGHT, buff=0.60).move_to(UP * 2.55)
        arrows = VGroup(*[
            Arrow(a.get_right(), b.get_left(), buff=0.10, color=C_EDGE,
                  stroke_width=2.2, max_tip_length_to_length_ratio=0.30)
            for a, b in zip(chain[:-1], chain[1:])
        ])
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.2) for b in chain], lag_ratio=0.15),
                  run_time=1.6)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), run_time=1.2)

        code = Code(
            code_string="layer = nn.Linear(3, 1)\ny_hat = layer(x)   # y_hat = Wx + b",
            language="python",
            formatter_style="monokai",
            background="window",
            add_line_numbers=False,
            paragraph_config=dict(font_size=28, font="monospace", line_spacing=0.9),
        )
        if code.width > 9.2:
            code.scale_to_fit_width(9.2)
        code.move_to(UP * 0.70)
        self.play(FadeIn(code, shift=UP * 0.15), run_time=1.2)
        self.say("nn.Linear — এই একটি লাইনই ঠিক y-hat = W x যোগ b", hold=1.3)

        note = VGroup(
            bn("• ব্যাকপ্রপাগেশন = সেই একই gradient descent + চেইন রুল", size=28, color=C_DIM),
            bn("• Attention-ও লিনিয়ার লেয়ার আর softmax দিয়েই তৈরি", size=28, color=C_DIM),
            bn("• প্রতি লেয়ারে লাখ লাখ ওজন — সবই ছোট ছোট w আর b", size=28, color=C_DIM),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        note.next_to(code, DOWN, buff=0.55)
        if note.width > 12.0:
            note.scale_to_fit_width(12.0)
        self.play(LaggedStart(*[FadeIn(n, shift=UP * 0.1) for n in note], lag_ratio=0.3),
                  run_time=1.8)
        self.wait(1.8)

        # --- bookend: back to where we started --------------------------------
        self.play(FadeOut(VGroup(chain, arrows, code, note)), run_time=1.0)

        ax = Axes(x_range=[-0.4, 3.9, 1], y_range=[0, 7.6, 1],
                  x_length=6.0, y_length=2.7, axis_config=dict(stroke_opacity=0))
        ax.move_to(UP * 0.75)
        line = ax.plot(lambda x: TRUE_W * x + TRUE_B, x_range=[-0.3, 3.3, 0.01],
                       color=C_LINE, stroke_width=4)
        dots = VGroup(*[Dot(ax.c2p(x, y), radius=0.075, color=C_DATA) for x, y in zip(X, Y)])
        self.play(Create(line), run_time=1.4)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2), run_time=1.2)
        self.play(LaggedStart(*[Indicate(d, scale_factor=1.6, color=WHITE) for d in dots],
                              lag_ratio=0.2), run_time=1.6)

        final = bn("সবকিছুর শুরুতে ছিল একটি সরল রেখা", size=42, color=C_LINE)
        final.move_to(DOWN * 1.75)
        self.play(FadeIn(final, shift=UP * 0.2), run_time=1.4)
        self.say("প্রতিটি আধুনিক নিউরাল নেটওয়ার্কের শুরুতে ছিল একটি সরল রেখা", hold=2.2)

        self.drop_caption()
        self.play(FadeOut(VGroup(line, dots, final), shift=DOWN * 0.2), run_time=1.2)
        thanks = bn("ধন্যবাদ", size=48, color=C_DIM)
        self.play(FadeIn(thanks, scale=1.15), run_time=1.2)
        self.wait(2.0)
