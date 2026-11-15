from manim import *
import pandas as pd



class TitleScene(Scene):

    def construct(self):
        self.show_title()
        self.display_table()


    def show_title(self):
        # ---------------- Title ----------------
        self.title = Text("Linear Regression", weight=BOLD)

        self.play(FadeIn(self.title))
        self.wait(3)

        self.play(self.title.animate.to_edge(UP))
        self.wait(1) 
    def display_table(self):
        df = pd.DataFrame({
            "Item": ["Alpha", "Beta", "Gamma"],
            "Score": [92, 85, 78]
        })

        # Convert DataFrame to a list of strings (including headers)
        table_data = [df.columns.tolist()] + df.astype(str).values.tolist()

        table = Table(
            table_data,
            include_outer_lines=True
        ).scale(0.7)

        self.play(Create(table))
        # Highlight a specific cell (row, col are 1-indexed)
        # self.play(table.animate.add_highlighted_cell((2, 2), color=GREEN))
        self.wait()