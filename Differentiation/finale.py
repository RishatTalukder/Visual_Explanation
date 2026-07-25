from manim import *

class Finale(Scene):
    def construct(self):
        self.state()
        self.new_equation_animation()
        self.transform_h()
        self.merge_all()
        self.draw_the_graph()
 
    def state(self):
        
        self.final_formula = MathTex(
            r"\frac{\Delta y}{\Delta x}",
            '=',
            r"\lim_{h \to 0}",
            r"\frac{y_2-y_1}{h}"
        )

        self.slope_title = Text("Slope", weight=BOLD).scale(0.6)
        self.slope_title.to_edge(LEFT)
        self.slope_title.shift(UP * 2)

        self.final_formula.next_to(
            self.slope_title,
            DOWN,
            buff=0.5,
            aligned_edge=LEFT
        )

        self.h = MathTex(
            "h",
            "=",
            "x_2-x_1"
        )
        
        self.h.next_to(
            self.final_formula,
            DOWN,
            buff=0.5,
            aligned_edge=LEFT
        )

        self.function = MathTex(
            "y", 
            "=",
            "f(x)"
        ).scale(1.5)

        self.function.shift(RIGHT * 2)

        self.add(
            self.function,
            self.slope_title,
            self.final_formula,
            self.h
        )

        self.wait()


    def new_equation_animation(self):
        self.new_equation = MathTex(
            r"\frac{\Delta y}{\Delta x}",
            "=",
            r"\lim_{h\to0}",
            r"\frac{f(x_2)-f(x_1)}{h}"
        )

        self.new_equation.move_to(self.function)


        self.play(
            Transform(
                self.final_formula,
                self.new_equation,
                transform_mismatches=True,
            ),
            FadeOut(self.function),
            FadeOut(self.slope_title),
            run_time=2,
        )

        self.wait()

    def transform_h(self):
        self.y2 = MathTex(
            "x_2",
            "=",
            "x_1+h"
        )

        self.y2.move_to(self.h)

        self.play(
            Transform(
                self.h,
                self.y2,
                transform_mismatches=True,
            ),
            run_time=2,
        )

        self.wait()

    def merge_all(self):
        last_formula = MathTex(
            r"\frac{\Delta y}{\Delta x}",
            '=',
            r"\lim_{h \to 0}",
            r"\frac{f(x_1+h)-f(x_1)}{h}"
        )

        # Morph both existing objects into looking like last_formula
        self.play(
            Transform(self.final_formula, last_formula),
            Transform(self.h, last_formula),
            run_time=2
        )
        self.wait()

        # Fade out self.h safely so it doesn't leave ghosts behind
        self.play(FadeOut(self.h))

        # Define the generalized formula clearly
        generalized_formula = MathTex(
            r"\frac{dy}{dx}",
            '=',
            r"\lim_{h \to 0}",
            r"\frac{f(x+h)-f(x)}{h}"
        )

        # Transform final_formula into it, and update the variable pointer
        self.play(
            ReplacementTransform(self.final_formula, generalized_formula),
            run_time=2
        )
        
        # CRITICAL FIX: Reassign the pointer so 'self.final_formula' 
        # now controls the actual object visible on the screen
        self.final_formula = generalized_formula
        self.wait()

    def draw_the_graph(self):
        self.axes = Axes(
            x_range=[0,10],
            y_range=[0,10],
            x_length=5,
            y_length=4,
        )
        self.axes.to_edge(RIGHT)

        graph = self.axes.plot(
            lambda x: 0.05*x**2 + 4,
            color=BLUE
        )

        # Move formula and show axes
        self.play(
            Create(self.axes),
            self.final_formula.animate.to_edge(LEFT),
            run_time=2
        )

        self.play(Create(graph))
        self.wait()

        # Initialize tracking value
                # Initialize tracking value
        tracker = ValueTracker(3)

        # Dynamic graph dot
        dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(tracker.get_value(), self.f(tracker.get_value())),
                radius=0.08,
                color=GREEN
            )
        )
        self.graph_dot = dot

        # Dynamic projection dot on X-axis
        x_dot = always_redraw(
            lambda: Dot(
                self.axes.c2p(tracker.get_value(), 0),
                color=BLUE
            )
        )

        # Dynamic projection dashed line
        vertical = always_redraw(
            lambda: DashedLine(
                x_dot.get_center(),
                dot.get_center()
            )
        )

        # Dynamic X label
        x_label = always_redraw(
            lambda: MathTex("x")
                .scale(0.8)
                .next_to(x_dot, DOWN, buff=.15)
        )

        # MODERN MANIM FIX: Using the modern TangentLine class wrapped in always_redraw
        # Since x goes from 0 to 10, alpha = tracker_value / 10
        tangent_line = always_redraw(
            lambda: TangentLine(
                graph, 
                alpha=tracker.get_value() / 10, 
                length=4, 
                color=RED
            )
        )

        # Display everything together
        self.play(
            Create(x_dot),
            Create(dot),
            Create(vertical),
            Create(x_label),
            Create(tangent_line)
        )
        self.wait()

        # Smoothly animate the value trackers
        self.play(tracker.animate.set_value(7), run_time=3)
        self.play(tracker.animate.set_value(1), run_time=3)
        self.play(tracker.animate.set_value(5), run_time=3)
        self.wait()



    def f(self,x):   
        return 0.05*x**2 + 4