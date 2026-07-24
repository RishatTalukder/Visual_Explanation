from manim import *

class Finale(Scene):
    def construct(self):
        self.state()

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