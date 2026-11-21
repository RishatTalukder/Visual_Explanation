from manim import *
import numpy as np

# ==========================================
# IT VAYA — NEON LAB PALETTE
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
SOFT_RED = "#FF2C2C"


class scene3_intuition(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 2 FINAL STATE
        # ==================================================

        # --- Top Right Header Equation ---
        equation = MathTex(
            r"y = 2x + 1",
            font_size=58 * 0.9,
            color=GREEN
        ).move_to([2.2, 2.7, 0])

        # --- Right Side: Axes ---
        axes = Axes(
            x_range=[0, 3.8, 1],
            y_range=[0, 8.5, 1],
            x_length=3,
            y_length=3,
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

        # Continuous Line y = 2x + 1
        line = axes.plot(
            lambda x: 2 * x + 1,
            x_range=[0, 3.4],
            color=CYAN,
            stroke_width=3.5,
        )

        # Points, Tick Labels & Projection Lines
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

        # --- Left Side: Formulas and Labels ---
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).move_to([-3.85, 1.4, 0])

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

        # Add everything initially
        self.add(
            equation,
            axes, x_axis_label, y_axis_label,
            line, dots, projections, tick_labels,
            linear_title, gen_eq,
            arrow_m, m_val_text,
            arrow_c, c_val_text
        )

        self.wait(1.0)

        # ==================================================
        # STEP 2 (Panel 2): Replace parameters with "?"
        # ==================================================
        m_q = MathTex("m = \,?", font_size=38, color=YELLOW).move_to(m_val_text.get_center())
        c_q = MathTex("c = \,?", font_size=38, color=CORAL).move_to(c_val_text.get_center())

        self.play(
            ReplacementTransform(m_val_text, m_q),
            ReplacementTransform(c_val_text, c_q),
            run_time=0.8,
        )
        self.wait(0.6)

        # ==================================================
        # STEP 3 (Panel 3): Clear line & Set m=0, c=0
        # ==================================================
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).move_to(m_q.get_center())
        c_0 = MathTex("c = 0", font_size=38, color=CORAL).move_to(c_q.get_center())

        self.play(
            FadeOut(line),
            FadeOut(projections),
            ReplacementTransform(m_q, m_0),
            ReplacementTransform(c_q, c_0),
            run_time=1.0,
        )
        self.wait(0.6)

        # ==================================================
        # STEP 4 (Panel 4): Draw Candidate Line y = 0
        # ==================================================
        active_points = [(0, 1), (1, 3), (2, 5), (3, 7)]
        c_tracker = ValueTracker(0.0)

        # Dynamic candidate line: y = 0*x + c
        test_line = always_redraw(
            lambda: axes.plot(
                lambda x: c_tracker.get_value(),
                x_range=[0, 3.4],
                color=CORAL,
                stroke_width=3.5,
            )
        )

        self.play(Create(test_line), run_time=0.9)
        self.wait(0.5)

        # ==================================================
        # STEP 5 & 6 (Panels 5 & 6): Residual Bars & "Error" Label
        # ==================================================
        def get_error_bars():
            c_val = c_tracker.get_value()
            bars = VGroup()
            for px, py in active_points:
                p_top = axes.c2p(px, py)
                p_bot = axes.c2p(px, c_val)
                bar = Line(
                    p_bot, p_top,
                    color=YELLOW,
                    stroke_width=3.2
                )
                bars.add(bar)
            return bars

        error_bars = always_redraw(get_error_bars)
        self.play(Create(error_bars), run_time=0.8)

        # "Error" annotation arrow
        mid_pt_error = axes.c2p(3, 3.5)
        error_label = Text("Error", font_size=26, color=SOFT_RED).move_to(
            mid_pt_error + RIGHT * 1.5 + UP * 1.0
        )
        error_arrow = Arrow(
            start=error_label.get_left() + LEFT * 0.05,
            end=mid_pt_error + RIGHT * 0.1,
            color=LAVENDER,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )

        self.play(
            Write(error_label),
            Create(error_arrow),
            run_time=0.8,
        )
        self.wait(1.0)

        # ==================================================
        # STEP 7 & 8 (Panels 7 & 8): Total Absolute Error = 16
        # ==================================================
        err_calc_full = MathTex(
            r"\text{Total Error} = (1 - 0) + (3 - 0) + (5 - 0) + (7 - 0)",
            font_size=26,
            color=WHITE
        ).move_to([2.2, -3.5, 0])

        err_res_16 = MathTex(
            r"\text{Total Error} = 16",
            font_size=32,
            color=WHITE
        ).move_to([2.2, -3.5, 0])

        self.play(
            FadeOut(error_label),
            FadeOut(error_arrow),
            FadeOut(equation),
            Write(err_calc_full),
            run_time=1.0,
        )
        self.wait(1.0)

        self.play(
            ReplacementTransform(err_calc_full, err_res_16),
            run_time=0.8,
        )
        self.wait(0.8)

        # ==================================================
        # STEP 9 & 10 (Panels 9 & 10): Continuous c sweep with Absolute Error
        # ==================================================
        self.remove(err_res_16, c_0)

        c_text_dynamic = always_redraw(
            lambda: MathTex(
                f"c = {c_tracker.get_value():.1f}" if abs(c_tracker.get_value() - round(c_tracker.get_value())) > 0.05 else f"c = {int(round(c_tracker.get_value()))}",
                font_size=38,
                color=CORAL
            ).move_to(arrow_c.get_end() + DOWN * 0.3)
        )
        self.add(c_text_dynamic)

        def calc_abs_error(c):
            return abs(1 - c) + abs(3 - c) + abs(5 - c) + abs(7 - c)

        err_text_dynamic = always_redraw(
            lambda: MathTex(
                rf"\text{{Total Error}} = {calc_abs_error(c_tracker.get_value()):.1f}" if abs(calc_abs_error(c_tracker.get_value()) - round(calc_abs_error(c_tracker.get_value()))) > 0.05 else rf"\text{{Total Error}} = {int(round(calc_abs_error(c_tracker.get_value())))}",
                font_size=32,
                color=WHITE
            ).move_to([2.2, -3.5, 0])
        )
        self.add(err_text_dynamic)

        # Sweep c: 0 -> 1 -> 3 -> 6 -> 0
        self.play(c_tracker.animate.set_value(1.0), run_time=1.4, rate_func=smooth)
        self.wait(0.8)

        self.play(c_tracker.animate.set_value(3.0), run_time=1.6, rate_func=smooth)
        self.wait(0.8)

        self.play(c_tracker.animate.set_value(8.0), run_time=1.8, rate_func=smooth)
        self.wait(0.8)

        self.play(c_tracker.animate.set_value(0.0), run_time=1.6, rate_func=smooth)
        self.wait(0.8)

        # ==================================================
        # NEW STATE (Between 10 & 11): Error Squared (Squares + Sweep)
        # ==================================================
        self.remove(err_text_dynamic)

        # Helper to build true geometric squares extending right from each vertical error bar
        def build_error_squares(stroke_w=2.4, opacity=0.22):
            c_val = c_tracker.get_value()
            squares = VGroup()
            for px, py in active_points:
                p_top = axes.c2p(px, py)
                p_bot = axes.c2p(px, c_val)
                side_len = abs(p_top[1] - p_bot[1])

                if side_len < 1e-4:
                    continue

                y_min = min(p_top[1], p_bot[1])
                y_max = max(p_top[1], p_bot[1])
                x_left = p_top[0]
                x_right = p_top[0] + side_len

                sq = Polygon(
                    [x_left, y_min, 0],
                    [x_right, y_min, 0],
                    [x_right, y_max, 0],
                    [x_left, y_max, 0],
                    color=YELLOW,
                    fill_color=YELLOW,
                    fill_opacity=opacity,
                    stroke_width=stroke_w,
                )
                squares.add(sq)
            return squares

        # 1) Create initial squares at c = 0 + "Error Squared" callout (matching sketch)
        initial_squares = build_error_squares()
        sq_last = initial_squares[-1]
        sq_top_mid = sq_last.get_top() + UP * 0.4

        err_sq_label = Text("Error Squared", font_size=26, color=SOFT_RED).move_to(
            sq_top_mid + RIGHT * 0.5 + UP * 0.9
        )
        err_sq_arrow = Arrow(
            start=err_sq_label.get_bottom() + LEFT * 0.05,
            end=sq_top_mid + RIGHT * 0.1,
            color=LAVENDER,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            buff=0,
        )

        self.play(
            Create(initial_squares),
            run_time=3.0,
        )

        self.wait(1.0)

        self.play(
            
            Write(err_sq_label),
            Create(err_sq_arrow),
            run_time=1.0,
        )
        self.wait(1.0)


        # 2) Mirror Steps 7 & 8: Show expanded Total Error^2 = 84
        err_sq_calc_full = MathTex(
            r"\text{Total Error}^2 = (1 - 0)^2 + (3 - 0)^2 + (5 - 0)^2 + (7 - 0)^2",
            font_size=24,
            color=WHITE
        ).move_to([2.2, -3.5, 0])

        err_sq_res_84 = MathTex(
            r"\text{Total Error}^2 = 84",
            font_size=32,
            color=WHITE
        ).move_to([2.2, -3.5, 0])

        self.play(
            FadeOut(err_sq_label),
            FadeOut(err_sq_arrow),
            Write(err_sq_calc_full),
            run_time=1.0,
        )
        self.wait(1.0)

        self.play(
            ReplacementTransform(err_sq_calc_full, err_sq_res_84),
            run_time=0.8,
        )
        self.wait(0.8)

        # 3) Mirror Steps 9 & 10: Dynamic squares + Total Error^2 sweep (0 -> 1 -> 3 -> 6 -> 0)
        self.remove(initial_squares, err_sq_res_84)

        error_squares = always_redraw(lambda: build_error_squares(stroke_w=2.4, opacity=0.22))
        self.add(error_squares)

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        err_sq_text_dynamic = always_redraw(
            lambda: MathTex(
                rf"\text{{Total Error}}^2 = {calc_squared_error(c_tracker.get_value()):.1f}"
                if abs(calc_squared_error(c_tracker.get_value()) - round(calc_squared_error(c_tracker.get_value()))) > 0.05
                else rf"\text{{Total Error}}^2 = {int(round(calc_squared_error(c_tracker.get_value())))}",
                font_size=32,
                color=WHITE
            ).move_to([2.2, -3.5, 0])
        )
        self.add(err_sq_text_dynamic)

        # Sweep c: 0 -> 1 -> 3 -> 6 -> 0
        self.play(c_tracker.animate.set_value(1.0), run_time=1.4, rate_func=smooth)
        self.wait(0.8)

        self.play(c_tracker.animate.set_value(3.0), run_time=1.6, rate_func=smooth)
        self.wait(0.8)

        self.play(c_tracker.animate.set_value(8.0), run_time=1.8, rate_func=smooth)
        self.wait(0.8)

        self.play(c_tracker.animate.set_value(0.0), run_time=1.6, rate_func=smooth)
        self.wait(0.8)

        # Clean up bottom readout before scaling into dual layout
        self.play(FadeOut(err_sq_text_dynamic), run_time=0.5)
        self.remove(err_sq_text_dynamic)

        # ==================================================
        # STEP 11 & 12 (Panels 11 & 12): Dual Layout + Squared Error Graph
        # ==================================================
        self.remove(test_line, error_bars, error_squares)

        # Static upper elements to scale
        top_group_static = VGroup(
            axes, x_axis_label, y_axis_label,
            dots[0], dots[1], dots[2], dots[3],
            tick_labels[0], tick_labels[1], tick_labels[2],
            tick_labels[3], tick_labels[4], tick_labels[5],
            tick_labels[6], tick_labels[7],
        )

        eq_group = VGroup(c_text_dynamic, gen_eq, arrow_m, m_0, arrow_c)

        self.play(
            top_group_static.animate.scale(0.58).move_to([2.7, 1.8, 0]),
            linear_title.animate.scale(0.9).move_to([-4.1, 1.8, 0]),
            eq_group.animate.scale(0.85).move_to([-4.1, 0.4, 0]),
            run_time=1.2,
        )

        # Re-attach dynamic elements for upper plot and left formula
        c_text_left = always_redraw(
            lambda: MathTex(
                f"c = {c_tracker.get_value():.1f}" if abs(c_tracker.get_value() - round(c_tracker.get_value())) > 0.05 else f"c = {int(round(c_tracker.get_value()))}",
                font_size=32,
                color=CORAL
            ).move_to(c_text_dynamic.get_center())
        )
        self.remove(c_text_dynamic)
        self.add(c_text_left)

        test_line_scaled = always_redraw(
            lambda: axes.plot(
                lambda x: c_tracker.get_value(),
                x_range=[0, 3.4],
                color=CORAL,
                stroke_width=2.5,
            )
        )
        error_bars_scaled = always_redraw(
            lambda: VGroup(*[
                Line(
                    axes.c2p(px, c_tracker.get_value()),
                    axes.c2p(px, py),
                    color=YELLOW,
                    stroke_width=2.4
                )
                for px, py in active_points
            ])
        )
        error_squares_scaled = always_redraw(
            lambda: build_error_squares(stroke_w=1.8, opacity=0.22)
        )
        self.play(
            Create(test_line_scaled),
            Create(error_bars_scaled),
            Create(error_squares_scaled),
        )

        # Lower Graph: Total Error Squared vs c
        error_axes = Axes(
            x_range=[0, 8.5, 2],
            y_range=[0, 95, 20],
            x_length=4.4,
            y_length=2.5,
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2.2,
                "include_tip": True,
                "tip_width": 0.14,
                "tip_height": 0.14,
            },
        ).move_to([2.7, -1.9, 0])

        error_c_label = MathTex("c", color=CORAL, font_size=30).next_to(
            error_axes.x_axis.get_end(), RIGHT, buff=0.12
        )
        error_y_label = MathTex(r"\text{Total Error}^2", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )

        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )
        

        lower_graph_group = VGroup(error_axes, error_c_label, error_y_label, origin_0)
        self.play(Create(lower_graph_group), run_time=1.0)
        self.wait(0.5)

        # Dynamic Tracer dot on Lower Error graph
        err_dot = always_redraw(
            lambda: Dot(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                radius=0.07,
                color=CORAL
            )
        )

        # Traced curve as c moves
        loss_trace = TracedPath(
            err_dot.get_center,
            stroke_color=CORAL,
            stroke_width=3.2
        )
        self.add(loss_trace, err_dot)

        # Milestone dots placed at integer steps of c (0..8)
        plotted_dots = VGroup()
        milestones = set(range(9))  # {0, 1, 2, 3, 4, 5, 6, 7, 8}

        def drop_milestone_dots(mob):
            curr_c = c_tracker.get_value()
            for m in list(milestones):
                if curr_c >= m - 0.03:
                    p_dot = Dot(
                        error_axes.c2p(m, calc_squared_error(m)),
                        radius=0.06,
                        color=YELLOW
                    )
                    plotted_dots.add(p_dot)
                    self.add(p_dot)
                    milestones.remove(m)

        err_dot.add_updater(drop_milestone_dots)

        # Continuous smooth sweep of c from 0 to 8
        c_tracker.set_value(0)
        self.play(
            c_tracker.animate.set_value(8.0),
            run_time=4.5,
            rate_func=linear
        )
        err_dot.remove_updater(drop_milestone_dots)
        self.wait(0.6)

        # Highlight optimal minimum at c = 4 (Error^2 = 20)
        min_point = error_axes.c2p(4, 20)
        min_dot = Dot(min_point, radius=0.1, color=GREEN)
        min_label = MathTex(r"\text{Min } (c=4)", font_size=22, color=GREEN).next_to(
            min_dot, DOWN, buff=0.10
        )

        self.play(
            Flash(
                min_point,
                color=GREEN,
                flash_radius=0.4,
                line_length=0.15,
                num_lines=8,
            ),
            FadeIn(min_dot),
            Write(min_label),
            run_time=0.8,
        )

        self.wait(3.0)


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
            x_length=3,
            y_length=3,
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

