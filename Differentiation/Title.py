from manim import *

class TitleScene(Scene):
    def construct(self):
        # ---------------- Title ----------------
        title = Text("Differentiation", weight=BOLD)

        self.play(FadeIn(title))
        self.wait(3)

        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # ---------------- Definition ----------------
        definition = Tex(
            r"\textbf{Definition: }",
            r"Differentiation is the process of finding the ",
            r"\textit{instantaneous rate of change}",
            r"of a function with respect to one of its variables.",
            font_size=40,
        )

        # definition.arrange(DOWN, aligned_edge=LEFT)
        definition.set_width(config.frame_width - 2)

        self.play(Write(definition), run_time=6)

        self.wait(2)

        # ---------------- Transition ----------------

        # Create the new title
        new_title = Text(
            "Instantaneous Rate of Change",
            weight=BOLD,
            font_size=40
        )

        # Keep only the phrase
        phrase = definition[2]

        self.play(
            FadeOut(title),
            FadeOut(definition[0]),
            FadeOut(definition[1]),
            FadeOut(definition[3]),
            # phrase.animate.scale(1.8).move_to(new_title),
            # run_time=2,
        )

        # Replace italic LaTeX with the clean title
        self.play(
            ReplacementTransform(phrase, new_title),
            run_time=1
        )

        self.play(new_title.animate.to_edge(UP))

        self.wait()