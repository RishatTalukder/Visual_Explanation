from manim import *

class Graph_Version(Scene):
    def construct(self):
        self.lines()
        self.show_graph()
        self.plotting()
        self.animate_position()
        self.animate_position_x2()
        self.rate_of_change()

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

        self.x_label = MathTex("x")
        self.y_label = MathTex("y")

        self.x_label.next_to(self.axes.x_axis.get_end(), RIGHT, buff=0.2)
        self.y_label.next_to(self.axes.y_axis.get_end(), UP, buff=0.2)

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
            Write(self.y_label),
            Write(self.x_label),
        )

        self.wait()

    def plotting(self):
        self.graph = self.axes.plot(
            lambda x:.05*x**2 + 4,
            color=BLUE,
        )

        self.play(Create(self.graph), run_time=3)

    def animate_position(self):
        tracker = ValueTracker(3)

        x_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(tracker.get_value(), 0),
                radius=0.08,
                color=BLUE
            )
        )

        y_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(0, 0.05*tracker.get_value()**2 + 4),
                radius=0.08,
                color=GREEN
            )
        )

        self.play(
            FadeIn(x_dot)
        )
        self.wait()

        graph_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(
                    tracker.get_value(),
                    0.05*tracker.get_value()**2 + 4,
                ),
                color=YELLOW,
                radius=0.09,
            )
        )

        vertical_line_x = always_redraw(
            lambda: DashedLine(
                x_dot.get_center(),
                graph_dot.get_center(),
                color=GRAY,
            )
        )

        vertical_line_y = always_redraw(
            lambda: DashedLine(
                graph_dot.get_center(),
                y_dot.get_center(),
                color=GRAY,
            )
        )

        self.play(Create(vertical_line_x))
        self.play(FadeIn(graph_dot))
        self.wait()
        # self.wait()

        self.play(Create(vertical_line_y))
        self.play(
            FadeIn(y_dot)
        )
        self.wait()
        

        trail = TracedPath(
            graph_dot.get_center,
            stroke_color=YELLOW,
            stroke_width=4,
            dissipating_time=0.5,
        )

        self.add(trail)


        self.play(
            tracker.animate.set_value(8),
            run_time=1.5,
            rate_func=smooth,
        )

        # self.wait()

        self.play(
            tracker.animate.set_value(2),
            run_time=1.5,
            rate_func=smooth,
        )

        # self.wait()

        self.play(
            tracker.animate.set_value(3),
            run_time=2,
            rate_func=smooth,
        )

        self.wait()

        self.remove(trail)


        x1_label = always_redraw(
            lambda: MathTex("x_1")
            .scale(0.8)
            .next_to(
                x_dot,
                DOWN,
                buff=0.15
            )
        )

        y1_label = always_redraw(
            lambda: MathTex("y_1")
            .scale(0.8)
            .next_to(
                y_dot,
                LEFT,
                buff=0.15
            )
        )

        self.play(Write(x1_label))
        self.play(Write(y1_label))
        self.wait()

        self.x1_group = VGroup(
            x_dot,
            y_dot,
            graph_dot,
            vertical_line_x,
            vertical_line_y,
            x1_label,
            y1_label,
        )

    def animate_position_x2(self):
        tracker = ValueTracker(3)

        x2_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(tracker.get_value(), 0),
                radius=0.08,
                color=BLUE_D
            )
        )

        y2_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(0, 0.05*tracker.get_value()**2 + 4),
                radius=0.08,
                color=GREEN_D
            )
        )

        graph_dot2 = always_redraw(
            lambda: Dot(
                self.axes.c2p(
                    tracker.get_value(),
                    0.05*tracker.get_value()**2 + 4,
                ),
                color=YELLOW_D,
                radius=0.09,
            )
        )

        vertical_line_x = always_redraw(
            lambda: DashedLine(
                x2_dot.get_center(),
                graph_dot2.get_center(),
                color=GRAY,
            )
        )

        vertical_line_y = always_redraw(
            lambda: DashedLine(
                graph_dot2.get_center(),
                y2_dot.get_center(),
                color=GRAY,
            )
        )

        self.add(
            x2_dot,
            y2_dot,
            graph_dot2,
            vertical_line_x,
            vertical_line_y
        )



        self.play(
            tracker.animate.set_value(8),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait()


        x2_label = always_redraw(
            lambda: MathTex("x_2")
            .scale(0.8)
            .next_to(
                x2_dot,
                DOWN,
                buff=0.15
            )
        )

        y2_label = always_redraw(
            lambda: MathTex("y_2")
            .scale(0.8)
            .next_to(
                y2_dot,
                LEFT,
                buff=0.15
            )
        )

        self.play(Write(x2_label))
        self.play(Write(y2_label))
        self.wait()

        self.x2_group = VGroup(
            x2_dot,
            y2_dot,
            graph_dot2,
            vertical_line_x,
            vertical_line_y,
            x2_label,
            y2_label,
        )

    
    def function(self, x):
        return .05*x**2 + 4


    def rate_of_change(self):

        graph_group = VGroup(
            self.axes,
            self.graph,
            self.x1_group,
            self.x2_group,
        )

        self.play(  
            graph_group.animate.shift(RIGHT * 2),
            self.x_label.animate.shift(RIGHT * 2),
            self.y_label.animate.shift(RIGHT * 2),
            run_time=2,
        )

        self.wait()

        # Δx brace
        x_brace = always_redraw(
            lambda: BraceBetweenPoints(
                self.axes.c2p(3, 0),      # x1
                self.axes.c2p(8, 0),      # x2
                direction=DOWN,
            ).shift(DOWN * 0.40)
        )

        # Δy brace
        y_brace = always_redraw(
            lambda: BraceBetweenPoints(
                self.axes.c2p(
                    0,
                    self.function(3),
                ),
                self.axes.c2p(
                    0,
                    self.function(8),
                ),
                direction=LEFT,
            ).shift(LEFT * 0.40)
        )

        delta_x = always_redraw(
            lambda: MathTex(r"\Delta x")
            .scale(0.8)
            .next_to(x_brace, DOWN, buff=0.15)
        )

        delta_y = always_redraw(
            lambda: MathTex(r"\Delta y")
            .scale(0.8)
            .next_to(y_brace, LEFT, buff=0.15)
        )

        self.play(
            GrowFromEdge(x_brace, edge=LEFT),
            GrowFromEdge(y_brace, edge=DOWN),
        )

        self.play(
            Write(delta_x),
            Write(delta_y),
        )

        self.wait()

        delta_y_tex = MathTex(r"\Delta y").to_edge(LEFT)
        delta_x_tex = MathTex(r"\Delta x").next_to(delta_y_tex, DOWN)

        frac = MathTex(r"\frac{\Delta y}{\Delta x}")

        equals = MathTex("=")

        difference = MathTex(
            r"\frac{y_2-y_1}{x_2-x_1}"
        )

        equation = VGroup(
            frac,
            equals,
            difference,
        ).arrange(RIGHT)

        equation.to_edge(LEFT)
        # equation.shift(UP * 0.5)

        self.play(
            ReplacementTransform(delta_y.copy(), delta_y_tex),
            ReplacementTransform(delta_x.copy(), delta_x_tex),
        )
        self.wait()

        self.play(
            ReplacementTransform(
                VGroup(delta_y_tex, delta_x_tex),
                frac,
            ),
            Write(equals),
            run_time=1.5,
        )

        self.play(
            Write(difference),
            run_time=2,
        )

        self.wait()

        slope_title = Text("Slope", weight=BOLD).scale(0.6)
        slope_title.to_edge(LEFT)
        slope_title.shift(UP * 2)

        self.play(Write(slope_title))


        school_formula = MathTex(
            "m",
            "=",
            r"\frac{y_2-y_1}{x_2-x_1}"
        )

        school_formula.next_to(
            slope_title,
            DOWN,
            buff=0.5,
            aligned_edge=LEFT
        )

        self.play(
            TransformMatchingTex(
                equation,
                school_formula
            ),
            run_time=2,
        )

        self.wait()

        TransformMatchingTex(
            equation,
            school_formula
        )

        

        graph_group = VGroup(
            self.axes,
            self.graph,
            self.x1_group,
            self.x2_group,
            self.x_label,
            self.y_label,
        )

        self.play(
            graph_group.animate.shift(LEFT * 0.8),

            FadeOut(
                x_brace,
                y_brace,
                delta_x,
                delta_y,
            ),

            run_time=2,
        )

        p1 = self.axes.c2p(3, self.function(3))
        p2 = self.axes.c2p(8, self.function(8))

        secant = Line(
            p1,
            p2,
            color=RED,
        )

        # Make it extend beyond the points
        secant.scale(2.8, about_point=secant.get_center())

        self.play(
            Create(secant),
            run_time=1.5
        )

        m_copy = school_formula[0].copy()

        m_target = MathTex("m").scale(1)

        m_target.move_to(
            secant.get_center()
        )

        m_target.shift(UP * 0.45)

        self.play(
            ReplacementTransform(
                m_copy,
                m_target,
            ),
            run_time=1.5,
        )

        slope_text = Text(
            "Slope of the Line",
            font_size=28,
        )

        slope_text.next_to(
            m_target,
            UP,
            buff=0.2,
        )

        self.play(FadeIn(slope_text))

        self.wait()

        # function = MathTex(
        #     "y", "=",
        #     "f", "(", "x", ")"
        # ).scale(1.3)

        # # function.to_edge(RIGHT)

        # self.play(
        #     ReplacementTransform(
        #         graph_group,
        #         function
        #     ),
        #     FadeOut(self.x_label),
        #     FadeOut(self.y_label),
        #     FadeOut(x_brace),
        #     FadeOut(y_brace),
        #     FadeOut(delta_x),
        #     FadeOut(delta_y),
        #     run_time=2
        # )

        # self.wait()