from manim import *

class TitleScene(Scene):
    def construct(self):
        self.show_title()
        self.definition()
        self.transition()


    def show_title(self):
        # ---------------- Title ----------------
        self.title = Text("Differentiation", weight=BOLD)

        self.play(FadeIn(self.title))
        self.wait(3)

        self.play(self.title.animate.to_edge(UP))
        self.wait(1)

    
    def definition(self):
        
        # ---------------- Definition ----------------
        self.definition = Tex(
            r"\textbf{Definition: }",
            r"Differentiation is the process of finding the ",
            r"\textit{instantaneous rate of change} ",
            r"of a function with respect to one of its variables.",
            font_size=40,
        )

        # definition.arrange(DOWN, aligned_edge=LEFT)
        self.definition.set_width(config.frame_width - 2)

        self.play(Write(self.definition), run_time=6) 
        self.wait()

    def transition(self):
        # ---------------- Transition ----------------

        # Create the new title
        new_title = Text(
            "Instantaneous Rate of Change",
            weight=BOLD,
            font_size=40
        )

        # Keep only the phrase
        phrase = self.definition[2]

        self.play(phrase.animate.set_color(YELLOW))
        self.wait()

        self.play(
            FadeOut(self.title),
            FadeOut(self.definition[0]),
            FadeOut(self.definition[1]),
            FadeOut(self.definition[3]),
            # phrase.animate.scale(1.8).move_to(new_title),
            # run_time=2,
        )

        # Replace italic LaTeX with the clean title
        self.play(
            ReplacementTransform(phrase, new_title),
            run_time=1
        )
        self.wait(2)

        self.play(FadeOut(new_title))
        # self.play(new_title.animate.to_edge(UP))

        
class Instantaneous_Rate_of_Change(Scene):
    def construct(self):
        self.show_title()
        function = self.show_function()
        self.explain_variables(function) 
        # self.show_second_point()

    def show_title(self):
        # ---------------- Title ----------------
        
        self.title = Text("Rate of Change", weight=BOLD)

        self.play(FadeIn(self.title))
        self.wait(3)

        self.play(self.title.animate.to_edge(UP))
        self.wait(1)

    def show_function(self):

        # Large function in the center
        function = MathTex("y", "=", "f(","x", ")").scale(2)

        self.play(Write(function))
        self.wait(2)

        # Create the bullet
        bullet = Dot(radius=0.08)

        # Create the smaller version of the function
        function_target = MathTex("y", "=", "f(","x", ")").scale(0.9)

        # Create the final bullet line
        line = VGroup(bullet, function_target)
        line.arrange(RIGHT, buff=0.3)

        # Move the entire line to the left side of the screen
        line.to_edge(LEFT, buff=1)
        line.shift(UP * 2)

        # Animate the function to its final position
        self.play(
            FadeIn(bullet),
            Transform(function, function_target),
            run_time=1.5
        )

        # Move the transformed function beside the bullet
        self.play(
            function.animate.move_to(function_target),
            run_time=1
        )

        self.wait()

        return function
    
    def explain_variables(self, function):
        # pass

        # ---------------- Highlight x ----------------

        self.play(
            function[3].animate.scale(1.6).set_color(BLUE),
            rate_func=there_and_back,
            run_time=1
        )

        self.wait()

        # ---------------- Highlight y ----------------

        self.play(
            function[0].animate.scale(1.6).set_color(GREEN),
            rate_func=there_and_back,
            run_time=1
        )

        self.wait()

        # ---------------- Number Lines ----------------

        x_line = NumberLine(
            x_range=[-10, 10, 1],
            length=4,
            include_numbers=False,
        ).rotate(PI / 2)

        y_line = NumberLine(
            x_range=[-10, 10, 1],
            length=4,
            include_numbers=False,
        ).rotate(PI / 2)

        x_line.shift(RIGHT * 0.5)
        y_line.shift(RIGHT * 3)

        # Labels
        x_label = MathTex("x")
        y_label = MathTex("y")

        # Variables
        x_var = Variable(
            0,
            x_label,
            num_decimal_places=1,
        )

        y_var = Variable(
            0,
            y_label,
            num_decimal_places=1,
        )

        x_var.next_to(x_line, UP)
        y_var.next_to(y_line, UP)

        # Create axes and transform labels
        self.play(
            ReplacementTransform(function[3].copy(), x_var.label),
            Create(x_line),
            run_time=1.5
        )
        self.wait()

        self.play(
            ReplacementTransform(function[0].copy(), y_var.label),
            Create(y_line),
            run_time=1.5
        )

        self.wait()

        self.play(
            Create(x_var.value),
            Create(y_var.value),
            run_time=1.5)

        self.wait()

        # ---------------- Tracker ----------------

        tracker = ValueTracker(0)

        # Keep the displayed values synchronized
        x_var.value.add_updater(
            lambda m: m.set_value(tracker.get_value())
        )

        y_var.value.add_updater(
            lambda m: m.set_value(-1.8 * tracker.get_value())
        )

        # ---------------- Dots ----------------

        x_dot = always_redraw(
            lambda: Dot(
                color=BLUE,
                radius=0.15
            ).move_to(
                x_line.n2p(tracker.get_value())
            )
        )

        y_dot = always_redraw(
            lambda: Dot(
                color=GREEN,
                radius=0.15
            ).move_to(
                y_line.n2p(-1.8 * tracker.get_value())
            )
        )

        self.add(x_dot, y_dot)

        self.wait(1)

        # ---------------- Animate ----------------

        self.play(
            tracker.animate.set_value(4),
            run_time=2,
        )

        self.wait()

        self.play(
            tracker.animate.set_value(-4),
            run_time=2,
        )

        self.wait()

        self.play(
            tracker.animate.set_value(0),
            run_time=2,
        )

        self.wait(2)

        self.show_second_point()

        start_x = x_line.n2p(0)
        start_y = y_line.n2p(0) 

        x_brace = always_redraw(
            lambda: BraceBetweenPoints(
                start_x,
                x_dot.get_center(),
                direction=LEFT
            )
        )

        y_brace = always_redraw(
            lambda: BraceBetweenPoints(
                start_y,
                y_dot.get_center(),
                direction=RIGHT
            )
        )

        x_distance = always_redraw(
            lambda: MathTex(
                f"{(tracker.get_value()):.1f}"
            ).next_to(
                x_brace,
                LEFT
            )
        )

        y_distance = always_redraw(
            lambda: MathTex(
                f"{-1.8*tracker.get_value():.1f}"
            ).next_to(
                y_brace,
                RIGHT
            )
        )

        self.add(x_brace, y_brace, x_distance, y_distance)

        self.play(
            tracker.animate.set_value(4),
            run_time=2,
        )

        self.wait()

        delta_x = MathTex(r"\Delta x =")
        delta_y = MathTex(r"\Delta y =")

        delta_x.to_edge(LEFT, buff=1)
        delta_x.shift(DOWN * 0.8)

        delta_y.next_to(delta_x, DOWN, buff=0.6)

        self.play(
            ReplacementTransform(x_brace.copy(), delta_x),
            ReplacementTransform(y_brace.copy(), delta_y),
        )
        self.wait()
        
        delta_x_value = always_redraw(
            lambda: DecimalNumber(
                (tracker.get_value()),
                num_decimal_places=1
            ).next_to(delta_x, RIGHT)
        )

        delta_y_value = always_redraw(
            lambda: DecimalNumber(
                -1.8 * tracker.get_value(),
                num_decimal_places=1
            ).next_to(delta_y, RIGHT)
        )

        self.play(
            ReplacementTransform(x_distance.copy(), delta_x_value),
            ReplacementTransform(y_distance.copy(), delta_y_value),
        )
        self.wait()

        x_val = tracker.get_value()
        y_val = -1.8 * tracker.get_value()

        ratio = MathTex(
            r"\frac{\Delta y}{\Delta x}", 
            "=", 
            rf"\frac{{{abs(y_val):.1f}}}{{{abs(x_val):.1f}}}"
        )

        ratio.to_edge(LEFT, buff=1)
        ratio.shift(DOWN * 1, RIGHT * 0.5)

        self.play(
            ReplacementTransform(VGroup(delta_x, delta_y), ratio[0]),
            ReplacementTransform(VGroup(delta_x_value, delta_y_value), ratio[2]),
            Write(ratio[1]),
            run_time=2,
        )
        self.wait(2)

        result = MathTex(
            r"\frac{\Delta y}{\Delta x}",
            "=",
            f"{y_val/x_val:.1f}"
        )

        result.move_to(ratio)

        self.play(
            TransformMatchingTex(
                ratio,
                result
            ),
            run_time=2
        )

        self.wait(2)

        self.play(
            *[
                FadeOut(mob)
                for mob in self.mobjects
                if mob not in (x_line, y_line)
            ],
        )

        self.wait()


    def show_second_point(self):

        # Large function in the center
        second_point = Text("How much the function changes?").scale(.6).to_edge(LEFT)
        # function = MathTex("y", "=", "f(","x", ")").scale(2)

        self.play(Write(second_point))
        self.wait(2)

        # Create the bullet
        bullet = Dot(radius=0.08)

        # Create the smaller version of the function
        second_point_target = Text("Calculate Change").scale(0.4)

        # Create the final bullet line
        line = VGroup(bullet, second_point_target)
        line.arrange(RIGHT, buff=0.3)

        # Move the entire line to the left side of the screen
        line.to_edge(LEFT, buff=1)
        line.shift(UP * 1)

        # Animate the function to its final position
        self.play(
            FadeIn(bullet),
            Transform(second_point, second_point_target),
            run_time=1.5
        )

        # Move the transformed function beside the bullet
        self.play(
            second_point.animate.move_to(second_point_target),
            run_time=1
        )

        self.wait()

        return second_point