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

        x_line.shift(RIGHT * .5)
        y_line.shift(RIGHT * 3)

        x_label = MathTex("x").next_to(x_line, UP)
        y_label = MathTex("y").next_to(y_line, UP)

        self.play(
            ReplacementTransform(function[3].copy(), x_label),
            Create(x_line),
            run_time=1.5
        )

        self.play(
            ReplacementTransform(function[0].copy(), y_label),
            Create(y_line),
            run_time=1.5
        )

        self.wait(2)

        # ---------------- Dots ----------------

        tracker = ValueTracker(0)

        x_dot = Dot(color=BLUE, radius=0.15)
        x_dot.move_to(x_line.n2p(tracker.get_value()))


        y_dot = Dot(color=GREEN, radius=0.15)
        y_dot.move_to(y_line.n2p(-1.8 * tracker.get_value()))

        # x moves exactly with the tracker
        x_dot.add_updater(
            lambda d: d.move_to(
                x_line.n2p(tracker.get_value())
            )
        )

        # Example relationship:
        # y = 0.8x + 1
        # (Change this later to whatever function you want.)
        y_dot.add_updater(
            lambda d: d.move_to(
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

        self.play(
            tracker.animate.set_value(-4),
            run_time=2,
        )

        self.play(
            tracker.animate.set_value(0),
            run_time=2,
        )

        self.wait(2)