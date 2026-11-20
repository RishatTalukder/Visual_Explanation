
from manim import *
import numpy as np

# ==========================================
# IT VAYA — NEON LAB
# ==========================================

config.background_color = "#262335"

BG = "#262335"
PANEL = "#34294F"
WHITE = "#FDEBFF"

PINK = "#FF7EDB"
CYAN = "#36F9F6"
GREEN = "#72F1B8"
YELLOW = "#FDEB5D"
CORAL = "#F97E72"
LAVENDER = "#A99BCB"


class NeonLabDemo(Scene):
    def construct(self):

        # ----------------------------------
        # 1. INTRO
        # ----------------------------------

        title = Text(
            "LINEAR REGRESSION",
            font_size=42,
            weight=BOLD,
            color=PINK
        )

        subtitle = Text(
            "Finding patterns in data",
            font_size=23,
            color=WHITE
        )

        subtitle.next_to(title, DOWN, buff=0.25)

        self.play(
            FadeIn(title, shift=UP),
            run_time=1
        )
        self.play(FadeIn(subtitle), run_time=0.7)
        self.wait(1)

        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )

        # ----------------------------------
        # 2. CREATE THE GRAPH
        # ----------------------------------

        plane = NumberPlane(
            x_range=[0, 7, 1],
            y_range=[0, 8, 1],
            x_length=8,
            y_length=5,
            background_line_style={
                "stroke_color": LAVENDER,
                "stroke_opacity": 0.20,
                "stroke_width": 1
            },
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2,
                "include_ticks": False
            }
        )

        plane.move_to(DOWN * 0.3)

        x_label = Text(
            "Study Hours",
            font_size=22,
            color=CYAN
        )
        x_label.next_to(plane, DOWN, buff=0.35)

        y_label = Text(
            "Exam Score",
            font_size=22,
            color=CYAN
        )
        y_label.rotate(PI / 2)
        y_label.next_to(plane, LEFT, buff=0.35)

        self.play(Create(plane), run_time=1.5)
        self.play(
            FadeIn(x_label),
            FadeIn(y_label)
        )

        # ----------------------------------
        # 3. DATA POINTS
        # ----------------------------------

        data = [
            (0.8, 1.5),
            (1.5, 2.0),
            (2.0, 3.1),
            (2.8, 3.2),
            (3.5, 4.5),
            (4.0, 4.1),
            (4.8, 5.6),
            (5.5, 6.0),
            (6.2, 7.0),
        ]

        dots = VGroup()

        for x, y in data:
            dot = Dot(
                plane.c2p(x, y),
                radius=0.075,
                color=CYAN
            )

            # Subtle glow behind each data point
            glow = Dot(
                plane.c2p(x, y),
                radius=0.15,
                color=CYAN
            ).set_opacity(0.18)

            dots.add(glow, dot)

        self.play(
            LaggedStart(
                *[FadeIn(dot, scale=0.5) for dot in dots],
                lag_ratio=0.06
            ),
            run_time=2
        )

        self.wait(0.5)

        # ----------------------------------
        # 4. REGRESSION LINE
        # ----------------------------------

        regression = plane.plot(
            lambda x: 0.95 * x + 0.8,
            x_range=[0.3, 6.5],
            color=PINK,
            stroke_width=5
        )

        # Fake neon glow using layered strokes
        glow1 = regression.copy().set_stroke(
            PINK,
            width=18,
            opacity=0.12
        )

        glow2 = regression.copy().set_stroke(
            PINK,
            width=10,
            opacity=0.20
        )

        self.play(
            Create(glow1),
            Create(glow2),
            Create(regression),
            run_time=2
        )

        # ----------------------------------
        # 5. EQUATION
        # ----------------------------------

        equation = MathTex(
            r"y = mx + b",
            font_size=42,
            color=YELLOW
        )

        equation.to_corner(UR, buff=0.5)

        equation_bg = SurroundingRectangle(
            equation,
            color=PANEL,
            fill_color=PANEL,
            fill_opacity=0.95,
            buff=0.2,
            stroke_width=1.5
        )

        self.play(
            FadeIn(equation_bg),
            Write(equation)
        )

        # ----------------------------------
        # 6. FINAL ANNOTATION
        # ----------------------------------

        annotation = Text(
            "A line that captures the trend.",
            font_size=23,
            color=GREEN
        )

        annotation.to_edge(DOWN, buff=0.35)

        self.play(
            FadeIn(annotation, shift=UP)
        )

        self.wait(3)
