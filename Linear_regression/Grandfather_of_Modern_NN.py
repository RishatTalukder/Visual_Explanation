
from manim import *
import numpy as np

# ==========================================
# IT VAYA — NEON LAB
# ==========================================

config.background_color = "#262335"

BG = "#262335"
PANEL = "#34294F"
WHITE = "#FDEBFF"
PINK = "#FF7EDB"
CYAN = "#36F9F6"
GREEN = "#72F1B8"
YELLOW = "#FDEB5D"
CORAL = "#F97E72"
LAVENDER = "#A99BCB"
## Storyboard Interpretation


class scene2_pattern_visual(Scene):
    def construct(self):
        # ----------------------------------
        # Setup from Scene 1
        # ----------------------------------
        LEFT_X = -1.65
        RIGHT_X = 1.65
        HEADER_Y = 1.35
        ROW_YS = [0.55, -0.25, -1.05, -1.85]
        FONT_SIZE = 54

        def make_value(value, position, color=GREEN):
            return MathTex(
                str(value),
                font_size=FONT_SIZE,
                color=color
            ).move_to(position)

        def make_arrow(y_position):
            return Arrow(
                start=[-0.75, y_position, 0],
                end=[0.75, y_position, 0],
                color=GREEN,
                stroke_width=2.5,
                buff=0,
                max_tip_length_to_length_ratio=0.18,
            )

        def make_row(x, y, row_index):
            ypos = ROW_YS[row_index]
            x_value = make_value(x, [LEFT_X, ypos, 0])
            arrow = make_arrow(ypos)
            if y == '7':
                y_value = make_value(y, [RIGHT_X, ypos, 0], YELLOW)
            else:
                y_value = make_value(y, [RIGHT_X, ypos, 0])
            return VGroup(x_value, arrow, y_value)

        # Recreate Scene 1's final table
        x_header = make_value("x", [LEFT_X, HEADER_Y, 0], CYAN)
        y_header = make_value("y", [RIGHT_X, HEADER_Y, 0], PINK)
        zero = make_value("0", [LEFT_X, ROW_YS[0], 0])
        arrow_0 = make_arrow(ROW_YS[0])
        one = make_value("1", [RIGHT_X, ROW_YS[0], 0])
        row_1 = make_row(1, 3, 1)
        row_2 = make_row(2, 5, 2)
        row_3 = make_row(3, "7", 3)

        table = VGroup(
            x_header, y_header,
            zero, arrow_0, one,
            row_1, row_2, row_3
        )
        table.scale(0.48)
        table.move_to([-4.15, 0, 0])

        equation = MathTex(
            r"y = 2x + 1",
            font_size=58,
            color=GREEN
        ).move_to([1.6, 0.55, 0])

        substitution_3 = MathTex(
            r"y = 1",
            font_size=52,
            color=YELLOW
        ).move_to([1.6, -0.85, 0])

        repeat_note = Text(
            "Now repeat for x = 1, 2, 3",
            font_size=27,
            color=GREEN
        ).move_to([1.6, -2.0, 0])

        self.add(table, equation, substitution_3, repeat_note)
        self.wait(1)

        # ==================================================
        # STEP 2 (Panel 2): Clear intermediate notes, reposition equation
        # ==================================================
        eq_header_pos = [2.2, 2.7, 0]

        self.play(
            FadeOut(substitution_3),
            FadeOut(repeat_note),
            equation.animate.scale(0.9).move_to(eq_header_pos),
            run_time=1.0,
        )
        self.wait(0.5)

        # ==================================================
        # STEP 3 (Panel 3): Create Coordinate Axes
        # ==================================================
        axes = Axes(
            x_range=[0, 3.8, 1],
            y_range=[0, 8.5, 1],
            x_length=4.4,
            y_length=4.2,
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2.5,
                "include_tip": True,
                "tip_width": 0.16,
                "tip_height": 0.16,
            },
        ).move_to([2.2, -0.6, 0])

        x_axis_label = MathTex("x", color=CYAN, font_size=38).next_to(
            axes.x_axis.get_end(), RIGHT, buff=0.15
        )
        y_axis_label = MathTex("y", color=PINK, font_size=38).next_to(
            axes.y_axis.get_end(), UP, buff=0.15
        )
        axes_group = VGroup(axes, x_axis_label, y_axis_label)

        self.play(
            Create(axes),
            Write(x_axis_label),
            Write(y_axis_label),
            run_time=1.2,
        )
        self.wait(0.5)

        # ==================================================
        # STEP 4 (Panel 4): Draw the Line y = 2x + 1
        # ==================================================
        line = axes.plot(
            lambda x: 2 * x + 1,
            x_range=[0, 3.4],
            color=CYAN,
            stroke_width=3.5,
        )

        self.play(Create(line), run_time=1.2)
        self.wait(0.6)

        # ==================================================
        # STEP 5 - 7 (Panels 5, 6, 7): Plot Points & Projections
        # ==================================================
        points_data = [(0, 1), (1, 3), (2, 5), (3, 7)]
        dots = VGroup()
        projections = VGroup()
        tick_labels = VGroup()

        for x_val, y_val in points_data:
            pt_coords = axes.c2p(x_val, y_val)
            dot = Dot(pt_coords, radius=0.08, color=YELLOW)
            dots.add(dot)

            # Axis tick labels
            y_tick = MathTex(str(y_val), font_size=28, color=PINK).next_to(
                axes.c2p(0, y_val), LEFT, buff=0.12
            )
            tick_labels.add(y_tick)

            if x_val > 0:
                x_tick = MathTex(str(x_val), font_size=28, color=CYAN).next_to(
                    axes.c2p(x_val, 0), DOWN, buff=0.12
                )
                tick_labels.add(x_tick)

                # Dashed projection lines
                v_line = DashedLine(
                    axes.c2p(x_val, 0), pt_coords,
                    dash_length=0.08, color=LAVENDER, stroke_width=1.8
                )
                h_line = DashedLine(
                    axes.c2p(0, y_val), pt_coords,
                    dash_length=0.08, color=LAVENDER, stroke_width=1.8
                )
                projections.add(v_line, h_line)
            else:
                x_tick = MathTex("0", font_size=28, color=CYAN).next_to(
                    axes.c2p(0, 0), DOWN + LEFT, buff=0.08
                )
                tick_labels.add(x_tick)

        # Panel 5: Points (0,1) and (1,3)
        self.play(
            FadeIn(dots[0], scale=1.5),
            Write(tick_labels[0]),  # y=1
            Write(tick_labels[1]),  # x=0
            run_time=0.7,
        )
        self.play(
            Create(projections[0]),  # v_line 1
            Create(projections[1]),  # h_line 1
            FadeIn(dots[1], scale=1.5),
            Write(tick_labels[2]),  # y=3
            Write(tick_labels[3]),  # x=1
            run_time=0.9,
        )
        self.wait(0.5)

        # Panel 6: Point (2,5)
        self.play(
            Create(projections[2]),
            Create(projections[3]),
            FadeIn(dots[2], scale=1.5),
            Write(tick_labels[4]),  # y=5
            Write(tick_labels[5]),  # x=2
            run_time=0.9,
        )
        self.wait(0.5)

        # Panel 7: Point (3,7)
        self.play(
            Create(projections[4]),
            Create(projections[5]),
            FadeIn(dots[3], scale=1.5),
            Write(tick_labels[6]),  # y=7
            Write(tick_labels[7]),  # x=3
            run_time=0.9,
        )
        self.wait(1.2)

        # ==================================================
        # STEP 8 (Panel 8): Replace Table with "Linear Relationship"
        # ==================================================
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).move_to([-3.85, 1.4, 0])

        self.play(
            FadeOut(table),
            Write(linear_title),
            run_time=1.2,
        )
        self.wait(0.6)

        # ==================================================
        # STEP 9 (Panel 9): Introduce y = mx + c
        # ==================================================
        gen_eq = MathTex(
            "y", "=", "m", "x", "+", "c",
            font_size=52
        ).move_to([-3.85, 0.2, 0])

        gen_eq[0].set_color(WHITE)
        gen_eq[1].set_color(WHITE)
        gen_eq[2].set_color(YELLOW)  # m
        gen_eq[3].set_color(WHITE)
        gen_eq[4].set_color(WHITE)
        gen_eq[5].set_color(CORAL)   # c

        self.play(Write(gen_eq), run_time=1.0)
        self.wait(1.0)

        # ==================================================
        # STEP 10 (Panel 10): Animate Slope (m)
        # ==================================================
        # Set up dynamic line trackers
        slope_tracker = ValueTracker(2.0)
        intercept_tracker = ValueTracker(1.0)

        # Replace static line with dynamic line
        self.remove(line)
        dynamic_line = always_redraw(
            lambda: axes.plot(
                lambda x: slope_tracker.get_value() * x + intercept_tracker.get_value(),
                x_range=[0, min(3.5, max(0.1, (8.2 - intercept_tracker.get_value()) / max(0.01, slope_tracker.get_value())))],
                color=CYAN,
                stroke_width=3.5,
            )
        )
        self.add(dynamic_line)

        # Arrow under m
        m_char = gen_eq[2]
        arrow_m = Arrow(
            start=m_char.get_bottom() + DOWN * 0.1,
            end=m_char.get_bottom() + DOWN * 0.85 + LEFT * 0.4,
            color=YELLOW,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
            buff=0,
        )
        m_val_text = MathTex("m = 2", font_size=38, color=YELLOW).next_to(
            arrow_m.get_end(), DOWN, buff=0.15
        )

        # Highlight m and animate slope variation
        self.play(
            m_char.animate.scale(1.2),
            run_time=0.6,
        )
        self.play(m_char.animate.scale(1 / 1.2), run_time=0.3)

        # Tilt slope back and forth to show steepness
        self.play(slope_tracker.animate.set_value(0.7), run_time=0.9, rate_func=rate_functions.ease_in_out_sine)
        self.play(slope_tracker.animate.set_value(2.8), run_time=0.9, rate_func=rate_functions.ease_in_out_sine)
        self.play(slope_tracker.animate.set_value(2.0), run_time=0.8, rate_func=rate_functions.ease_in_out_sine)

        self.play(Create(arrow_m), run_time=0.5)
        self.play(Write(m_val_text), run_time=0.6)
        self.wait(0.8)

        # ==================================================
        # STEP 11 (Panel 11): Animate Intercept (c)
        # ==================================================
        c_char = gen_eq[5]
        arrow_c = Arrow(
            start=c_char.get_bottom() + DOWN * 0.1,
            end=c_char.get_bottom() + DOWN * 0.85 + RIGHT * 0.4,
            color=CORAL,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
            buff=0,
        )
        c_val_text = MathTex("c = 1", font_size=38, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.15
        )

        # Highlight c and animate vertical shift
        self.play(
            c_char.animate.scale(1.2),
            # Create(arrow_c),
            run_time=0.6,
        )
        self.play(c_char.animate.scale(1 / 1.2), run_time=0.3)

        # Shift line up and down to show intercept shift
        self.play(intercept_tracker.animate.set_value(3.0), run_time=0.9, rate_func=rate_functions.ease_in_out_sine)
        self.play(intercept_tracker.animate.set_value(-0.5), run_time=0.9, rate_func=rate_functions.ease_in_out_sine)
        self.play(intercept_tracker.animate.set_value(1.0), run_time=0.8, rate_func=rate_functions.ease_in_out_sine)

        self.play(Create(arrow_c), run_time=0.5)
        self.play(Write(c_val_text), run_time=0.6)
        self.wait(0.8)

        # ==================================================
        # STEP 12 (Panel 12): Final Visual Emphasis
        # ==================================================
        # Highlight intercept point (0, 1) and lock final view
        intercept_flash_dot = Dot(axes.c2p(3, 7), radius=0.12, color=CORAL)
        self.play(
            Flash(
                axes.c2p(3, 7),
                color=CORAL,
                flash_radius=0.4,
                line_length=0.15,
                num_lines=8,
            ),
            FadeIn(intercept_flash_dot),
            run_time=0.6,
        )
        self.play(FadeOut(intercept_flash_dot), run_time=0.4)

        self.wait(3.0)


class scene1_intro(Scene):

    def construct(self):

        # ----------------------------------
        # Layout
        # ----------------------------------

        LEFT_X = -1.65
        RIGHT_X = 1.65

        HEADER_Y = 1.35
        ROW_YS = [0.55, -0.25, -1.05, -1.85]

        FONT_SIZE = 54

        # ----------------------------------
        # Helper functions
        # ----------------------------------

        def make_value(value, position, color=GREEN):
            return MathTex(
                str(value),
                font_size=FONT_SIZE,
                color=color
            ).move_to(position)

        def make_arrow(y_position):
            return Arrow(
                start=[-0.75, y_position, 0],
                end=[0.75, y_position, 0],
                color=GREEN,
                stroke_width=2.5,
                buff=0,
                max_tip_length_to_length_ratio=0.18,
            )

        def make_row(x, y, row_index):
            ypos = ROW_YS[row_index]

            x_value = make_value(
                x,
                [LEFT_X, ypos, 0]
            )

            arrow = make_arrow(ypos)

            y_value = make_value(
                y,
                [RIGHT_X, ypos, 0]
            )

            return VGroup(x_value, arrow, y_value)

        def reveal_row(row):
            self.play(
                Write(row[0]),
                Create(row[1]),
                Write(row[2]),
                run_time=1.0
            )

        # ==================================
        # STEP 1
        # Show x = 0
        # ==================================

        x_header = make_value(
            "x",
            [0, 0.55, 0],
            CYAN
        )

        zero = make_value(
            "0",
            [0, -0.35, 0]
        )

        self.play(
            Write(x_header),
            run_time=0.8
        )

        self.play(
            Write(zero),
            run_time=0.8
        )

        self.wait(0.6)

        # ==================================
        # STEP 2
        # Move x = 0 left.
        # Introduce y = 1 on the right.
        # ==================================

        new_x_position = [LEFT_X, HEADER_Y, 0]
        new_zero_position = [LEFT_X, ROW_YS[0], 0]

        y_header = make_value(
            "y",
            [RIGHT_X, HEADER_Y, 0],
            PINK
        )

        one = make_value(
            "1",
            [RIGHT_X, ROW_YS[0], 0]
        )

        arrow_0 = make_arrow(ROW_YS[0])

        self.play(
            x_header.animate.move_to(new_x_position),
            zero.animate.move_to(new_zero_position),
            Write(y_header),
            run_time=1.2
        )

        self.play(
            Create(arrow_0),
            Write(one),
            run_time=1.0
        )

        self.wait(0.7)

        # ==================================
        # STEP 3
        # Add 1 -> 3
        # ==================================

        row_1 = make_row(1, 3, 1)

        reveal_row(row_1)

        self.wait(0.7)

        # ==================================
        # STEP 4
        # Add 2 -> 5
        # ==================================

        row_2 = make_row(2, 5, 2)

        reveal_row(row_2)

        self.wait(0.7)

        # ==================================
        # STEP 5
        # Hold the completed table
        # ==================================

        self.wait(1.5)

        # ==================================
        # STEP 6
        # Introduce 3 -> ?
        # ==================================

        row_3 = make_row(3, "?", 3)

        self.play(
            Write(row_3[0]),
            Create(row_3[1]),
            Write(row_3[2]),
            run_time=1.2
        )

        self.wait(1.0)

        # ==================================
        # STEP 7
        # Reveal the answer: 3 -> 7
        # ==================================

        seven = make_value(
            "7",
            [RIGHT_X, ROW_YS[3], 0],
            YELLOW
        )

        self.play(
            Transform(
                row_3[2],
                seven
            ),
            run_time=1.0
        )

        self.wait(1)

        self.play(
            Flash(
                seven.get_center(),
                color=YELLOW,
                flash_radius=0.45,
                line_length=0.18,
                num_lines=8,
            ),
            run_time=0.5,
        )

        self.wait(2)


        
        # ==================================
        # STEP 8
        # Move table to the LEFT
        # ==================================

        table = VGroup(
            x_header,
            y_header,
            zero,
            arrow_0,
            one,
            row_1,
            row_2,
            row_3
        )

        # Dedicated left-side area.
        # Scale down and anchor the table.
        self.play(
            table.animate
                .scale(0.48)
                .move_to([-4.15, 0, 0]),
            run_time=1.5
        )

        # ==================================
        # STEP 9
        # Ask: What is the pattern?
        # ==================================

        question = Text(
            "What is the pattern?",
            font_size=30,
            color=GREEN
        )

        question.move_to([1.6, 1.65, 0])

        self.play(
            Write(question),
            run_time=1.2
        )

        self.wait(1.2)

        # ==================================
        # STEP 10
        # Reveal 2x + 1
        # ==================================

        pattern = MathTex(
            r"2x + 1",
            font_size=62,
            color=YELLOW
        )

        pattern.move_to([1.6, 0.55, 0])

        self.play(
            Write(pattern),
            run_time=1.3
        )

        self.wait(1.5)

        # ==================================
        # STEP 11
        # Introduce y = 2x + 1
        # ==================================

        equation = MathTex(
            r"y = 2x + 1",
            font_size=58,
            color=GREEN
        )

        equation.move_to(pattern.get_center())

        self.play(
            FadeOut(question),
            ReplacementTransform(pattern, equation),
            run_time=1.2
        )

        self.wait(1)

        # ==================================
        # STEP 12
        # Substitute x = 0
        # ==================================

        substitution_1 = MathTex(
            r"y = 2 \times 0 + 1",
            font_size=42,
            color=WHITE
        )

        substitution_2 = MathTex(
            r"y = 0 + 1",
            font_size=42,
            color=WHITE
        )

        substitution_3 = MathTex(
            r"y = 1",
            font_size=52,
            color=YELLOW
        )

        # Keep all equations in exactly the
        # same dedicated position.
        substitution_position = [1.6, -0.85, 0]

        substitution_1.move_to(substitution_position)
        substitution_2.move_to(substitution_position)
        substitution_3.move_to(substitution_position)

        self.play(
            Write(substitution_1),
            run_time=1.2
        )

        self.wait(0.8)

        self.play(
            ReplacementTransform(
                substitution_1,
                substitution_2
            ),
            run_time=1
        )

        self.wait(0.8)

        self.play(
            ReplacementTransform(
                substitution_2,
                substitution_3
            ),
            run_time=1
        )

        self.wait(1.2)

        # ==================================
        # STEP 13
        # Repeat for x = 1, 2, 3
        # ==================================

        repeat_note = Text(
            "Now repeat for x = 1, 2, 3",
            font_size=27,
            color=GREEN
        )

        repeat_note.move_to([1.6, -2.0, 0])

        self.play(
            FadeIn(repeat_note, shift=UP * 0.2),
            run_time=1
        )

        self.wait(3)


class NeonLabDemo(Scene):
    def construct(self):

        # ----------------------------------
        # 1. INTRO
        # ----------------------------------

        title = Text(
            "LINEAR REGRESSION",
            font_size=42,
            weight=BOLD,
            color=PINK
        )

        subtitle = Text(
            "Finding patterns in data",
            font_size=23,
            color=WHITE
        )

        subtitle.next_to(title, DOWN, buff=0.25)

        self.play(
            FadeIn(title, shift=UP),
            run_time=1
        )
        self.play(FadeIn(subtitle), run_time=0.7)
        self.wait(1)

        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )

        # ----------------------------------
        # 2. CREATE THE GRAPH
        # ----------------------------------

        plane = NumberPlane(
            x_range=[0, 7, 1],
            y_range=[0, 8, 1],
            x_length=8,
            y_length=5,
            background_line_style={
                "stroke_color": LAVENDER,
                "stroke_opacity": 0.20,
                "stroke_width": 1
            },
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2,
                "include_ticks": False
            }
        )

        plane.move_to(DOWN * 0.3)

        x_label = Text(
            "Study Hours",
            font_size=22,
            color=CYAN
        )
        x_label.next_to(plane, DOWN, buff=0.35)

        y_label = Text(
            "Exam Score",
            font_size=22,
            color=CYAN
        )
        y_label.rotate(PI / 2)
        y_label.next_to(plane, LEFT, buff=0.35)

        self.play(Create(plane), run_time=1.5)
        self.play(
            FadeIn(x_label),
            FadeIn(y_label)
        )

        # ----------------------------------
        # 3. DATA POINTS
        # ----------------------------------

        data = [
            (0.8, 1.5),
            (1.5, 2.0),
            (2.0, 3.1),
            (2.8, 3.2),
            (3.5, 4.5),
            (4.0, 4.1),
            (4.8, 5.6),
            (5.5, 6.0),
            (6.2, 7.0),
        ]

        dots = VGroup()

        for x, y in data:
            dot = Dot(
                plane.c2p(x, y),
                radius=0.075,
                color=CYAN
            )

            # Subtle glow behind each data point
            glow = Dot(
                plane.c2p(x, y),
                radius=0.15,
                color=CYAN
            ).set_opacity(0.18)

            dots.add(glow, dot)

        self.play(
            LaggedStart(
                *[FadeIn(dot, scale=0.5) for dot in dots],
                lag_ratio=0.06
            ),
            run_time=2
        )

        self.wait(0.5)

        # ----------------------------------
        # 4. REGRESSION LINE
        # ----------------------------------

        regression = plane.plot(
            lambda x: 0.95 * x + 0.8,
            x_range=[0.3, 6.5],
            color=PINK,
            stroke_width=5
        )

        # Fake neon glow using layered strokes
        glow1 = regression.copy().set_stroke(
            PINK,
            width=18,
            opacity=0.12
        )

        glow2 = regression.copy().set_stroke(
            PINK,
            width=10,
            opacity=0.20
        )

        self.play(
            Create(glow1),
            Create(glow2),
            Create(regression),
            run_time=2
        )

        # ----------------------------------
        # 5. EQUATION
        # ----------------------------------

        equation = MathTex(
            r"y = mx + b",
            font_size=42,
            color=YELLOW
        )

        equation.to_corner(UR, buff=0.5)

        equation_bg = SurroundingRectangle(
            equation,
            color=PANEL,
            fill_color=PANEL,
            fill_opacity=0.95,
            buff=0.2,
            stroke_width=1.5
        )

        self.play(
            FadeIn(equation_bg),
            Write(equation)
        )

        # ----------------------------------
        # 6. FINAL ANNOTATION
        # ----------------------------------

        annotation = Text(
            "A line that captures the trend.",
            font_size=23,
            color=GREEN
        )

        annotation.to_edge(DOWN, buff=0.35)

        self.play(
            FadeIn(annotation, shift=UP)
        )

        self.wait(3)


class scene1_intro3(Scene):
    INPUT_X = -2.0
    OUTPUT_X = 2.0
    HEADER_Y = 1.95
    ROW_YS = (1.0, 0.15, -0.70, -1.55)

    @staticmethod
    def _point(x, y):
        return np.array([x, y, 0.0])

    def _make_value(self, tex, x, y, color=WHITE, scale=1.0):
        return (
            MathTex(tex, color=color)
            .scale(scale)
            .move_to(self._point(x, y))
        )

    def _make_arrow(self, y):
        return Arrow(
            start=self._point(-1.05, y),
            end=self._point(1.05, y),
            buff=0,
            color=CYAN,
            stroke_width=2.8,
        )

    def construct(self):
        # Column headers and short underlines.
        x_header = self._make_value("x", self.INPUT_X, self.HEADER_Y, color=PINK)
        y_header = self._make_value("y", self.OUTPUT_X, self.HEADER_Y, color=PINK)

        x_rule = Line(
            self._point(self.INPUT_X - 0.32, self.HEADER_Y - 0.34),
            self._point(self.INPUT_X + 0.32, self.HEADER_Y - 0.34),
            color=PINK,
            stroke_width=2.4,
        )
        y_rule = Line(
            self._point(self.OUTPUT_X - 0.32, self.HEADER_Y - 0.34),
            self._point(self.OUTPUT_X + 0.32, self.HEADER_Y - 0.34),
            color=PINK,
            stroke_width=2.4,
        )

        input_values = [
            self._make_value(label, self.INPUT_X, y)
            for label, y in zip(("0", "1", "2", "3"), self.ROW_YS)
        ]

        output_labels = ("1", "3", "5", "?")
        output_values = [
            self._make_value(
                label,
                self.OUTPUT_X,
                y,
                color=LAVENDER if label == "?" else WHITE,
            )
            for label, y in zip(output_labels, self.ROW_YS)
        ]

        row_arrows = [self._make_arrow(y) for y in self.ROW_YS]

        # State 1: x column and its first value.
        self.play(Write(x_header), Create(x_rule), run_time=0.8)
        self.play(
            FadeIn(input_values[0], shift=0.12 * UP),
            run_time=0.55,
        )
        self.wait(0.3)

        # State 2: introduce y and the first mapping, 0 -> 1.
        self.play(Write(y_header), Create(y_rule), run_time=0.75)
        self.play(
            Create(row_arrows[0]),
            FadeIn(output_values[0], shift=0.12 * RIGHT),
            run_time=0.8,
        )
        self.wait(0.3)

        def reveal_added_row(index):
            self.play(
                FadeIn(input_values[index], shift=0.12 * UP),
                run_time=0.5,
            )
            self.play(
                Create(row_arrows[index]),
                FadeIn(output_values[index], shift=0.12 * RIGHT),
                run_time=0.8,
            )

        # Add the next two mappings while retaining the earlier rows.
        reveal_added_row(1)  # 1 -> 3
        reveal_added_row(2)  # 2 -> 5

        # The storyboard repeats the same three-row state; hold on it briefly.
        self.wait(1.0)

        # Add the final input with an unknown output.
        reveal_added_row(3)  # 3 -> ?

        self.wait(0.65)

        # Resolve the unknown output as 7.
        final_output = self._make_value(
            "7",
            self.OUTPUT_X,
            self.ROW_YS[3],
            color=YELLOW,
            scale=1.1,
        )
        self.play(
            ReplacementTransform(output_values[3], final_output),
            run_time=0.8,
        )
        self.wait(1.5)




class scene1_intro2(Scene):
    def construct(self):
        # Column X positions
        x_col = -1.6
        arr_col = 0.0
        y_col = 1.6

        # Row Y positions
        header_y = 2.0
        row_y = [1.0, 0.0, -1.0, -2.0]

        # --------------------------------------------------
        # Header Elements
        # --------------------------------------------------
        header_x = MathTex(r"\underline{\,x\,}", color=CYAN, font_size=52)
        header_x.move_to([x_col, header_y, 0])

        header_y_elem = MathTex(r"\underline{\,y\,}", color=PINK, font_size=52)
        header_y_elem.move_to([y_col, header_y, 0])

        # --------------------------------------------------
        # Row 0: 0 -> 1
        # --------------------------------------------------
        val_x0 = MathTex("0", color=WHITE, font_size=46).move_to([x_col, row_y[0], 0])
        arr0 = MathTex(r"\rightarrow", color=LAVENDER, font_size=44).move_to([arr_col, row_y[0], 0])
        val_y0 = MathTex("1", color=WHITE, font_size=46).move_to([y_col, row_y[0], 0])

        # --------------------------------------------------
        # Row 1: 1 -> 3
        # --------------------------------------------------
        val_x1 = MathTex("1", color=WHITE, font_size=46).move_to([x_col, row_y[1], 0])
        arr1 = MathTex(r"\rightarrow", color=LAVENDER, font_size=44).move_to([arr_col, row_y[1], 0])
        val_y1 = MathTex("3", color=WHITE, font_size=46).move_to([y_col, row_y[1], 0])

        # --------------------------------------------------
        # Row 2: 2 -> 5
        # --------------------------------------------------
        val_x2 = MathTex("2", color=WHITE, font_size=46).move_to([x_col, row_y[2], 0])
        arr2 = MathTex(r"\rightarrow", color=LAVENDER, font_size=44).move_to([arr_col, row_y[2], 0])
        val_y2 = MathTex("5", color=WHITE, font_size=46).move_to([y_col, row_y[2], 0])

        # --------------------------------------------------
        # Row 3: 3 -> ? -> 7
        # --------------------------------------------------
        val_x3 = MathTex("3", color=WHITE, font_size=46).move_to([x_col, row_y[3], 0])
        arr3 = MathTex(r"\rightarrow", color=LAVENDER, font_size=44).move_to([arr_col, row_y[3], 0])
        q_mark = MathTex("?", color=YELLOW, font_size=48).move_to([y_col, row_y[3], 0])
        val_y3 = MathTex("7", color=YELLOW, font_size=46).move_to([y_col, row_y[3], 0])

        # ==================================================
        # ANIMATION SEQUENCE
        # ==================================================

        # --- State 1: Column x and first input 0 ---
        self.play(Write(header_x), run_time=0.7)
        self.play(FadeIn(val_x0, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.5)

        # --- State 2: Column y and mapping 0 -> 1 ---
        self.play(Write(header_y_elem), run_time=0.7)
        self.play(
            Write(arr0),
            FadeIn(val_y0, shift=RIGHT * 0.2),
            run_time=0.6,
        )
        self.wait(0.6)

        # --- State 3: Second row 1 -> 3 ---
        self.play(
            FadeIn(val_x1, shift=DOWN * 0.2),
            Write(arr1),
            FadeIn(val_y1, shift=RIGHT * 0.2),
            run_time=0.7,
        )
        self.wait(0.6)

        # --- State 4 & 5: Third row 2 -> 5 and hold to spot pattern ---
        self.play(
            FadeIn(val_x2, shift=DOWN * 0.2),
            Write(arr2),
            FadeIn(val_y2, shift=RIGHT * 0.2),
            run_time=0.7,
        )
        self.wait(1.0)

        # --- State 6: Posing the question 3 -> ? ---
        self.play(
            FadeIn(val_x3, shift=DOWN * 0.2),
            Write(arr3),
            FadeIn(q_mark, shift=RIGHT * 0.2),
            run_time=0.7,
        )
        self.wait(1.2)

        # --- State 7: Revealing the answer 7 ---
        self.play(
            Transform(q_mark, val_y3),
            run_time=0.6,
        )
        self.play(
            Flash(
                val_y3.get_center(),
                color=YELLOW,
                flash_radius=0.45,
                line_length=0.18,
                num_lines=8,
            ),
            run_time=0.5,
        )

        self.wait(2.0)


class scene1_intro1(Scene):
    def construct(self):
        # ---------- table geometry (fixed column anchors) ----------
        X_COL = -1.9            # x-column anchor
        Y_COL = 1.9             # y-column anchor
        HEADER_Y = 1.6          # header row height
        ROW_YS = [0.75, -0.10, -0.95, -1.80]   # data row heights

        # ---------- helpers ----------
        def value_glyph(tex, col_x, row_y, color):
            return MathTex(tex, color=color).move_to([col_x, row_y, 0])

        def row_arrow(row_y):
            return MathTex(r"\rightarrow", color=LAVENDER).move_to([0, row_y, 0])

        # ---------- STATE 1 : the x column begins (x over 0) ----------
        header_x = MathTex("x", color=PINK).scale(1.15).move_to([X_COL, HEADER_Y, 0])
        val_x0 = value_glyph("0", X_COL, ROW_YS[0], CYAN)

        self.play(Write(header_x), run_time=0.9)
        self.play(Write(val_x0), run_time=0.9)
        self.wait(0.5)

        # ---------- STATE 2 : y column + first mapping 0 -> 1 ----------
        header_y = MathTex("y", color=PINK).scale(1.15).move_to([Y_COL, HEADER_Y, 0])
        val_y1 = value_glyph("1", Y_COL, ROW_YS[0], CYAN)
        arrow_0 = row_arrow(ROW_YS[0])

        self.play(
            LaggedStart(
                Write(header_y),
                Write(val_y1),
                FadeIn(arrow_0, scale=0.6),
                lag_ratio=0.35,
            ),
            run_time=1.6,
        )
        self.wait(0.6)

        # ---------- STATE 3 : row 1 -> 3 ----------
        val_x1 = value_glyph("1", X_COL, ROW_YS[1], CYAN)
        arrow_1 = row_arrow(ROW_YS[1])
        val_y3 = value_glyph("3", Y_COL, ROW_YS[1], CYAN)

        self.play(
            LaggedStart(
                Write(val_x1),
                FadeIn(arrow_1, scale=0.6),
                Write(val_y3),
                lag_ratio=0.3,
            ),
            run_time=1.5,
        )
        self.wait(0.5)

        # ---------- STATE 4 : row 2 -> 5 ----------
        val_x2 = value_glyph("2", X_COL, ROW_YS[2], CYAN)
        arrow_2 = row_arrow(ROW_YS[2])
        val_y5 = value_glyph("5", Y_COL, ROW_YS[2], CYAN)

        self.play(
            LaggedStart(
                Write(val_x2),
                FadeIn(arrow_2, scale=0.6),
                Write(val_y5),
                lag_ratio=0.3,
            ),
            run_time=1.5,
        )

        # ---------- STATE 5 : hold — let the pattern breathe ----------
        self.play(
            LaggedStart(
                Indicate(val_y1, scale_factor=1.25, color=WHITE),
                Indicate(val_y3, scale_factor=1.25, color=WHITE),
                Indicate(val_y5, scale_factor=1.25, color=WHITE),
                lag_ratio=0.4,
            ),
            run_time=2.4,
        )
        self.wait(0.4)

        # ---------- STATE 6 : row 3 -> ? ----------
        val_x3 = value_glyph("3", X_COL, ROW_YS[3], CYAN)
        arrow_3 = row_arrow(ROW_YS[3])
        val_yq = value_glyph("?", Y_COL, ROW_YS[3], YELLOW)

        self.play(
            LaggedStart(
                Write(val_x3),
                FadeIn(arrow_3, scale=0.6),
                Write(val_yq),
                lag_ratio=0.3,
            ),
            run_time=1.5,
        )
        self.play(Indicate(val_yq, scale_factor=1.3, color=WHITE), run_time=1.0)
        self.wait(0.6)

        # ---------- STATE 7 : the answer — 7 ----------
        val_y7 = value_glyph("7", Y_COL, ROW_YS[3], GREEN)

        self.play(ReplacementTransform(val_yq, val_y7), run_time=1.0)
        self.play(
            Circumscribe(val_y7, color=GREEN, buff=0.2, stroke_width=3.0),
            run_time=1.6,
        )
        self.wait(1.2)