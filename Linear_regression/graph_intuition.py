from manim import *


class GraphIntuition(Scene):
    """
    Segment 2: Graph Intuition
    Seamlessly continues from where title.py ends.
    - Transitions title to the top edge
    - Constructs the 2D coordinate graph (axes)
    - Animates 5 sample data points on the graph
    """

    def construct(self): 
        self.setup_title()
        self.create_graph()
        self.animate_dots()

    def setup_title(self):
        # ---------------- Title ----------------
        # Pop in the title at the exact position rendered at the end of title.py
        self.title = Text("Linear Regression", weight=BOLD).to_edge(UP)
        self.add(self.title)
        self.wait(1)

    def create_graph(self):
        # ---------------- Create Graph / Axes ----------------
        self.axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 6, 1],
            x_length=7.5,
            y_length=4.8,
            axis_config={
                "include_numbers": True,
                "font_size": 22,
                "color": GREY_B,
            },
            tips=True,
        ).shift(DOWN * 0.3)

        # Labels for x and y axes
        self.x_label = self.axes.get_x_axis_label(
            MathTex("x", font_size=28, color=BLUE),
            edge=RIGHT,
            direction=RIGHT,
            buff=0.25,
        )
        self.y_label = self.axes.get_y_axis_label(
            MathTex("y", font_size=28, color=GREEN),
            edge=UP,
            direction=UP,
            buff=0.25,
        )

        self.play(
            Create(self.axes),
            Write(self.x_label),
            Write(self.y_label),
            run_time=1.5,
        )
        self.wait(1)

    def animate_dots(self):
        # ---------------- 5 Data Points ----------------
        # 5 points showing a clear linear relationship with slight real-world noise
        self.data_coords = [
            (1.0, 1.5),
            (2.0, 2.8),
            (3.0, 3.2),
            (4.0, 4.5),
            (5.0, 5.2),
        ]

        self.dots = VGroup()
        self.dot_labels = VGroup()
        self.guidelines = VGroup()

        for x_val, y_val in self.data_coords:
            pt = self.axes.c2p(x_val, y_val)
            dot = Dot(point=pt, radius=0.09, color=YELLOW)

            # Coordinate label: (x, y)
            label = MathTex(
                f"({x_val:.0f}, {y_val:.1f})",
                font_size=20,
                color=YELLOW_B,
            ).next_to(dot, UR, buff=0.12)

            # Dashed guidelines projecting from axes to the point
            x_proj = self.axes.c2p(x_val, 0)
            y_proj = self.axes.c2p(0, y_val)
            x_guide = DashedLine(x_proj, pt, stroke_width=1.5, color=BLUE_E, dash_length=0.08)
            y_guide = DashedLine(y_proj, pt, stroke_width=1.5, color=GREEN_E, dash_length=0.08)

            # Animate guidelines then dot appearance
            self.play(
                Create(x_guide),
                Create(y_guide),
                run_time=0.4,
            )
            self.play(
                GrowFromCenter(dot),
                FadeIn(label, shift=UP * 0.1),
                run_time=0.4,
            )

            self.dots.add(dot)
            self.dot_labels.add(label)
            self.guidelines.add(VGroup(x_guide, y_guide))

        self.wait(1)

        # Clean up guidelines and soften labels so the focus remains on the 5 dots
        self.play(
            FadeOut(self.guidelines),
            self.dot_labels.animate.set_opacity(0.7),
            run_time=1.0,
        )

        # Final hold for the segment ending
        self.wait(3)
