from manim import *

class Graph_Version(Scene):
    def construct(self):
        self.lines()
        self.show_graph()
        self.plotting()

    def lines(self):
        self.x_line = NumberLine(
            x_range=[-10, 10, 1],
            length=4,
            include_numbers=False,
        ).rotate(PI / 2)

        self.y_line = NumberLine(
            x_range=[-10, 10, 1],
            length=4,
            include_numbers=False,
        ).rotate(PI / 2)

        self.x_line.shift(RIGHT * 0.5)
        self.y_line.shift(RIGHT * 3)

        # Create axes and transform labels
        self.add(
            self.x_line,
            self.y_line,
        )

        self.wait()

    def show_graph(self):

        # Create the graph axes
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

        self.axes.shift(RIGHT * .5, UP * .5)

        x_label = MathTex("x")
        y_label = MathTex("y")

        x_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.2)

        # Animate the old lines into the new axes
        self.play(
            ReplacementTransform(
                self.x_line,
                self.axes.x_axis
            ),
            ReplacementTransform(
                self.y_line,
                self.axes.y_axis
            ),
            run_time=2,
        )

        # The axes object still contains both axes,
        # so add it back to the scene.
        # self.add(self.axes)
        self.play(
            Write(x_label),
            Write(y_label),
        )

        self.wait()

    def plotting(self):
        graph = self.axes.plot(
            lambda x:.05*x**2 + 4,
            color=BLUE,
        )

        self.play(Create(graph), run_time=3)