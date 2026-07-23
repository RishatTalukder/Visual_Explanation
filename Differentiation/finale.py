from manim import *

class DerivativeIntro(Scene):
    def construct(self):
        self.create_graph()
        self.create_points()
        self.create_slope()

    # ----------------------------------------------------
    # Graph
    # ----------------------------------------------------
    def create_graph(self):

        self.axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=5,
            y_length=4,
            axis_config={
                "include_numbers": False,
                "include_ticks": True,
            },
        )

        # This should match the FINAL shifted position
        self.axes.shift(RIGHT * 2.5 + UP * 0.5)

        self.graph = self.axes.plot(
            lambda x: 0.05 * x**2 + 4,
            color=BLUE,
        )

        self.x_label = MathTex("x").next_to(
            self.axes.x_axis.get_end(),
            RIGHT,
            buff=0.2,
        )

        self.y_label = MathTex("y").next_to(
            self.axes.y_axis.get_end(),
            UP,
            buff=0.2,
        )

        self.add(
            self.axes,
            self.graph,
            self.x_label,
            self.y_label,
        )

    # ----------------------------------------------------
    # Two fixed points
    # ----------------------------------------------------
    def create_points(self):

        x1 = 3
        x2 = 8

        y1 = self.function(x1)
        y2 = self.function(x2)

        # x1
        self.x1_dot = Dot(
            self.axes.c2p(x1, 0),
            radius=0.08,
            color=BLUE,
        )

        self.y1_dot = Dot(
            self.axes.c2p(0, y1),
            radius=0.08,
            color=GREEN,
        )

        self.graph_dot1 = Dot(
            self.axes.c2p(x1, y1),
            radius=0.09,
            color=YELLOW,
        )

        # x2
        self.x2_dot = Dot(
            self.axes.c2p(x2, 0),
            radius=0.08,
            color=BLUE_D,
        )

        self.y2_dot = Dot(
            self.axes.c2p(0, y2),
            radius=0.08,
            color=GREEN_D,
        )

        self.graph_dot2 = Dot(
            self.axes.c2p(x2, y2),
            radius=0.09,
            color=YELLOW_D,
        )

        self.v1 = DashedLine(
            self.x1_dot.get_center(),
            self.graph_dot1.get_center(),
            color=GRAY,
        )

        self.h1 = DashedLine(
            self.graph_dot1.get_center(),
            self.y1_dot.get_center(),
            color=GRAY,
        )

        self.v2 = DashedLine(
            self.x2_dot.get_center(),
            self.graph_dot2.get_center(),
            color=GRAY,
        )

        self.h2 = DashedLine(
            self.graph_dot2.get_center(),
            self.y2_dot.get_center(),
            color=GRAY,
        )

        self.x1_label = MathTex("x_1").scale(0.8).next_to(
            self.x1_dot,
            DOWN,
            buff=0.15,
        )

        self.y1_label = MathTex("y_1").scale(0.8).next_to(
            self.y1_dot,
            LEFT,
            buff=0.15,
        )

        self.x2_label = MathTex("x_2").scale(0.8).next_to(
            self.x2_dot,
            DOWN,
            buff=0.15,
        )

        self.y2_label = MathTex("y_2").scale(0.8).next_to(
            self.y2_dot,
            LEFT,
            buff=0.15,
        )

        self.add(
            self.v1,
            self.h1,
            self.v2,
            self.h2,
            self.x1_dot,
            self.y1_dot,
            self.graph_dot1,
            self.x2_dot,
            self.y2_dot,
            self.graph_dot2,
            self.x1_label,
            self.y1_label,
            self.x2_label,
            self.y2_label,
        )

    # ----------------------------------------------------
    # Secant line + slope
    # ----------------------------------------------------
    def create_slope(self):

        self.secant = Line(
            self.axes.c2p(2, self.function(2)),
            self.axes.c2p(9, self.function(9)),
            color=RED,
        )

        self.add(self.secant)

        self.m = MathTex("m").scale(0.8)
        self.m.next_to(self.secant, UP)

        self.add(self.m)

    # ----------------------------------------------------

    def function(self, x):
        return 0.05 * x**2 + 4