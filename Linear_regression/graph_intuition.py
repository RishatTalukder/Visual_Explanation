from manim import *


class GraphIntuition(Scene):
    """
    Visual explanation of Linear Regression Graph Intuition.
    Introduces 2D coordinate axes, animates 5 sample data points,
    illustrates the trend, and introduces the concept of the best-fit line.
    """

    def construct(self):
        self.show_title()
        self.create_axes()
        self.animate_dots()
        self.show_trend_and_best_fit()

    def show_title(self):
        # ---------------- Title Section ----------------
        self.title = Text("Linear Regression", weight=BOLD, font_size=40)
        self.subtitle = Text("Graph Intuition & Data Points", font_size=26, color=BLUE_B)
        title_group = VGroup(self.title, self.subtitle).arrange(DOWN, buff=0.2)

        self.play(FadeIn(title_group, shift=UP * 0.3))
        self.wait(1.5)

        # Transition title to the top
        header = Text("Linear Regression: Graph Intuition", weight=BOLD, font_size=28)
        header.to_edge(UP, buff=0.4)

        self.play(
            ReplacementTransform(title_group, header),
            run_time=1.2,
        )
        self.header = header
        self.wait(0.5)

    def create_axes(self):
        # ---------------- Create Axes ----------------
        # Setting up axes for 5 data points in a 0-6 range
        self.axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 7, 1],
            x_length=7.5,
            y_length=5.0,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "color": GREY_B,
            },
            tips=True,
        ).shift(DOWN * 0.4)

        # Axis labels
        x_label = self.axes.get_x_axis_label(
            MathTex("x", font_size=30, color=BLUE),
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,
        )
        y_label = self.axes.get_y_axis_label(
            MathTex("y", font_size=30, color=GREEN),
            edge=UP,
            direction=UP,
            buff=0.3,
        )

        self.x_label = x_label
        self.y_label = y_label

        self.play(Create(self.axes), Write(x_label), Write(y_label), run_time=1.8)
        self.wait(0.8)

    def animate_dots(self):
        # ---------------- 5 Data Points ----------------
        # Sample coordinates (x, y) displaying a linear trend with slight scatter
        self.data_coords = [
            (1.0, 1.8),
            (2.0, 2.5),
            (3.0, 3.8),
            (4.0, 4.2),
            (5.0, 5.6),
        ]

        self.dots = VGroup()
        self.dot_labels = VGroup()
        self.projection_lines = VGroup()

        # Iterate through points and animate with projection lines
        for i, (x_val, y_val) in enumerate(self.data_coords):
            pt = self.axes.c2p(x_val, y_val)

            # Dot with glow ring
            dot = Dot(point=pt, radius=0.1, color=YELLOW)
            
            # Label (e.g. P1, P2... or coordinates (x, y))
            label = MathTex(
                f"({x_val:.0f}, {y_val:.1f})",
                font_size=20,
                color=YELLOW_B,
            ).next_to(dot, UR, buff=0.15)

            # Dashed projection lines to x and y axes
            x_proj = self.axes.c2p(x_val, 0)
            y_proj = self.axes.c2p(0, y_val)
            proj_x = DashedLine(x_proj, pt, stroke_width=2, color=BLUE_E, dash_length=0.08)
            proj_y = DashedLine(y_proj, pt, stroke_width=2, color=GREEN_E, dash_length=0.08)

            # Animate projection lines appearing, then dot popping up
            self.play(
                Create(proj_x),
                Create(proj_y),
                run_time=0.4,
            )
            self.play(
                GrowFromCenter(dot),
                FadeIn(label, shift=UP * 0.1),
                run_time=0.5,
            )

            # Subtle ripple/flash effect around the dot
            ring = Circle(radius=0.25, color=YELLOW, stroke_width=2).move_to(pt)
            self.play(
                ring.animate.scale(1.6).set_opacity(0),
                run_time=0.4,
            )
            self.remove(ring)

            self.dots.add(dot)
            self.dot_labels.add(label)
            self.projection_lines.add(VGroup(proj_x, proj_y))

        self.wait(1.0)

        # Fade out projection lines and labels to keep the graph uncluttered
        self.play(
            FadeOut(self.projection_lines),
            self.dot_labels.animate.set_opacity(0.7),
            run_time=1.0,
        )
        self.wait(1.0)

    def show_trend_and_best_fit(self):
        # ---------------- Best-fit Line Intuition ----------------
        # Linear model: y = mx + c (slope ~ 0.95, intercept ~ 0.8)
        slope = 0.95
        intercept = 0.8

        best_fit_line = self.axes.plot(
            lambda x: slope * x + intercept,
            x_range=[0.5, 5.5],
            color=RED,
            stroke_width=4,
        )

        line_equation = MathTex(
            r"\hat{y} = wx + b",
            font_size=28,
            color=RED,
        ).next_to(best_fit_line.get_end(), UP + RIGHT, buff=0.2)

        # Question / Idea
        question_text = Text(
            "Find the line that best fits these 5 points",
            font_size=22,
            color=LIGHT_GREY,
        ).to_edge(DOWN, buff=0.3)

        self.play(Write(question_text), run_time=1.2)
        self.wait(0.5)

        # Draw the best-fit line
        self.play(Create(best_fit_line), Write(line_equation), run_time=1.8)
        self.wait(1.0)

        # Residuals / Error lines (vertical distances from points to the line)
        residual_lines = VGroup()
        for x_val, y_val in self.data_coords:
            y_pred = slope * x_val + intercept
            p_actual = self.axes.c2p(x_val, y_val)
            p_pred = self.axes.c2p(x_val, y_pred)
            res_line = DashedLine(
                p_actual,
                p_pred,
                color=ORANGE,
                stroke_width=3,
                dash_length=0.06,
            )
            residual_lines.add(res_line)

        error_label = Text("Minimize distances (residuals)", font_size=20, color=ORANGE)
        error_label.next_to(question_text, UP, buff=0.2)

        self.play(
            Create(residual_lines),
            FadeIn(error_label),
            run_time=1.5,
        )
        self.wait(3.0)
