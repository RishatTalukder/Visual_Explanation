from manim import *



class TitleScene(Scene):

    def construct(self):
        self.show_title()

    def show_title(self):
        # ---------------- Title ----------------
        self.title = Text("Linear Regression", weight=BOLD)

        self.play(FadeIn(self.title))
        self.wait(3)

        # self.play(self.title.animate.to_edge(UP))
        # self.wait(1) 