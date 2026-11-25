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
SOFT_RED = "#F75353"



class scene17_finale(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 16 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Top Title
        # --------------------------------------------------
        perceptron_title = Text(
            "Perceptron Model",
            font_size=36,
            color=WHITE
        ).move_to([0, 2.85, 0])

        # --------------------------------------------------
        # 2. Generalized Input Nodes (x1, x2, ..., xn)
        # --------------------------------------------------
        gen_node_x1 = Circle(
            radius=0.40,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.9,
            stroke_width=2.5
        ).move_to([-4.6, 1.0, 0])
        gen_lbl_x1 = MathTex("x_1", font_size=28, color=WHITE).move_to(gen_node_x1)
        gen_group_x1 = VGroup(gen_node_x1, gen_lbl_x1)

        gen_node_x2 = Circle(
            radius=0.40,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.9,
            stroke_width=2.5
        ).move_to([-4.6, 0.0, 0])
        gen_lbl_x2 = MathTex("x_2", font_size=28, color=WHITE).move_to(gen_node_x2)
        gen_group_x2 = VGroup(gen_node_x2, gen_lbl_x2)

        gen_dots = MathTex(r"\vdots", font_size=34, color=WHITE).move_to([-4.6, -0.85, 0])

        gen_node_xn = Circle(
            radius=0.40,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.9,
            stroke_width=2.5
        ).move_to([-4.6, -1.75, 0])
        gen_lbl_xn = MathTex("x_n", font_size=28, color=WHITE).move_to(gen_node_xn)
        gen_group_xn = VGroup(gen_node_xn, gen_lbl_xn)

        gen_inputs = VGroup(gen_group_x1, gen_group_x2, gen_dots, gen_group_xn)

        # --------------------------------------------------
        # 3. Summation Box
        # --------------------------------------------------
        gen_sum_box = Rectangle(
            width=2.1,
            height=1.4,
            color=LAVENDER,
            stroke_width=2.2,
            fill_color=PANEL,
            fill_opacity=0.9
        ).move_to([-1.65, -0.35, 0])
        gen_sum_text = Text("summation", font_size=21, color=WHITE).move_to(gen_sum_box)
        gen_sum_group = VGroup(gen_sum_box, gen_sum_text)

        # --------------------------------------------------
        # 4. Weight Arrows & Labels (w1, w2, wn)
        # --------------------------------------------------
        arr_in_1 = Arrow(
            gen_node_x1.get_right(),
            gen_sum_box.get_left() + UP * 0.42,
            color=CYAN,
            stroke_width=2.6,
            buff=0.08,
            max_tip_length_to_length_ratio=0.14
        )
        arr_in_2 = Arrow(
            gen_node_x2.get_right(),
            gen_sum_box.get_left(),
            color=CYAN,
            stroke_width=2.6,
            buff=0.08,
            max_tip_length_to_length_ratio=0.14
        )
        arr_in_n = Arrow(
            gen_node_xn.get_right(),
            gen_sum_box.get_left() + DOWN * 0.42,
            color=CYAN,
            stroke_width=2.6,
            buff=0.08,
            max_tip_length_to_length_ratio=0.14
        )
        gen_arrows = VGroup(arr_in_1, arr_in_2, arr_in_n)

        w_lbl_1 = MathTex("w_1", font_size=26, color=YELLOW).next_to(arr_in_1.get_center(), UP, buff=0.10)
        w_lbl_2 = MathTex("w_2", font_size=26, color=YELLOW).next_to(arr_in_2.get_center(), UP, buff=0.10)
        w_lbl_n = MathTex("w_n", font_size=26, color=YELLOW).next_to(arr_in_n.get_center(), DOWN, buff=0.10)
        w_labels = VGroup(w_lbl_1, w_lbl_2, w_lbl_n)

        # --------------------------------------------------
        # 5. Bias Node & Pointer Callout
        # --------------------------------------------------
        arr_sum_to_bias = Arrow(
            gen_sum_box.get_right(),
            np.array([0.25, -0.35, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.20
        )
        gen_bias_node = Circle(
            radius=0.45,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.9,
            stroke_width=2.5
        ).move_to([0.78, -0.35, 0])
        gen_bias_lbl = MathTex("+b", font_size=28, color=WHITE).move_to(gen_bias_node)
        gen_bias_group = VGroup(arr_sum_to_bias, gen_bias_node, gen_bias_lbl)

        bias_label_title = Text("Bias", font_size=23, color=CORAL).next_to(gen_bias_node, UP, buff=0.72)
        arrow_to_bias_node = Arrow(
            start=bias_label_title.get_bottom(),
            end=gen_bias_node.get_top(),
            color=CORAL,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.24
        )
        bias_callout = VGroup(bias_label_title, arrow_to_bias_node)

        # --------------------------------------------------
        # 6. Activation Box & Output Arrow
        # --------------------------------------------------
        arr_bias_to_act = Arrow(
            gen_bias_node.get_right(),
            np.array([1.70, -0.35, 0]),
            color=CYAN,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.20
        )
        gen_act_box = RoundedRectangle(
            corner_radius=0.22,
            width=2.1,
            height=1.15,
            color=GREEN,
            stroke_width=2.5,
            fill_color=PANEL,
            fill_opacity=0.9
        ).move_to([2.80, -0.35, 0])
        gen_act_text = Text("activation", font_size=21, color=GREEN).move_to(gen_act_box)
        gen_act_group = VGroup(arr_bias_to_act, gen_act_box, gen_act_text)

        gen_out_arrow = Arrow(
            gen_act_box.get_right(),
            np.array([4.65, -0.35, 0]),
            color=WHITE,
            stroke_width=2.6,
            buff=0.08,
            max_tip_length_to_length_ratio=0.16
        )

        self.add(
            perceptron_title,
            gen_inputs,
            gen_arrows,
            w_labels,
            gen_sum_group,
            gen_bias_group,
            bias_callout,
            gen_act_group,
            gen_out_arrow
        )
        self.wait(2)

        # ==================================================
        # SCENE 17 FINALE ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Condense Perceptron into a Single Circle Neuron
        # --------------------------------------------------
        single_neuron = Circle(
            radius=0.34,
            color=WHITE,
            fill_color=PANEL,
            fill_opacity=0.95,
            stroke_width=2.6
        ).move_to([-0.5, -0.35, 0])

        new_arr_1 = Arrow(
            gen_node_x1.get_right(), single_neuron.get_left(),
            color=CYAN, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.14
        )
        new_arr_2 = Arrow(
            gen_node_x2.get_right(), single_neuron.get_left(),
            color=CYAN, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.14
        )
        new_arr_n = Arrow(
            gen_node_xn.get_right(), single_neuron.get_left(),
            color=CYAN, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.14
        )
        new_gen_arrows = VGroup(new_arr_1, new_arr_2, new_arr_n)

        single_out_arrow = Arrow(
            single_neuron.get_right(),
            single_neuron.get_right() + RIGHT * 1.4,
            color=WHITE,
            stroke_width=2.5,
            buff=0.08,
            max_tip_length_to_length_ratio=0.20
        )

        self.play(
            FadeOut(bias_callout, shift=UP * 0.2),
            FadeOut(w_labels, shift=UP * 0.2),
            ReplacementTransform(VGroup(gen_sum_group, gen_bias_group, gen_act_group), single_neuron),
            ReplacementTransform(gen_arrows, new_gen_arrows),
            ReplacementTransform(gen_out_arrow, single_out_arrow),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Grow into 3-Layer Neural Network (5 -> 5 -> 3)
        # --------------------------------------------------
        inputs_target_pos = [
            [-5.2, 1.15, 0],
            [-5.2, 0.20, 0],
            [-5.2, -0.65, 0],
            [-5.2, -1.55, 0]
        ]

        x_l1 = -2.6
        x_l2 = -0.1
        x_l3 = 2.4

        y_5_nodes = [1.2, 0.4, -0.4, -1.2, -2.0]
        y_3_nodes = [0.4, -0.4, -1.2]

        layer1_nodes = VGroup(*[
            Circle(radius=0.27, color=WHITE, fill_color=PANEL, fill_opacity=0.95, stroke_width=2.3).move_to([x_l1, y, 0])
            for y in y_5_nodes
        ])
        layer2_nodes = VGroup(*[
            Circle(radius=0.27, color=WHITE, fill_color=PANEL, fill_opacity=0.95, stroke_width=2.3).move_to([x_l2, y, 0])
            for y in y_5_nodes
        ])
        layer3_nodes = VGroup(*[
            Circle(radius=0.27, color=WHITE, fill_color=PANEL, fill_opacity=0.95, stroke_width=2.3).move_to([x_l3, y, 0])
            for y in y_3_nodes
        ])

        # Shift inputs left while morphing single_neuron into the first neuron of Layer 1
        anchor_neuron = layer1_nodes[0].copy()

        self.play(
            gen_group_x1.animate.move_to(inputs_target_pos[0]),
            gen_group_x2.animate.move_to(inputs_target_pos[1]),
            gen_dots.animate.move_to(inputs_target_pos[2]),
            gen_group_xn.animate.move_to(inputs_target_pos[3]),
            Transform(single_neuron, anchor_neuron),
            FadeOut(new_gen_arrows),
            FadeOut(single_out_arrow),
            run_time=1.0,
        )

        # Build connections for each stage
        def make_connections(src_nodes, dst_nodes, color_hex=CYAN, width=1.6, opacity=0.65):
            conns = VGroup()
            for s in src_nodes:
                for d in dst_nodes:
                    conns.add(
                        Line(
                            s.get_right(),
                            d.get_left(),
                            color=color_hex,
                            stroke_width=width,
                            stroke_opacity=opacity
                        )
                    )
            return conns

        in_node_list = [gen_node_x1, gen_node_x2, gen_node_xn]
        conn_in_l1 = make_connections(in_node_list, layer1_nodes, CYAN, 1.7, 0.7)
        conn_l1_l2 = make_connections(layer1_nodes, layer2_nodes, CYAN, 1.6, 0.6)
        conn_l2_l3 = make_connections(layer2_nodes, layer3_nodes, CYAN, 1.6, 0.6)

        final_output_arrows = VGroup(*[
            Arrow(
                n3.get_right(),
                n3.get_right() + RIGHT * 1.05,
                color=WHITE,
                stroke_width=2.2,
                buff=0.06,
                max_tip_length_to_length_ratio=0.22
            )
            for n3 in layer3_nodes
        ])

        # Column 1 (5 neurons): replace anchor with real layer1_nodes[0] and pop remaining 4 one by one
        self.remove(single_neuron)
        self.add(layer1_nodes[0])
        self.play(
            LaggedStart(
                *[FadeIn(n, scale=0.6) for n in layer1_nodes[1:]],
                lag_ratio=0.14
            ),
            LaggedStart(
                *[Create(line) for line in conn_in_l1],
                lag_ratio=0.04
            ),
            run_time=1.3,
        )

        # Column 2 (5 neurons) connected to Layer 1
        self.play(
            LaggedStart(
                *[FadeIn(n, scale=0.6) for n in layer2_nodes],
                lag_ratio=0.14
            ),
            LaggedStart(
                *[Create(line) for line in conn_l1_l2],
                lag_ratio=0.03
            ),
            run_time=1.4,
        )

        # Column 3 (3 neurons) connected to Layer 2 + output arrows
        self.play(
            LaggedStart(
                *[FadeIn(n, scale=0.6) for n in layer3_nodes],
                lag_ratio=0.16
            ),
            LaggedStart(
                *[Create(line) for line in conn_l2_l3],
                lag_ratio=0.04
            ),
            LaggedStart(
                *[GrowArrow(arr) for arr in final_output_arrows],
                lag_ratio=0.15
            ),
            run_time=1.4,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Title: "Perceptron Model" -> "Neural Network"
        # --------------------------------------------------
        nn_title = Text("Neural Network", font_size=34, weight=BOLD, color=CYAN).move_to([0, 2.85, 0])

        self.play(
            ReplacementTransform(perceptron_title, nn_title),
            run_time=1.1,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Wiggle Connection Lines (Weights) & Pop Biases One by One
        # --------------------------------------------------
        all_lines = VGroup(*conn_in_l1, *conn_l1_l2, *conn_l2_l3)
        all_neurons = VGroup(*layer1_nodes, *layer2_nodes, *layer3_nodes)

        self.play(
            LaggedStart(
                *[
                    Wiggle(
                        ln,
                        scale_value=1.06,
                        rotation_angle=0.015 * TAU,
                        n_wiggles=3
                    )
                    for ln in all_lines
                ],
                lag_ratio=0.015
            ),
            run_time=1.5,
        )
        self.wait(2)

        # Each neuron pops out (bias added) and settles back one by one
        self.play(
            LaggedStart(
                *[
                    Succession(
                        n.animate(run_time=0.18).scale(1.22).set_color(CORAL),
                        n.animate(run_time=0.18).scale(1 / 1.22).set_color(WHITE),
                    )
                    for n in all_neurons
                ],
                lag_ratio=0.09
            ),
            run_time=2.0,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Gradient Descent Equation Appears (Top Right)
        # --------------------------------------------------
        eq_pos = np.array([3.65, 2.85, 0])

        gd_beta = MathTex(
            "\\beta_{\\text{new}}", "=", "\\beta_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial\\beta}\\right)",
            font_size=26
        ).move_to(eq_pos)
        gd_beta[0].set_color(PINK)
        gd_beta[1].set_color(WHITE)
        gd_beta[2].set_color(PINK)
        gd_beta[3].set_color(WHITE)
        gd_beta[4].set_color(CYAN)
        gd_beta[5].set_color(YELLOW)

        gd_box = RoundedRectangle(
            corner_radius=0.14,
            width=gd_beta.width + 0.45,
            height=gd_beta.height + 0.30,
            color=CYAN,
            stroke_width=2.0,
            fill_color=PANEL,
            fill_opacity=0.20
        ).move_to(eq_pos)

        self.play(
            FadeIn(gd_box, shift=DOWN * 0.15),
            Write(gd_beta),
            nn_title.animate.move_to([-3.5, 3.0, 0]),
            run_time=1.2,
        )
        self.wait(2)

        # --------------------------------------------------
        # 6. Transform β -> w (Keep RSS for Linear Regression Comparison)
        # --------------------------------------------------
        gd_w = MathTex(
            "w_{\\text{new}}", "=", "w_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial w}\\right)",
            font_size=26
        ).move_to(eq_pos)
        gd_w[0].set_color(YELLOW)
        gd_w[1].set_color(WHITE)
        gd_w[2].set_color(YELLOW)
        gd_w[3].set_color(WHITE)
        gd_w[4].set_color(CYAN)
        gd_w[5].set_color(YELLOW)

        self.play(
            ReplacementTransform(gd_beta, gd_w),
            run_time=1.2,
        )
        self.wait(2)

        # --------------------------------------------------
        # 7. Transform RSS -> Loss -> Canonical L
        # --------------------------------------------------
        gd_loss = MathTex(
            "w_{\\text{new}}", "=", "w_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{Loss}}{\\partial w}\\right)",
            font_size=26
        ).move_to(eq_pos)
        gd_loss[0].set_color(YELLOW)
        gd_loss[1].set_color(WHITE)
        gd_loss[2].set_color(YELLOW)
        gd_loss[3].set_color(WHITE)
        gd_loss[4].set_color(CYAN)
        gd_loss[5].set_color(CORAL)

        self.play(
            ReplacementTransform(gd_w, gd_loss),
            run_time=1.2,
        )
        self.wait(2)

        gd_final = MathTex(
            "w_{\\text{new}}", "=", "w_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial L}{\\partial w}\\right)",
            font_size=28
        ).move_to(eq_pos)
        gd_final[0].set_color(YELLOW)
        gd_final[1].set_color(WHITE)
        gd_final[2].set_color(YELLOW)
        gd_final[3].set_color(WHITE)
        gd_final[4].set_color(CYAN)
        gd_final[5].set_color(GREEN)

        final_box = RoundedRectangle(
            corner_radius=0.14,
            width=gd_final.width + 0.45,
            height=gd_final.height + 0.30,
            color=GREEN,
            stroke_width=2.2,
            fill_color=PANEL,
            fill_opacity=0.20
        ).move_to(eq_pos)

        self.play(
            Transform(gd_box, final_box),
            ReplacementTransform(gd_loss, gd_final),
            run_time=1.2,
        )
        self.play(
            Circumscribe(VGroup(final_box, gd_final), color=GREEN, time_width=0.7),
            run_time=1.2,
        )
        self.wait(2)



class scene16_neural_network(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 15 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Base Left Model (Constructed then scaled & positioned)
        # --------------------------------------------------
        linear_title = Text("Linear Function", font_size=32, color=CYAN).move_to([-0.75, 1.0, 0])

        # Input Nodes
        node_x1 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -0.4, 0])
        lbl_x1 = MathTex("x_1", font_size=26, color=CYAN).move_to(node_x1)
        group_x1 = VGroup(node_x1, lbl_x1)

        node_x2 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -1.4, 0])
        lbl_x2 = MathTex("x_2", font_size=26, color=CYAN).move_to(node_x2)
        group_x2 = VGroup(node_x2, lbl_x2)

        node_x3 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -2.4, 0])
        lbl_x3 = MathTex("x_3", font_size=26, color=CYAN).move_to(node_x3)
        group_x3 = VGroup(node_x3, lbl_x3)
        input_nodes = VGroup(group_x1, group_x2, group_x3)

        # Weight Connections
        sum_box_left_pt1 = np.array([-2.0, -1.05, 0])
        sum_box_left_pt2 = np.array([-2.0, -1.4, 0])
        sum_box_left_pt3 = np.array([-2.0, -1.75, 0])

        arrow_1 = Arrow(node_x1.get_right(), sum_box_left_pt1, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b1 = MathTex("\\beta_1", font_size=23, color=YELLOW).next_to(arrow_1.get_center(), UP, buff=0.1)

        arrow_2 = Arrow(node_x2.get_right(), sum_box_left_pt2, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b2 = MathTex("\\beta_2", font_size=23, color=YELLOW).next_to(arrow_2.get_center(), UP, buff=0.1)

        arrow_3 = Arrow(node_x3.get_right(), sum_box_left_pt3, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b3 = MathTex("\\beta_3", font_size=23, color=YELLOW).next_to(arrow_3.get_center(), DOWN, buff=0.1)
        weights_group = VGroup(arrow_1, lbl_b1, arrow_2, lbl_b2, arrow_3, lbl_b3)

        # Summation Block
        sum_box = RoundedRectangle(
            corner_radius=0.14,
            width=1.3,
            height=1.3,
            color=GREEN,
            stroke_width=2.4,
            fill_color=PANEL,
            fill_opacity=0.1
        ).move_to([-1.35, -1.4, 0])
        sum_symbol = MathTex("\\sum", font_size=44, color=GREEN).move_to(sum_box)
        sum_block = VGroup(sum_box, sum_symbol)

        # Bias Node
        arrow_to_bias = Arrow(
            sum_box.get_right(),
            np.array([0.42, -1.4, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.22
        )
        bias_node = Circle(
            radius=0.46,
            color=CORAL,
            fill_color=PANEL,
            fill_opacity=0.1,
            stroke_width=2.4
        ).move_to([0.95, -1.4, 0])
        bias_lbl = MathTex("+\\beta_0", font_size=25, color=CORAL).move_to(bias_node)
        bias_group = VGroup(arrow_to_bias, bias_node, bias_lbl)

        # Output Node
        arrow_to_out = Arrow(
            bias_node.get_right(),
            np.array([2.35, -1.4, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.22
        )
        y_node = Circle(
            radius=0.38,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.1,
            stroke_width=2.4
        ).move_to([2.85, -1.4, 0])
        y_lbl = MathTex("y", font_size=28, color=PINK).move_to(y_node)
        out_group = VGroup(arrow_to_out, y_node, y_lbl)

        model_elements = VGroup(input_nodes, weights_group, sum_block, bias_group, out_group)
        full_left_model = VGroup(linear_title, model_elements).scale(0.70).move_to([-4, 0.2, 0])

        # --------------------------------------------------
        # 2. Sigmoid Box & Arrow
        # --------------------------------------------------
        sigmoid_box = Rectangle(
            width=1.65,
            height=0.85,
            color=CYAN,
            stroke_width=2.2,
            fill_color=PANEL,
            fill_opacity=0.6,
        )
        sigmoid_formula = MathTex(
            r"\sigma(z) = \frac{1}{1 + e^{-z}}",
            font_size=20,
            color=WHITE,
        ).move_to(sigmoid_box.get_center())
        sigmoid_group = VGroup(sigmoid_box, sigmoid_formula).scale(0.82).next_to(
            y_node, RIGHT, buff=0.55
        )

        arrow_to_sigmoid = Arrow(
            start=y_node.get_right(),
            end=sigmoid_box.get_left(),
            color=WHITE,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.20,
            buff=0.05,
        )

        # --------------------------------------------------
        # 3. Non-Linear Curve Graph & Arrow
        # --------------------------------------------------
        sigmoid_axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[0, 1.15, 0.5],
            x_length=2.8,
            y_length=2.1,
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2.0,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
        ).move_to(sigmoid_box.get_center() + RIGHT * 3.5)

        arrow_to_curve = Arrow(
            start=sigmoid_box.get_right(),
            end=sigmoid_axes.get_left(),
            color=WHITE,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.22,
            buff=0.08,
        )

        curve_label_1 = MathTex("1", font_size=18, color=LAVENDER).next_to(
            sigmoid_axes.c2p(0, 1.0), LEFT, buff=0.08
        )
        curve_label_0 = MathTex("0", font_size=18, color=LAVENDER).next_to(
            sigmoid_axes.c2p(0, 0.0), DOWN + LEFT, buff=0.06
        )

        sigmoid_curve = sigmoid_axes.plot(
            lambda x: 1.0 / (1.0 + np.exp(-x)),
            x_range=[-3.8, 3.8],
            color=GREEN,
            stroke_width=3.4,
        )

        curve_title = Text(
            "Non-linear Pattern",
            font_size=20,
            color=GREEN,
        ).next_to(sigmoid_axes, UP, buff=0.18)

        curve_graph_group = VGroup(sigmoid_axes, curve_label_1, curve_label_0, sigmoid_curve, curve_title)

        # --------------------------------------------------
        # Display Scene 15 Ending State
        # --------------------------------------------------
        self.add(
            full_left_model,
            arrow_to_sigmoid,
            sigmoid_group,
            arrow_to_curve,
            curve_graph_group
        )
        self.wait(2)

        # ==================================================
        # SCENE 16 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Clean Titles & Center Full Assembly
        # --------------------------------------------------
        full_assembly = VGroup(
            model_elements,
            arrow_to_sigmoid,
            sigmoid_group,
            arrow_to_curve,
            sigmoid_axes,
            curve_label_1,
            curve_label_0,
            sigmoid_curve
        )

        self.play(
            FadeOut(linear_title, shift=UP * 0.2),
            FadeOut(curve_title, shift=UP * 0.2),
            run_time=0.8,
        )
        self.play(
            full_assembly.animate.move_to([0, -0.4, 0]),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Titles: "A Neuron" -> "Perceptron Model"
        # --------------------------------------------------
        neuron_title = Text("A Neuron", font_size=36, color=CYAN).move_to([0, 2.7, 0])
        perceptron_title = Text("Perceptron Model", font_size=36, color=WHITE).move_to([0, 2.7, 0])

        self.play(
            FadeIn(neuron_title, shift=DOWN * 0.2),
            run_time=1.0,
        )
        self.wait(2)
        self.play(
            ReplacementTransform(neuron_title, perceptron_title),
            run_time=1.2,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Build Generalized Perceptron Components (Storyboard Reference)
        # --------------------------------------------------
        # Generalized Input Nodes (x1, x2, ..., xn)
        gen_node_x1 = Circle(radius=0.42, color=PINK, fill_color=PANEL, fill_opacity=0.85, stroke_width=2.5).move_to([-4.5, 1.1, 0])
        gen_lbl_x1 = MathTex("x_1", font_size=28, color=WHITE).move_to(gen_node_x1)
        gen_group_x1 = VGroup(gen_node_x1, gen_lbl_x1)

        gen_node_x2 = Circle(radius=0.42, color=PINK, fill_color=PANEL, fill_opacity=0.85, stroke_width=2.5).move_to([-4.5, 0.0, 0])
        gen_lbl_x2 = MathTex("x_2", font_size=28, color=WHITE).move_to(gen_node_x2)
        gen_group_x2 = VGroup(gen_node_x2, gen_lbl_x2)

        gen_dots = MathTex(r"\vdots", font_size=36, color=WHITE).move_to([-4.5, -0.85, 0])

        gen_node_xn = Circle(radius=0.42, color=PINK, fill_color=PANEL, fill_opacity=0.85, stroke_width=2.5).move_to([-4.5, -1.8, 0])
        gen_lbl_xn = MathTex("x_n", font_size=28, color=WHITE).move_to(gen_node_xn)
        gen_group_xn = VGroup(gen_node_xn, gen_lbl_xn)

        gen_inputs = VGroup(gen_group_x1, gen_group_x2, gen_dots, gen_group_xn)

        # Summation Box ("summation")
        gen_sum_box = Rectangle(
            width=2.2,
            height=1.5,
            color=LAVENDER,
            stroke_width=2.2,
            fill_color=PANEL,
            fill_opacity=0.85
        ).move_to([-1.5, -0.4, 0])
        gen_sum_text = Text("summation", font_size=21, color=WHITE).move_to(gen_sum_box)
        gen_sum_group = VGroup(gen_sum_box, gen_sum_text)

        # Connecting Weight Arrows (Blue / Cyan)
        arr_in_1 = Arrow(gen_node_x1.get_right(), gen_sum_box.get_left() + UP * 0.45, color=CYAN, stroke_width=2.6, buff=0.08, max_tip_length_to_length_ratio=0.14)
        arr_in_2 = Arrow(gen_node_x2.get_right(), gen_sum_box.get_left(), color=CYAN, stroke_width=2.6, buff=0.08, max_tip_length_to_length_ratio=0.14)
        arr_in_n = Arrow(gen_node_xn.get_right(), gen_sum_box.get_left() + DOWN * 0.45, color=CYAN, stroke_width=2.6, buff=0.08, max_tip_length_to_length_ratio=0.14)

        gen_arrows = VGroup(arr_in_1, arr_in_2, arr_in_n)

        # Bias Node (+b)
        arr_sum_to_bias = Arrow(gen_sum_box.get_right(), np.array([0.3, -0.4, 0]), color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.20)
        gen_bias_node = Circle(radius=0.48, color=PINK, fill_color=PANEL, fill_opacity=0.85, stroke_width=2.5).move_to([0.85, -0.4, 0])
        gen_bias_lbl = MathTex("+b", font_size=28, color=WHITE).move_to(gen_bias_node)
        gen_bias_group = VGroup(arr_sum_to_bias, gen_bias_node, gen_bias_lbl)

        # Activation Box ("activation")
        arr_bias_to_act = Arrow(gen_bias_node.get_right(), np.array([1.75, -0.4, 0]), color=CYAN, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.20)
        gen_act_box = RoundedRectangle(
            corner_radius=0.22,
            width=2.2,
            height=1.2,
            color=GREEN,
            stroke_width=2.5,
            fill_color=PANEL,
            fill_opacity=0.85
        ).move_to([2.9, -0.4, 0])
        gen_act_text = Text("activation", font_size=21, color=GREEN).move_to(gen_act_box)
        gen_act_group = VGroup(arr_bias_to_act, gen_act_box, gen_act_text)

        # Output Arrow
        gen_out_arrow = Arrow(gen_act_box.get_right(), np.array([4.8, -0.4, 0]), color=WHITE, stroke_width=2.6, buff=0.08, max_tip_length_to_length_ratio=0.16)

        # --------------------------------------------------
        # 4. Transform Assembly into Clean Generalized Perceptron
        # --------------------------------------------------
        self.play(
            FadeOut(sigmoid_axes),
            FadeOut(curve_label_1),
            FadeOut(curve_label_0),
            FadeOut(sigmoid_curve),
            FadeOut(arrow_to_curve),
            ReplacementTransform(input_nodes, gen_inputs),
            ReplacementTransform(weights_group, gen_arrows),
            ReplacementTransform(sum_block, gen_sum_group),
            ReplacementTransform(bias_group, gen_bias_group),
            ReplacementTransform(VGroup(out_group, arrow_to_sigmoid, sigmoid_group), VGroup(gen_act_group, gen_out_arrow)),
            run_time=2.0,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Weights Jump, Wiggle & Reveal 'w' Labels
        # --------------------------------------------------
        w_lbl_1 = MathTex("w_1", font_size=26, color=YELLOW).next_to(arr_in_1.get_center(), UP, buff=0.12)
        w_lbl_2 = MathTex("w_2", font_size=26, color=YELLOW).next_to(arr_in_2.get_center(), UP, buff=0.12)
        w_lbl_n = MathTex("w_n", font_size=26, color=YELLOW).next_to(arr_in_n.get_center(), DOWN, buff=0.12)
        w_labels = VGroup(w_lbl_1, w_lbl_2, w_lbl_n)

        self.play(
            Wiggle(gen_arrows, scale_value=1.12, rotation_angle=0.04 * TAU, n_wiggles=4),
            gen_arrows.animate.set_color(YELLOW),
            run_time=1.4,
        )
        self.play(
            FadeIn(w_labels, shift=UP * 0.15),
            gen_arrows.animate.set_color(CYAN),
            run_time=1.0,
        )
        self.wait(2)

        # --------------------------------------------------
        # 6. Bias Label & Pointer directly to +b Node
        # --------------------------------------------------
        bias_label_title = Text("Bias", font_size=23, color=CORAL).next_to(gen_bias_node, UP, buff=0.75)
        arrow_to_bias_node = Arrow(
            start=bias_label_title.get_bottom(),
            end=gen_bias_node.get_top(),
            color=CORAL,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.24
        )

        self.play(
            FadeIn(bias_label_title, shift=DOWN * 0.15),
            GrowArrow(arrow_to_bias_node),
            Indicate(gen_bias_node, color=CORAL, scale_factor=1.15),
            run_time=1.4,
        )
        self.wait(2)



class scene15_non_linearity(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 14 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Upper Right: Scaled Gradient Descent Rule
        # --------------------------------------------------
        beta_new_eq = MathTex(
            "\\beta_{\\text{new}}", "=", "\\beta_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial\\beta}\\right)",
            font_size=35
        ).scale(0.85).move_to([3.4, 2.2, 0])
        beta_new_eq[0].set_color(PINK)
        beta_new_eq[1].set_color(WHITE)
        beta_new_eq[2].set_color(PINK)
        beta_new_eq[3].set_color(WHITE)
        beta_new_eq[4].set_color(CYAN)
        beta_new_eq[5].set_color(YELLOW)

        # --------------------------------------------------
        # 2. Perceptron Bounding Box & Header Formula
        # --------------------------------------------------
        perceptron_box = RoundedRectangle(
            corner_radius=0.2,
            width=8.6,
            height=3.6,
            color=LAVENDER,
            stroke_width=1.8,
            fill_color=PANEL,
            fill_opacity=0.2
        ).move_to([-0.75, -1.4, 0])

        neuron_title = MathTex(
            "y", "=", "\\sum_{i=1}^n", "\\beta_i", "x_i", "+", "\\beta_0",
            font_size=36
        ).move_to(perceptron_box.get_top() + UP * 0.6)
        neuron_title[0].set_color(WHITE)
        neuron_title[1].set_color(WHITE)
        neuron_title[2].set_color(GREEN)   # summation
        neuron_title[3].set_color(YELLOW)  # beta_i
        neuron_title[4].set_color(CYAN)    # x_i
        neuron_title[5].set_color(WHITE)
        neuron_title[6].set_color(CORAL)   # beta_0

        # --------------------------------------------------
        # 3. Input Nodes (x1, x2, x3)
        # --------------------------------------------------
        node_x1 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -0.4, 0])
        lbl_x1 = MathTex("x_1", font_size=26, color=CYAN).move_to(node_x1)
        group_x1 = VGroup(node_x1, lbl_x1)

        node_x2 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -1.4, 0])
        lbl_x2 = MathTex("x_2", font_size=26, color=CYAN).move_to(node_x2)
        group_x2 = VGroup(node_x2, lbl_x2)

        node_x3 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -2.4, 0])
        lbl_x3 = MathTex("x_3", font_size=26, color=CYAN).move_to(node_x3)
        group_x3 = VGroup(node_x3, lbl_x3)

        input_nodes = VGroup(group_x1, group_x2, group_x3)

        # --------------------------------------------------
        # 4. Weight Arrows & Labels (beta_1, beta_2, beta_3)
        # --------------------------------------------------
        sum_box_left_pt1 = np.array([-2.0, -1.05, 0])
        sum_box_left_pt2 = np.array([-2.0, -1.4, 0])
        sum_box_left_pt3 = np.array([-2.0, -1.75, 0])

        arrow_1 = Arrow(node_x1.get_right(), sum_box_left_pt1, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b1 = MathTex("\\beta_1", font_size=23, color=YELLOW).next_to(arrow_1.get_center(), UP, buff=0.1)

        arrow_2 = Arrow(node_x2.get_right(), sum_box_left_pt2, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b2 = MathTex("\\beta_2", font_size=23, color=YELLOW).next_to(arrow_2.get_center(), UP, buff=0.1)

        arrow_3 = Arrow(node_x3.get_right(), sum_box_left_pt3, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b3 = MathTex("\\beta_3", font_size=23, color=YELLOW).next_to(arrow_3.get_center(), DOWN, buff=0.1)

        weights_group = VGroup(arrow_1, lbl_b1, arrow_2, lbl_b2, arrow_3, lbl_b3)

        # --------------------------------------------------
        # 5. Summation Block
        # --------------------------------------------------
        sum_box = RoundedRectangle(
            corner_radius=0.14,
            width=1.3,
            height=1.3,
            color=GREEN,
            stroke_width=2.4,
            fill_color=PANEL,
            fill_opacity=0.1
        ).move_to([-1.35, -1.4, 0])
        sum_symbol = MathTex("\\sum", font_size=44, color=GREEN).move_to(sum_box)
        sum_block = VGroup(sum_box, sum_symbol)

        # --------------------------------------------------
        # 6. Bias Node
        # --------------------------------------------------
        arrow_to_bias = Arrow(
            sum_box.get_right(),
            np.array([0.42, -1.4, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.22
        )
        bias_node = Circle(
            radius=0.46,
            color=CORAL,
            fill_color=PANEL,
            fill_opacity=0.1,
            stroke_width=2.4
        ).move_to([0.95, -1.4, 0])
        bias_lbl = MathTex("+\\beta_0", font_size=25, color=CORAL).move_to(bias_node)
        bias_group = VGroup(arrow_to_bias, bias_node, bias_lbl)

        # --------------------------------------------------
        # 7. Output Node
        # --------------------------------------------------
        arrow_to_out = Arrow(
            bias_node.get_right(),
            np.array([2.35, -1.4, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.22
        )
        y_node = Circle(
            radius=0.38,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.1,
            stroke_width=2.4
        ).move_to([2.85, -1.4, 0])
        y_lbl = MathTex("y", font_size=28, color=PINK).move_to(y_node)
        out_group = VGroup(arrow_to_out, y_node, y_lbl)

        # --------------------------------------------------
        # Display Scene 14 Ending State
        # --------------------------------------------------
        self.add(
            beta_new_eq,
            perceptron_box,
            neuron_title,
            input_nodes,
            weights_group,
            sum_block,
            bias_group,
            out_group
        )
        self.wait(2)

        # ==================================================
        # SCENE 15 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Title transforms to "Linear Function" & clean UI
        # --------------------------------------------------
        linear_title = Text("Linear Function", font_size=32, color=CYAN).move_to(neuron_title.get_center())

        self.play(
            ReplacementTransform(neuron_title, linear_title),
            FadeOut(perceptron_box),
            FadeOut(beta_new_eq, shift=UP * 0.4),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Scale down model & shift to the left
        # --------------------------------------------------
        model_elements = VGroup(input_nodes, weights_group, sum_block, bias_group, out_group)
        full_left_model = VGroup(linear_title, model_elements)

        self.play(
            full_left_model.animate.scale(0.70).move_to([-4, 0.2, 0]),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Arrow from y to Linear Graph on the Right
        # --------------------------------------------------
        

        linear_axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=3.0,
            y_length=2.3,
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2.0,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
        ).move_to(full_left_model.get_right() + RIGHT * 4 + DOWN * 0.28)

        arrow_to_linear = Arrow(
            start=y_node.get_right() + RIGHT * 0.05,
            end=linear_axes.get_left() + LEFT * 0.05,
            color=WHITE,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.20,
            buff=0.08
        )

        linear_line = linear_axes.plot(
            lambda x: 0.85 * x,
            color=PINK,
            stroke_width=3.2
        )

        linear_graph_title = Text(
            "Linear Pattern",
            font_size=20,
            color=PINK
        ).next_to(linear_axes, UP, buff=0.18)

        linear_graph_group = VGroup(linear_axes, linear_line, linear_graph_title)

        self.play(
            GrowArrow(arrow_to_linear),
            Create(linear_axes),
            FadeIn(linear_graph_title, shift=DOWN * 0.15),
            run_time=1.3,
        )
        self.play(
            Create(linear_line),
            run_time=1.2,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Linear Graph morphs into Sigmoid Activation Box
        # --------------------------------------------------
        sigmoid_box = Rectangle(
            width=1.65,
            height=0.85,
            color=CYAN,
            stroke_width=2.2,
            fill_color=PANEL,
            fill_opacity=0.6,
        ).move_to(linear_axes.get_center())

        sigmoid_formula = MathTex(
            r"\sigma(z) = \frac{1}{1 + e^{-z}}",
            font_size=20,
            color=WHITE,
        ).move_to(sigmoid_box.get_center())
        sigmoid_group = VGroup(sigmoid_box, sigmoid_formula)

        arrow_to_sigmoid = always_redraw(
            lambda: Arrow(
                start=y_node.get_right(),
                end=sigmoid_box.get_left(),
                color=WHITE,
                stroke_width=2.2,
                max_tip_length_to_length_ratio=0.20,
                buff=0.05,
            )
        )

        # self.remove(arrow_to_linear)
        # self.add(arrow_to_sigmoid)
        self.play(
            ReplacementTransform(arrow_to_linear, arrow_to_sigmoid),
            ReplacementTransform(linear_graph_group, sigmoid_group),
            run_time=1.6,
        )
        self.wait(2)

        # Move Sigmoid box + formula right next to y_node, with arrow adjusting automatically
        target_sigmoid_group = sigmoid_group.copy().scale(0.82).next_to(
            y_node, RIGHT, buff=0.55
        )
        self.play(
            Transform(sigmoid_group, target_sigmoid_group),
            run_time=1.2,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Sigmoid Box points to Non-linear S-Curve Graph
        # --------------------------------------------------
        sigmoid_axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[0, 1.15, 0.5],
            x_length=2.8,
            y_length=2.1,
            axis_config={
                "color": LAVENDER,
                "stroke_width": 2.0,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            },
        ).move_to(sigmoid_box.get_center() + RIGHT * 3.5)

        arrow_to_curve = Arrow(
            start=sigmoid_box.get_right(),
            end=sigmoid_axes.get_left(),
            color=WHITE,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.22,
            buff=0.08,
        )

        curve_label_1 = MathTex("1", font_size=18, color=LAVENDER).next_to(
            sigmoid_axes.c2p(0, 1.0), LEFT, buff=0.08
        )
        curve_label_0 = MathTex("0", font_size=18, color=LAVENDER).next_to(
            sigmoid_axes.c2p(0, 0.0), DOWN + LEFT, buff=0.06
        )

        sigmoid_curve = sigmoid_axes.plot(
            lambda x: 1.0 / (1.0 + np.exp(-x)),
            x_range=[-3.8, 3.8],
            color=GREEN,
            stroke_width=3.4,
        )

        curve_title = Text(
            "Non-linear Pattern",
            font_size=20,
            color=GREEN,
        ).next_to(sigmoid_axes, UP, buff=0.18)

        curve_graph_group = VGroup(sigmoid_axes, curve_label_1, curve_label_0, curve_title)

        self.play(
            GrowArrow(arrow_to_curve),
            Create(sigmoid_axes),
            Write(curve_label_1),
            Write(curve_label_0),
            FadeIn(curve_title, shift=DOWN * 0.15),
            run_time=1.4,
        )
        self.play(
            Create(sigmoid_curve),
            run_time=1.6,
        )
        self.play(
            Indicate(sigmoid_curve, color=YELLOW, scale_factor=1.08),
            run_time=1.2,
        )
        self.wait(2)



class scene14_connection(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 13 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Top Middle: Grand Title & Underline
        # --------------------------------------------------
        final_title = Text(
            "Linear Regression",
            font_size=42,
            weight=BOLD,
            color=CYAN
        ).move_to([0, 3.0, 0])

        underline = Line(
            start=final_title.get_left() + DOWN * 0.28,
            end=final_title.get_right() + DOWN * 0.28,
            color=PINK,
            stroke_width=2.5,
        )

        top_title_group = VGroup(final_title, underline)

        # --------------------------------------------------
        # 2. Left Side: Multivariate Model & Subtitle
        # --------------------------------------------------
        sum_eq = MathTex(
            "y", "=", "\\sum_{i=1}^n", "\\beta_i", "x_i", "+", "\\beta_0",
            font_size=36
        ).move_to([-3.65, 0.4, 0])
        sum_eq[0].set_color(WHITE)
        sum_eq[1].set_color(WHITE)
        sum_eq[2].set_color(GREEN)   # summation
        sum_eq[3].set_color(YELLOW)  # beta_i
        sum_eq[4].set_color(CYAN)    # x_i
        sum_eq[5].set_color(WHITE)
        sum_eq[6].set_color(CORAL)   # beta_0

        model_subtitle = Text(
            "Multivariate Linear Model",
            font_size=20,
            color=LAVENDER
        ).next_to(sum_eq, DOWN, buff=0.45)

        # --------------------------------------------------
        # 3. Right Side: Generalized Gradient Descent Update Rule
        # --------------------------------------------------
        rule_title = Text(
            "Gradient Descent Update Rule",
            font_size=23,
            color=GREEN
        ).move_to([2.7, 1.45, 0])

        beta_new_eq = MathTex(
            "\\beta_{\\text{new}}", "=", "\\beta_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial\\beta}\\right)",
            font_size=35
        ).move_to([2.7, 0.3, 0])
        beta_new_eq[0].set_color(PINK)
        beta_new_eq[1].set_color(WHITE)
        beta_new_eq[2].set_color(PINK)
        beta_new_eq[3].set_color(WHITE)
        beta_new_eq[4].set_color(CYAN)
        beta_new_eq[5].set_color(YELLOW)

        single_rule_box = RoundedRectangle(
            corner_radius=0.16,
            width=beta_new_eq.width + 0.65,
            height=beta_new_eq.height + 0.55,
            color=CYAN,
            stroke_width=2.2,
        ).move_to(beta_new_eq)

        # --------------------------------------------------
        # Display Scene 13 Ending State
        # --------------------------------------------------
        self.add(
            top_title_group,
            sum_eq,
            model_subtitle,
            rule_title,
            single_rule_box,
            beta_new_eq
        )
        self.wait(2)

        # ==================================================
        # SCENE 14 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Clean UI & Setup Top Reference Equations
        # --------------------------------------------------
        top_model_full = MathTex(
            "y", "=", "\\sum", "\\beta_i", "x_i", "+", "\\beta_0",
            font_size=34
        ).move_to([-3.8, 2.2, 0])
        top_model_full[0].set_color(WHITE)
        top_model_full[1].set_color(WHITE)
        top_model_full[2].set_color(GREEN)
        top_model_full[3].set_color(YELLOW)
        top_model_full[4].set_color(CYAN)
        top_model_full[5].set_color(WHITE)
        top_model_full[6].set_color(CORAL)

        self.play(
            FadeOut(top_title_group, shift=UP * 0.3),
            FadeOut(model_subtitle, shift=DOWN * 0.2),
            FadeOut(rule_title, shift=UP * 0.2),
            FadeOut(single_rule_box),
            beta_new_eq.animate.scale(0.85).move_to([3.4, 2.2, 0]),
            ReplacementTransform(sum_eq, top_model_full),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. x_i flies down into 3 Input Nodes (x1, x2, x3)
        # --------------------------------------------------
        self.play(
            Indicate(top_model_full[4], color=CYAN, scale_factor=1.35),
            run_time=1.0,
        )

        node_x1 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -0.4, 0])
        lbl_x1 = MathTex("x_1", font_size=26, color=CYAN).move_to(node_x1)
        group_x1 = VGroup(node_x1, lbl_x1)

        node_x2 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -1.4, 0])
        lbl_x2 = MathTex("x_2", font_size=26, color=CYAN).move_to(node_x2)
        group_x2 = VGroup(node_x2, lbl_x2)

        node_x3 = Circle(radius=0.36, color=CYAN, fill_color=PANEL, fill_opacity=0.9, stroke_width=2.4).move_to([-4.4, -2.4, 0])
        lbl_x3 = MathTex("x_3", font_size=26, color=CYAN).move_to(node_x3)
        group_x3 = VGroup(node_x3, lbl_x3)

        top_model_step2 = MathTex(
            "y", "=", "\\sum", "\\beta_i", "+", "\\beta_0",
            font_size=34
        ).move_to([-3.8, 2.2, 0])
        top_model_step2[0].set_color(WHITE)
        top_model_step2[1].set_color(WHITE)
        top_model_step2[2].set_color(GREEN)
        top_model_step2[3].set_color(YELLOW)
        top_model_step2[4].set_color(WHITE)
        top_model_step2[5].set_color(CORAL)

        self.play(
            TransformFromCopy(top_model_full[4], group_x1),
            TransformFromCopy(top_model_full[4], group_x2),
            TransformFromCopy(top_model_full[4], group_x3),
            ReplacementTransform(top_model_full, top_model_step2),
            run_time=1.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. β_i flies down into Weight Arrows (β1, β2, β3)
        # --------------------------------------------------
        self.play(
            Indicate(top_model_step2[3], color=YELLOW, scale_factor=1.35),
            run_time=1.0,
        )

        sum_box_left_pt1 = np.array([-2.0, -1.05, 0])
        sum_box_left_pt2 = np.array([-2.0, -1.4, 0])
        sum_box_left_pt3 = np.array([-2.0, -1.75, 0])

        arrow_1 = Arrow(node_x1.get_right(), sum_box_left_pt1, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b1 = MathTex("\\beta_1", font_size=23, color=YELLOW).next_to(arrow_1.get_center(), UP, buff=0.1)

        arrow_2 = Arrow(node_x2.get_right(), sum_box_left_pt2, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b2 = MathTex("\\beta_2", font_size=23, color=YELLOW).next_to(arrow_2.get_center(), UP, buff=0.1)

        arrow_3 = Arrow(node_x3.get_right(), sum_box_left_pt3, color=WHITE, stroke_width=2.4, buff=0.08, max_tip_length_to_length_ratio=0.10)
        lbl_b3 = MathTex("\\beta_3", font_size=23, color=YELLOW).next_to(arrow_3.get_center(), DOWN, buff=0.1)

        weights_group = VGroup(arrow_1, lbl_b1, arrow_2, lbl_b2, arrow_3, lbl_b3)

        top_model_step3 = MathTex(
            "y", "=", "\\sum", "+", "\\beta_0",
            font_size=34
        ).move_to([-3.8, 2.2, 0])
        top_model_step3[0].set_color(WHITE)
        top_model_step3[1].set_color(WHITE)
        top_model_step3[2].set_color(GREEN)
        top_model_step3[3].set_color(WHITE)
        top_model_step3[4].set_color(CORAL)

        self.play(
            TransformFromCopy(top_model_step2[3], weights_group),
            ReplacementTransform(top_model_step2, top_model_step3),
            run_time=1.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Summation symbol (∑) flies into the Summation Block
        # --------------------------------------------------
        self.play(
            Indicate(top_model_step3[2], color=GREEN, scale_factor=1.35),
            run_time=1.0,
        )

        sum_box = RoundedRectangle(
            corner_radius=0.14,
            width=1.3,
            height=1.3,
            color=GREEN,
            stroke_width=2.4,
            fill_color=PANEL,
            fill_opacity=0.1
        ).move_to([-1.35, -1.4, 0])

        sum_symbol = MathTex("\\sum", font_size=44, color=GREEN).move_to(sum_box)

        top_model_step4 = MathTex(
            "y", "=", "+", "\\beta_0",
            font_size=34
        ).move_to([-3.8, 2.2, 0])
        top_model_step4[0].set_color(WHITE)
        top_model_step4[1].set_color(WHITE)
        top_model_step4[2].set_color(WHITE)
        top_model_step4[3].set_color(CORAL)

        self.play(
            Create(sum_box),
            TransformFromCopy(top_model_step3[2], sum_symbol),
            ReplacementTransform(top_model_step3, top_model_step4),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. +β0 flies down into the Bias Node
        # --------------------------------------------------
        self.play(
            Indicate(top_model_step4[2:], color=CORAL, scale_factor=1.35),
            run_time=1.0,
        )

        arrow_to_bias = Arrow(
            sum_box.get_right(),
            np.array([0.42, -1.4, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.22
        )

        bias_node = Circle(
            radius=0.46,
            color=CORAL,
            fill_color=PANEL,
            fill_opacity=0.1,
            stroke_width=2.4
        ).move_to([0.95, -1.4, 0])

        bias_lbl = MathTex("+\\beta_0", font_size=25, color=CORAL).move_to(bias_node)
        bias_group = VGroup(arrow_to_bias, bias_node, bias_lbl)

        top_model_step5 = MathTex(
            "y", "=",
            font_size=34
        ).move_to([-3.8, 2.2, 0])
        top_model_step5[0].set_color(WHITE)
        top_model_step5[1].set_color(WHITE)

        self.play(
            TransformFromCopy(top_model_step4[2:], bias_group),
            ReplacementTransform(top_model_step4, top_model_step5),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 6. y flies down into the Output Node
        # --------------------------------------------------
        self.play(
            Indicate(top_model_step5[0], color=PINK, scale_factor=1.35),
            run_time=1.0,
        )

        arrow_to_out = Arrow(
            bias_node.get_right(),
            np.array([2.35, -1.4, 0]),
            color=WHITE,
            stroke_width=2.4,
            buff=0.08,
            max_tip_length_to_length_ratio=0.22
        )

        y_node = Circle(
            radius=0.38,
            color=PINK,
            fill_color=PANEL,
            fill_opacity=0.1,
            stroke_width=2.4
        ).move_to([2.85, -1.4, 0])

        y_lbl = MathTex("y", font_size=28, color=PINK).move_to(y_node)
        out_group = VGroup(arrow_to_out, y_node, y_lbl)

        self.play(
            TransformFromCopy(top_model_step5[0], out_group),
            FadeOut(top_model_step5, shift=UP * 0.2),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 7. Architecture Subtitle & Final Connection Highlight
        # --------------------------------------------------
        

        perceptron_box = RoundedRectangle(
            corner_radius=0.2,
            width=8.6,
            height=3.6,
            color=LAVENDER,
            stroke_width=1.8,
            fill_color=PANEL,
            fill_opacity=0.2
        ).move_to([-0.75, -1.4, 0])
 
        neuron_title = MathTex(
            "y", "=", "\\sum_{i=1}^n", "\\beta_i", "x_i", "+", "\\beta_0",
            font_size=36 
        ).move_to(perceptron_box.get_top() + UP * 0.6)

        neuron_title[0].set_color(WHITE)
        neuron_title[1].set_color(WHITE)
        neuron_title[2].set_color(GREEN)   # summation
        neuron_title[3].set_color(YELLOW)  # beta_i
        neuron_title[4].set_color(CYAN)    # x_i
        neuron_title[5].set_color(WHITE)
        neuron_title[6].set_color(CORAL)   # beta_0

        self.play(
            Create(perceptron_box),
            FadeIn(neuron_title, shift=UP * 0.15),
            run_time=1.5,
        )

        self.wait(2)

        self.play(
            Indicate(beta_new_eq, color=YELLOW, scale_factor=1.08),
        )

        self.wait(2)

        self.play(
            Indicate(weights_group, color=YELLOW, scale_factor=1.05),
            Indicate(bias_node, color=CORAL, scale_factor=1.08),
            run_time=1.6,
        )
        self.wait(2)





class scene13_expansion(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 12 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Top Middle: Grand Title & Underline
        # --------------------------------------------------
        final_title = Text(
            "Linear Regression",
            font_size=42,
            weight=BOLD,
            color=CYAN
        ).move_to([0, 3.0, 0])

        underline = Line(
            start=final_title.get_left() + DOWN * 0.28,
            end=final_title.get_right() + DOWN * 0.28,
            color=PINK,
            stroke_width=2.5,
        )

        top_title_group = VGroup(final_title, underline)

        # --------------------------------------------------
        # 2. Left Side: Parameterized Linear Model (y = β₁x + β₀)
        # --------------------------------------------------
        beta_eq = MathTex(
            "y", "=", "\\beta_1", "x", "+", "\\beta_0",
            font_size=44
        ).move_to([-3.8, 0.4, 0])
        beta_eq[0].set_color(WHITE)
        beta_eq[1].set_color(WHITE)
        beta_eq[2].set_color(YELLOW)  # beta_1
        beta_eq[3].set_color(WHITE)   # x
        beta_eq[4].set_color(WHITE)
        beta_eq[5].set_color(CORAL)   # beta_0

        # --------------------------------------------------
        # 3. Right Side: Generalized Gradient Descent Update Rule
        # --------------------------------------------------
        rule_title = Text(
            "Gradient Descent Update Rule",
            font_size=23,
            color=GREEN
        ).move_to([2.7, 1.45, 0])

        beta_new_eq = MathTex(
            "\\beta_{\\text{new}}", "=", "\\beta_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial\\beta}\\right)",
            font_size=35
        ).move_to([2.7, 0.3, 0])
        beta_new_eq[0].set_color(PINK)
        beta_new_eq[1].set_color(WHITE)
        beta_new_eq[2].set_color(PINK)
        beta_new_eq[3].set_color(WHITE)
        beta_new_eq[4].set_color(CYAN)
        beta_new_eq[5].set_color(YELLOW)

        single_rule_box = RoundedRectangle(
            corner_radius=0.16,
            width=beta_new_eq.width + 0.65,
            height=beta_new_eq.height + 0.55,
            color=CYAN,
            stroke_width=2.2,
        ).move_to(beta_new_eq)

        right_group = VGroup(rule_title, single_rule_box, beta_new_eq)

        # --------------------------------------------------
        # Display Scene 12 Ending State
        # --------------------------------------------------
        self.add(
            top_title_group,
            beta_eq,
            right_group
        )
        self.wait(2)

        # ==================================================
        # SCENE 13 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Pop / Pulse β₁ and β₀
        # --------------------------------------------------
        self.play(
            Indicate(beta_eq[2], color=YELLOW, scale_factor=1.25),
            Indicate(beta_eq[5], color=CORAL, scale_factor=1.25),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Input and Output Labels with Pointers
        # --------------------------------------------------
        output_text = Text("Output", font_size=20, color=PINK).next_to(beta_eq[0], UP, buff=0.65)
        arrow_output = Arrow(
            start=output_text.get_bottom(),
            end=beta_eq[0].get_top() + UP * 0.08,
            color=PINK,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.25,
            buff=0.06,
        )

        input_text = Text("Input", font_size=20, color=CYAN).next_to(beta_eq[3], UP, buff=0.65)
        arrow_input = Arrow(
            start=input_text.get_bottom(),
            end=beta_eq[3].get_top() + UP * 0.08,
            color=CYAN,
            stroke_width=2.2,
            max_tip_length_to_length_ratio=0.25,
            buff=0.06,
        )

        io_group = VGroup(output_text, arrow_output, input_text, arrow_input)

        self.play(
            FadeIn(output_text, shift=DOWN * 0.15),
            GrowArrow(arrow_output),
            FadeIn(input_text, shift=DOWN * 0.15),
            GrowArrow(arrow_input),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Fade Out Labels & Start Multivariate Extension
        # --------------------------------------------------
        self.play(
            FadeOut(io_group, shift=UP * 0.2),
            run_time=0.9,
        )

        # Step 3A: y = β₁x₁ + β₂x₂ + β₀
        multi_eq_1 = MathTex(
            "y", "=", "\\beta_1", "x_1", "+", "\\beta_2", "x_2", "+", "\\beta_0",
            font_size=33
        ).move_to([-3.65, 0.4, 0])
        multi_eq_1[0].set_color(WHITE)
        multi_eq_1[1].set_color(WHITE)
        multi_eq_1[2].set_color(YELLOW)  # beta_1
        multi_eq_1[3].set_color(CYAN)    # x_1
        multi_eq_1[4].set_color(WHITE)
        multi_eq_1[5].set_color(YELLOW)  # beta_2
        multi_eq_1[6].set_color(CYAN)    # x_2
        multi_eq_1[7].set_color(WHITE)
        multi_eq_1[8].set_color(CORAL)   # beta_0

        self.play(
            ReplacementTransform(beta_eq, multi_eq_1),
            run_time=1.4,
        )
        self.wait(2)

        # Step 3B: y = β₁x₁ + β₂x₂ + β₃x₃ + β₀
        multi_eq_2 = MathTex(
            "y", "=", "\\beta_1", "x_1", "+", "\\beta_2", "x_2", "+", "\\beta_3", "x_3", "+", "\\beta_0",
            font_size=29
        ).move_to([-3.65, 0.4, 0])
        multi_eq_2[0].set_color(WHITE)
        multi_eq_2[1].set_color(WHITE)
        multi_eq_2[2].set_color(YELLOW)
        multi_eq_2[3].set_color(CYAN)
        multi_eq_2[4].set_color(WHITE)
        multi_eq_2[5].set_color(YELLOW)
        multi_eq_2[6].set_color(CYAN)
        multi_eq_2[7].set_color(WHITE)
        multi_eq_2[8].set_color(YELLOW)
        multi_eq_2[9].set_color(CYAN)
        multi_eq_2[10].set_color(WHITE)
        multi_eq_2[11].set_color(CORAL)

        self.play(
            ReplacementTransform(multi_eq_1, multi_eq_2),
            run_time=1.4,
        )
        self.wait(2)

        # Step 3C: y = β₁x₁ + β₂x₂ + ... + βₙxₙ + β₀
        multi_eq_3 = MathTex(
            "y", "=", "\\beta_1", "x_1", "+", "\\beta_2", "x_2", "+", "\\dots", "+", "\\beta_n", "x_n", "+", "\\beta_0",
            font_size=26
        ).move_to([-3.65, 0.4, 0])
        multi_eq_3[0].set_color(WHITE)
        multi_eq_3[1].set_color(WHITE)
        multi_eq_3[2].set_color(YELLOW)
        multi_eq_3[3].set_color(CYAN)
        multi_eq_3[4].set_color(WHITE)
        multi_eq_3[5].set_color(YELLOW)
        multi_eq_3[6].set_color(CYAN)
        multi_eq_3[7].set_color(WHITE)
        multi_eq_3[8].set_color(WHITE)   # dots
        multi_eq_3[9].set_color(WHITE)
        multi_eq_3[10].set_color(YELLOW) # beta_n
        multi_eq_3[11].set_color(CYAN)   # x_n
        multi_eq_3[12].set_color(WHITE)
        multi_eq_3[13].set_color(CORAL)  # beta_0

        self.play(
            ReplacementTransform(multi_eq_2, multi_eq_3),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Collapse into Summation Form: y = ∑ βᵢxᵢ + β₀
        # --------------------------------------------------
        sum_eq = MathTex(
            "y", "=", "\\sum_{i=1}^n", "\\beta_i", "x_i", "+", "\\beta_0",
            font_size=36
        ).move_to([-3.65, 0.4, 0])
        sum_eq[0].set_color(WHITE)
        sum_eq[1].set_color(WHITE)
        sum_eq[2].set_color(GREEN)   # summation
        sum_eq[3].set_color(YELLOW)  # beta_i
        sum_eq[4].set_color(CYAN)    # x_i
        sum_eq[5].set_color(WHITE)
        sum_eq[6].set_color(CORAL)   # beta_0

        model_subtitle = Text(
            "Multivariate Linear Model",
            font_size=20,
            color=LAVENDER
        ).next_to(sum_eq, DOWN, buff=0.45)

        self.play(
            ReplacementTransform(multi_eq_3, sum_eq),
            FadeIn(model_subtitle, shift=UP * 0.15),
            run_time=1.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Universality: Highlight the Gradient Descent Rule
        # --------------------------------------------------
        universal_note = MathTex(
            r"\text{Updates each } \beta \in \{\beta_0, \beta_1, \dots, \beta_n\}",
            font_size=21,
            color=GREEN
        ).next_to(single_rule_box, DOWN, buff=0.35)

        self.play(
            Indicate(single_rule_box, color=YELLOW, scale_factor=1.06),
            Indicate(beta_new_eq, color=WHITE, scale_factor=1.06),
            # FadeIn(universal_note, shift=UP * 0.15),
            run_time=1.6,
        )
        self.wait(2)

        

class scene12_generalization(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 11 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Left Side: Linear Model & Target Function
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 3.97", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        # Lower-left Target Function Badge
        target_title = Text(
            "Target Function",
            font_size=22,
            color=LAVENDER
        ).move_to([-4.1, -1.3, 0])

        target_eq = MathTex(
            "y", "=", "2", "x", "+", "1",
            font_size=38
        ).next_to(target_title, DOWN, buff=0.18)
        target_eq[0].set_color(WHITE)
        target_eq[1].set_color(WHITE)
        target_eq[2].set_color(YELLOW)  # m = 2
        target_eq[3].set_color(WHITE)
        target_eq[4].set_color(WHITE)
        target_eq[5].set_color(CORAL)   # c = 1

        target_badge = RoundedRectangle(
            corner_radius=0.15,
            width=3.6,
            height=1.45,
            color=PINK,
            stroke_width=1.6,
            fill_color=PANEL,
            fill_opacity=0.45,
        ).move_to(VGroup(target_title, target_eq).get_center())

        target_group = VGroup(target_badge, target_title, target_eq)

        left_side_group = VGroup(linear_title, eq_group, target_group)

        # --------------------------------------------------
        # 2. Right Side: Master Gradient Descent Rules (Partial Derivatives)
        # --------------------------------------------------
        c_target_pos = np.array([2.7, 0.85, 0])
        m_target_pos = np.array([2.7, -0.45, 0])

        rule_title = Text(
            "Gradient Descent Update Rule",
            font_size=23,
            color=GREEN
        ).move_to([2.7, 2.05, 0])

        c_new_partial = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial c}\\right)",
            font_size=34
        ).move_to(c_target_pos)
        c_new_partial[0].set_color(CORAL)
        c_new_partial[1].set_color(WHITE)
        c_new_partial[2].set_color(CORAL)
        c_new_partial[3].set_color(WHITE)
        c_new_partial[4].set_color(CYAN)
        c_new_partial[5].set_color(YELLOW)

        m_new_partial = MathTex(
            "m_{\\text{new}}", "=", "m_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial m}\\right)",
            font_size=34
        ).move_to(m_target_pos)
        m_new_partial[0].set_color(YELLOW)
        m_new_partial[1].set_color(WHITE)
        m_new_partial[2].set_color(YELLOW)
        m_new_partial[3].set_color(WHITE)
        m_new_partial[4].set_color(CYAN)
        m_new_partial[5].set_color(YELLOW)

        double_rule_box = RoundedRectangle(
            corner_radius=0.18,
            width=c_new_partial.width + 0.65,
            height=2.5,
            color=CYAN,
            stroke_width=2.2,
        ).move_to([2.7, 0.2, 0])

        right_side_group = VGroup(rule_title, double_rule_box, c_new_partial, m_new_partial)

        # --------------------------------------------------
        # Display Scene 11 Ending State
        # --------------------------------------------------
        self.add(
            left_side_group,
            right_side_group
        )
        self.wait(2)

        # ==================================================
        # SCENE 12 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. RSS Dependency: RSS term pulses in soft red
        # --------------------------------------------------
        self.play(
            Indicate(c_new_partial[5], color=SOFT_RED, scale_factor=1.18),
            Indicate(m_new_partial[5], color=SOFT_RED, scale_factor=1.18),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Learning Rate (eta) Pulse in Neon Pink
        # --------------------------------------------------
        self.play(
            Indicate(c_new_partial[4], color=PINK, scale_factor=1.35),
            Indicate(m_new_partial[4], color=PINK, scale_factor=1.35),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Clean Left Side & Rename m -> beta_1, c -> beta_0
        # --------------------------------------------------
        beta_eq = MathTex(
            "y", "=", "\\beta_1", "x", "+", "\\beta_0",
            font_size=44
        ).move_to([-4.1, 0.4, 0])
        beta_eq[0].set_color(WHITE)
        beta_eq[1].set_color(WHITE)
        beta_eq[2].set_color(YELLOW)  # beta_1
        beta_eq[3].set_color(WHITE)
        beta_eq[4].set_color(WHITE)
        beta_eq[5].set_color(CORAL)   # beta_0

        self.play(
            FadeOut(target_group, shift=DOWN * 0.4),
            FadeOut(linear_title),
            FadeOut(arrow_m),
            FadeOut(m_0),
            FadeOut(arrow_c),
            FadeOut(c_val_text),
            run_time=1.2,
        )
        self.play(
            ReplacementTransform(gen_eq, beta_eq),
            run_time=1.4,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Generalize Both Equations into Master Beta Update Rule
        # --------------------------------------------------
        beta_new_eq = MathTex(
            "\\beta_{\\text{new}}", "=", "\\beta_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial\\beta}\\right)",
            font_size=35
        ).move_to([2.7, 0.3, 0])
        beta_new_eq[0].set_color(PINK)
        beta_new_eq[1].set_color(WHITE)
        beta_new_eq[2].set_color(PINK)
        beta_new_eq[3].set_color(WHITE)
        beta_new_eq[4].set_color(CYAN)
        beta_new_eq[5].set_color(YELLOW)

        single_rule_box = RoundedRectangle(
            corner_radius=0.16,
            width=beta_new_eq.width + 0.65,
            height=beta_new_eq.height + 0.55,
            color=CYAN,
            stroke_width=2.2,
        ).move_to(beta_new_eq)

        self.play(
            rule_title.animate.move_to([2.7, 1.45, 0]),
            Transform(double_rule_box, single_rule_box),
            ReplacementTransform(c_new_partial, beta_new_eq),
            ReplacementTransform(m_new_partial, beta_new_eq),
            run_time=1.8,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Grand Finale: "Linear Regression" Title at Top Middle
        # --------------------------------------------------
        final_title = Text(
            "Linear Regression",
            font_size=42,
            weight=BOLD,
            color=CYAN
        ).move_to([0, 3.0, 0])

        underline = Line(
            start=final_title.get_left() + DOWN * 0.28,
            end=final_title.get_right() + DOWN * 0.28,
            color=PINK,
            stroke_width=2.5,
        )

        title_group = VGroup(final_title, underline)

        self.play(
            FadeIn(final_title, shift=DOWN * 0.25),
            Create(underline),
            run_time=1.4,
        )
        self.play(
            Indicate(final_title, color=YELLOW, scale_factor=1.05),
            run_time=1.2,
        )
        self.wait(2)


class scene11_gradient_descent(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 10 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Left Side: Title & Linear Model (m = 0, c = 3.97)
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 3.97", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        left_side_group = VGroup(linear_title, eq_group)

        # --------------------------------------------------
        # 2. Right Side: Master Gradient Descent Rule with Bounding Box
        # --------------------------------------------------
        c_new_eq = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "-", "\\eta", "\\left(\\frac{d\\text{RSS}}{dc}\\right)",
            font_size=34
        ).move_to([2.7, 0.3, 0])
        c_new_eq[0].set_color(CORAL)
        c_new_eq[1].set_color(WHITE)
        c_new_eq[2].set_color(CORAL)
        c_new_eq[3].set_color(WHITE)
        c_new_eq[4].set_color(CYAN)
        c_new_eq[5].set_color(YELLOW)

        rule_box = RoundedRectangle(
            corner_radius=0.15,
            width=c_new_eq.width + 0.6,
            height=c_new_eq.height + 0.45,
            color=CYAN,
            stroke_width=2.2,
        ).move_to(c_new_eq)

        # --------------------------------------------------
        # Display Scene 10 Ending State
        # --------------------------------------------------
        self.add(
            left_side_group,
            c_new_eq,
            rule_box
        )
        self.wait(2)

        # ==================================================
        # SCENE 11 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Label the equation: "Gradient Descent Update Rule"
        # --------------------------------------------------
        rule_title = Text(
            "Gradient Descent Update Rule",
            font_size=23,
            color=GREEN
        ).next_to(rule_box, UP, buff=0.35)

        self.play(
            FadeIn(rule_title, shift=DOWN * 0.15),
            run_time=1.0,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Recall the True Pattern in Lower Left: y = 2x + 1
        # --------------------------------------------------
        target_title = Text(
            "Target Function",
            font_size=22,
            color=LAVENDER
        ).move_to([-4.1, -1.3, 0])

        target_eq = MathTex(
            "y", "=", "2", "x", "+", "1",
            font_size=38
        ).next_to(target_title, DOWN, buff=0.18)
        target_eq[0].set_color(WHITE)
        target_eq[1].set_color(WHITE)
        target_eq[2].set_color(YELLOW)  # m = 2
        target_eq[3].set_color(WHITE)
        target_eq[4].set_color(WHITE)
        target_eq[5].set_color(CORAL)   # c = 1

        target_badge = RoundedRectangle(
            corner_radius=0.15,
            width=3.6,
            height=1.45,
            color=PINK,
            stroke_width=1.6,
            fill_color=PANEL,
            fill_opacity=0.45,
        ).move_to(VGroup(target_title, target_eq).get_center())

        target_group = VGroup(target_badge, target_title, target_eq)

        self.play(
            FadeIn(target_group, shift=UP * 0.3),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Discrepancy Highlight: c = 3.97 vs c = 1
        # --------------------------------------------------
        self.play(
            Indicate(c_val_text, color=SOFT_RED, scale_factor=1.15),
            Indicate(target_eq[5], color=CORAL, scale_factor=1.25),
            run_time=1.4,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Highlight m = 0 as the reason (Pulse Animation)
        # --------------------------------------------------
        self.play(
            m_0.animate.scale(1.3).set_color(PINK),
            arrow_m.animate.set_color(PINK),
            run_time=0.6,
        )
        self.play(
            m_0.animate.scale(1 / 1.3).set_color(YELLOW),
            arrow_m.animate.set_color(YELLOW),
            run_time=0.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Expand & Introduce Update Equation for m
        # --------------------------------------------------
        # Target positions for stacked equations
        c_target_pos = np.array([2.7, 0.85, 0])
        m_target_pos = np.array([2.7, -0.45, 0])

        m_new_eq = MathTex(
            "m_{\\text{new}}", "=", "m_{\\text{old}}", "-", "\\eta", "\\left(\\frac{d\\text{RSS}}{dm}\\right)",
            font_size=34
        ).move_to(m_target_pos)
        m_new_eq[0].set_color(YELLOW)
        m_new_eq[1].set_color(WHITE)
        m_new_eq[2].set_color(YELLOW)
        m_new_eq[3].set_color(WHITE)
        m_new_eq[4].set_color(CYAN)
        m_new_eq[5].set_color(YELLOW)

        # Expanded box covering both equations
        double_rule_box = RoundedRectangle(
            corner_radius=0.18,
            width=c_new_eq.width + 0.65,
            height=2.5,
            color=CYAN,
            stroke_width=2.2,
        ).move_to([2.7, 0.2, 0])

        self.play(
            rule_title.animate.move_to([2.7, 2.05, 0]),
            c_new_eq.animate.move_to(c_target_pos),
            Transform(rule_box, double_rule_box),
            FadeIn(m_new_eq, shift=UP * 0.3),
            run_time=1.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 6. Transform to Partial Derivatives (d -> ∂)
        # --------------------------------------------------
        c_new_partial = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial c}\\right)",
            font_size=34
        ).move_to(c_target_pos)
        c_new_partial[0].set_color(CORAL)
        c_new_partial[1].set_color(WHITE)
        c_new_partial[2].set_color(CORAL)
        c_new_partial[3].set_color(WHITE)
        c_new_partial[4].set_color(CYAN)
        c_new_partial[5].set_color(YELLOW)

        m_new_partial = MathTex(
            "m_{\\text{new}}", "=", "m_{\\text{old}}", "-", "\\eta", "\\left(\\frac{\\partial\\text{RSS}}{\\partial m}\\right)",
            font_size=34
        ).move_to(m_target_pos)
        m_new_partial[0].set_color(YELLOW)
        m_new_partial[1].set_color(WHITE)
        m_new_partial[2].set_color(YELLOW)
        m_new_partial[3].set_color(WHITE)
        m_new_partial[4].set_color(CYAN)
        m_new_partial[5].set_color(YELLOW)

        self.play(
            ReplacementTransform(c_new_eq, c_new_partial),
            ReplacementTransform(m_new_eq, m_new_partial),
            run_time=1.6,
        )
        self.wait(2)




class scene10_found(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 9 FINAL STATE (c = 3.97, -dRSS/dc = 0.2)
        # ==================================================

        # --------------------------------------------------
        # 1. Left Side: Title, Formulas & Negative Slope Readout
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 3.97", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        negetive_slope_title = Text("Negative Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])
        diff_text = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 0.2",
            font_size=28,
            color=YELLOW
        ).next_to(negetive_slope_title, DOWN, buff=0.25)

        # --------------------------------------------------
        # 2. Upper Formulas (Step Formula & Iteration 3 Calculation)
        # --------------------------------------------------
        step_formula = MathTex(
            r"\text{Step} = \text{Step Size} \times \left(-\frac{d\text{RSS}}{dc}\right)",
            font_size=24,
            color=CYAN
        ).move_to([2.7, 1.5, 0])

        step_calc_iter3 = MathTex(
            r"\text{Step} = 0.1 \times 1.12 \approx 0.11 \implies c = 3.97",
            font_size=21,
            color=YELLOW
        ).next_to(step_formula, DOWN, buff=0.18)

        # --------------------------------------------------
        # 3. Lower Graph (Dashed Curve, History Arcs, Ghosts & Active State at c = 3.97)
        # --------------------------------------------------
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
        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        solid_loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        dashed_loss_curve = DashedVMobject(
            solid_loss_curve,
            num_dashes=44,
            dashed_ratio=0.55
        ).set_color(CORAL).set_stroke(opacity=0.35)

        p0 = error_axes.c2p(0.5, calc_squared_error(0.5))
        p1 = error_axes.c2p(3.3, calc_squared_error(3.3))
        p2 = error_axes.c2p(3.86, calc_squared_error(3.86))
        p3 = error_axes.c2p(3.97, calc_squared_error(3.97))

        ghost_0 = Dot(p0, radius=0.08, color=CYAN, fill_opacity=0.35)
        ghost_1 = Dot(p1, radius=0.08, color=CYAN, fill_opacity=0.35)
        ghost_2 = Dot(p2, radius=0.08, color=CYAN, fill_opacity=0.35)
        ghost_dots = VGroup(ghost_0, ghost_1, ghost_2)

        arc_1 = CurvedArrow(
            p0,
            p1,
            angle=-PI / 3.4,
            color=CYAN,
            stroke_width=2.4,
            tip_length=0.15,
        )
        arc_2 = CurvedArrow(
            p1,
            p2,
            angle=-PI / 3.4,
            color=CYAN,
            stroke_width=2.4,
            tip_length=0.15,
        )
        arc_3 = CurvedArrow(
            p2,
            p3,
            angle=-PI / 3.4,
            color=GREEN,
            stroke_width=2.4,
            tip_length=0.15,
        )
        jump_arcs = VGroup(arc_1, arc_2, arc_3)

        c_axis_dot = Dot(
            error_axes.c2p(3.97, 0),
            radius=0.10,
            color=CORAL
        )

        eval_drop_line = DashedLine(
            error_axes.c2p(3.97, 0),
            p3,
            color=GREEN,
            stroke_width=2.2,
            dash_length=0.06
        )

        eval_ball = Dot(p3, radius=0.11, color=GREEN)

        def build_descent_arrow(c_val, length=1.0):
            pt = error_axes.c2p(c_val, calc_squared_error(c_val))
            slope = 8.0 * (c_val - 4.0)
            dc_val = 0.25
            if slope <= 0:
                p_fwd = error_axes.c2p(c_val + dc_val, calc_squared_error(c_val) + slope * dc_val)
            else:
                p_fwd = error_axes.c2p(c_val - dc_val, calc_squared_error(c_val) - slope * dc_val)
            v = p_fwd - pt
            norm_v = np.linalg.norm(v)
            u = v / norm_v if norm_v > 1e-6 else RIGHT
            return Arrow(
                start=pt - u * (length / 2),
                end=pt + u * (length / 2),
                color=WHITE,
                stroke_width=3.2,
                max_tip_length_to_length_ratio=0.18,
                buff=0,
            )

        arrow_active = build_descent_arrow(3.97, length=1.0)

        lower_graph = VGroup(
            error_axes, error_c_label, RSS2, origin_0,
            dashed_loss_curve, ghost_dots, jump_arcs,
            c_axis_dot, eval_drop_line, eval_ball, arrow_active
        )

        # --------------------------------------------------
        # Display Scene 9 Ending State
        # --------------------------------------------------
        self.add(
            linear_title,
            eq_group,
            negetive_slope_title,
            diff_text,
            step_formula,
            step_calc_iter3,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 10 ANIMATIONS
        # ==================================================

        # --------------------------------------------------
        # 1. Graph Merges into the Master Update Equation: c_new = c_old + Step
        # --------------------------------------------------
        c_new_eq1 = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "+", "\\text{Step}",
            font_size=32
        ).move_to([2.7, 0.6, 0])
        c_new_eq1[0].set_color(CORAL)
        c_new_eq1[1].set_color(WHITE)
        c_new_eq1[2].set_color(CORAL)
        c_new_eq1[3].set_color(WHITE)
        c_new_eq1[4].set_color(CYAN)

        self.play(
            FadeOut(lower_graph, scale=0.4, shift=UP * 1.5),
            ReplacementTransform(step_calc_iter3, c_new_eq1),
            run_time=1.8,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Step becomes Step Size * (Negative Slope) & absorbs top formula
        # --------------------------------------------------
        c_new_eq2 = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "+", "\\text{Step Size}", "\\times", "(\\text{Negative Slope})",
            font_size=26
        ).move_to([2.7, 0.6, 0])
        c_new_eq2[0].set_color(CORAL)
        c_new_eq2[1].set_color(WHITE)
        c_new_eq2[2].set_color(CORAL)
        c_new_eq2[3].set_color(WHITE)
        c_new_eq2[4].set_color(CYAN)
        c_new_eq2[5].set_color(WHITE)
        c_new_eq2[6].set_color(YELLOW)

        self.play(
            FadeOut(step_formula, shift=DOWN * 0.3),
            ReplacementTransform(c_new_eq1, c_new_eq2),
            run_time=1.5,
        )
        self.wait(2)

        # --------------------------------------------------
        # 3. Step Size becomes Learning Rate
        # --------------------------------------------------
        c_new_eq3 = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "+", "\\text{Learning Rate}", "\\times", "(\\text{Negative Slope})",
            font_size=25
        ).move_to([2.7, 0.6, 0])
        c_new_eq3[0].set_color(CORAL)
        c_new_eq3[1].set_color(WHITE)
        c_new_eq3[2].set_color(CORAL)
        c_new_eq3[3].set_color(WHITE)
        c_new_eq3[4].set_color(CYAN)
        c_new_eq3[5].set_color(WHITE)
        c_new_eq3[6].set_color(YELLOW)

        self.play(
            ReplacementTransform(c_new_eq2, c_new_eq3),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. Learning Rate becomes Greek Symbol eta (η)
        # --------------------------------------------------
        c_new_eq4 = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "+", "\\eta", "\\times", "(\\text{Negative Slope})",
            font_size=29
        ).move_to([2.7, 0.6, 0])
        c_new_eq4[0].set_color(CORAL)
        c_new_eq4[1].set_color(WHITE)
        c_new_eq4[2].set_color(CORAL)
        c_new_eq4[3].set_color(WHITE)
        c_new_eq4[4].set_color(CYAN)
        c_new_eq4[5].set_color(WHITE)
        c_new_eq4[6].set_color(YELLOW)

        self.play(
            ReplacementTransform(c_new_eq3, c_new_eq4),
            run_time=1.3,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Negative Slope becomes (-dRSS/dc) & lower-left slope disappears
        # --------------------------------------------------
        c_new_eq5 = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "+", "\\eta", "\\left(-\\frac{d\\text{RSS}}{dc}\\right)",
            font_size=31
        ).move_to([2.7, 0.6, 0])
        c_new_eq5[0].set_color(CORAL)
        c_new_eq5[1].set_color(WHITE)
        c_new_eq5[2].set_color(CORAL)
        c_new_eq5[3].set_color(WHITE)
        c_new_eq5[4].set_color(CYAN)
        c_new_eq5[5].set_color(YELLOW)

        self.play(
            FadeOut(negetive_slope_title, shift=RIGHT * 0.8),
            FadeOut(diff_text, shift=RIGHT * 0.8),
            ReplacementTransform(c_new_eq4, c_new_eq5),
            run_time=1.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 6. Final Canonical Gradient Descent Formula: c_new = c_old - η (dRSS/dc)
        # --------------------------------------------------
        c_new_eq6 = MathTex(
            "c_{\\text{new}}", "=", "c_{\\text{old}}", "-", "\\eta", "\\left(\\frac{d\\text{RSS}}{dc}\\right)",
            font_size=34
        ).move_to([2.7, 0.3, 0])
        c_new_eq6[0].set_color(CORAL)
        c_new_eq6[1].set_color(WHITE)
        c_new_eq6[2].set_color(CORAL)
        c_new_eq6[3].set_color(WHITE)
        c_new_eq6[4].set_color(CYAN)
        c_new_eq6[5].set_color(YELLOW)

        rule_title = Text(
            "Gradient Descent Update Rule",
            font_size=23,
            color=GREEN
        ).next_to(c_new_eq6, UP, buff=0.45)

        rule_box = RoundedRectangle(
            corner_radius=0.15,
            width=c_new_eq6.width + 0.6,
            height=c_new_eq6.height + 0.45,
            color=CYAN,
            stroke_width=2.2,
        ).move_to(c_new_eq6)

        self.play(
            ReplacementTransform(c_new_eq5, c_new_eq6),
            # c_new_eq6.animate.scale(1.5),
            run_time=1.4,
        )

        self.play(
            # FadeIn(rule_title, shift=DOWN * 0.15),
            Create(rule_box),
            run_time=1.2,
        )
        self.wait(2)


class scene9_way(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 8 FINAL STATE (c = 0.5, -dRSS/dc = 28)
        # ==================================================

        # --------------------------------------------------
        # 1. Left Side: Title, Formulas & Negative Slope Readout
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 0.5", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        negetive_slope_title = Text("Negative Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])
        neg_diff_val_text = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 28",
            font_size=28,
            color=YELLOW
        ).next_to(negetive_slope_title, DOWN, buff=0.25)

        # --------------------------------------------------
        # 2. Upper Callout ("Let's rethink this")
        # --------------------------------------------------
        rethink_text = Text(
            "Let's rethink this",
            font_size=28,
            color=CYAN
        ).move_to([2.7, 1.4, 0])

        # --------------------------------------------------
        # 3. Lower Graph (Dashed Parabola, Point, Drop Line, Descent Arrow at c = 0.5)
        # --------------------------------------------------
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
        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        solid_loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        dashed_loss_curve = DashedVMobject(
            solid_loss_curve,
            num_dashes=44,
            dashed_ratio=0.55
        ).set_color(CORAL).set_stroke(opacity=0.35)

        c_axis_dot = Dot(
            error_axes.c2p(0.5, 0),
            radius=0.10,
            color=CORAL
        )

        rss_at_05 = calc_squared_error(0.5)
        pt_on_curve = error_axes.c2p(0.5, rss_at_05)

        eval_drop_line = DashedLine(
            error_axes.c2p(0.5, 0),
            pt_on_curve,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )

        eval_ball = Dot(pt_on_curve, radius=0.11, color=CYAN)

        def build_descent_arrow(c_val, length=1.3):
            pt = error_axes.c2p(c_val, calc_squared_error(c_val))
            slope = 8.0 * (c_val - 4.0)
            dc_val = 0.25
            if slope <= 0:
                p_fwd = error_axes.c2p(c_val + dc_val, calc_squared_error(c_val) + slope * dc_val)
            else:
                p_fwd = error_axes.c2p(c_val - dc_val, calc_squared_error(c_val) - slope * dc_val)
            v = p_fwd - pt
            norm_v = np.linalg.norm(v)
            u = v / norm_v if norm_v > 1e-6 else RIGHT
            return Arrow(
                start=pt - u * (length / 2),
                end=pt + u * (length / 2),
                color=WHITE,
                stroke_width=3.2,
                max_tip_length_to_length_ratio=0.18,
                buff=0,
            )

        arrow_active = build_descent_arrow(0.5)

        lower_graph = VGroup(
            error_axes, error_c_label, RSS2, origin_0,
            dashed_loss_curve, c_axis_dot,
            eval_drop_line, eval_ball, arrow_active
        )

        # --------------------------------------------------
        # Display Scene 8 Ending State
        # --------------------------------------------------
        self.add(
            linear_title, eq_group, negetive_slope_title, neg_diff_val_text,
            rethink_text,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 9: PROPORTIONAL STEPPING & GRADIENT DESCENT
        # ==================================================

        # --------------------------------------------------
        # 1. Slope as a Guide (Pulse Negative Slope)
        # --------------------------------------------------
        self.play(
            Indicate(neg_diff_val_text, color=YELLOW, scale_factor=1.15),
            run_time=0.9,
        )
        self.wait(2)

        # --------------------------------------------------
        # 2. Introduce the Mathematical Formulation: Step = Step Size * (-dRSS/dc)
        # --------------------------------------------------
        step_formula = MathTex(
            r"\text{Step} = \text{Step Size} \times \text{Negative Slope}",
            font_size=24,
            color=CYAN
        ).move_to([2.7, 1.5, 0])

        self.play(
            ReplacementTransform(rethink_text, step_formula),
            run_time=0.8,
        )
        self.wait(2)

        

        self.play(
            ReplacementTransform(step_formula, MathTex(
                r"\text{Step} = \text{Step Size} \times \left(-\frac{d\text{RSS}}{dc}\right)",
                font_size=24,
                color=CYAN
            ).move_to(step_formula.get_center())
            ),
            run_time=0.8
        )

        # --------------------------------------------------
        # 3. Test Step Size = 1.0 (Overshoot Warning) vs Step Size = 0.1 (Tolerable)
        # --------------------------------------------------
        step_calc_1 = MathTex(
            r"\text{Step} = 1.0 \times 28 = 28 \quad",
            r"\text{(Too Big!)}",
            font_size=20,
        ).next_to(step_formula, DOWN, buff=0.18)
        step_calc_1[0].set_color(WHITE)
        step_calc_1[1].set_color(SOFT_RED)

        self.play(
            FadeIn(step_calc_1, shift=DOWN * 0.1),
            run_time=0.8,
        )
        self.wait(2)

        step_calc_01 = MathTex(
            r"\text{Step} = 0.1 \times 28 = 2.8 \quad",
            r"\text{(Tolerable!)}",
            font_size=20,
        ).move_to(step_calc_1.get_center())
        step_calc_01[0].set_color(WHITE)
        step_calc_01[1].set_color(GREEN)

        self.play(
            ReplacementTransform(step_calc_1, step_calc_01),
            run_time=0.8,
        )
        self.wait(2)

        # Transform into active step execution readout   
        active_step_calc = MathTex(
            r"\text{Step} = 0.1 \times 28 = 2.8 \implies c = 3.3",
            font_size=21,
            color=YELLOW
        ).move_to(step_calc_01.get_center())

        self.play(
            ReplacementTransform(step_calc_01, active_step_calc),
            run_time=0.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # 4. ITERATION 1: c = 0.5 -> c = 3.3 (Step = +2.8)
        # --------------------------------------------------
        p0 = error_axes.c2p(0.5, calc_squared_error(0.5))
        p1 = error_axes.c2p(3.3, calc_squared_error(3.3))

        ghost_0 = Dot(p0, radius=0.08, color=CYAN, fill_opacity=0.35)
        self.add(ghost_0)

        arc_1 = CurvedArrow(
            p0,
            p1,
            angle=-PI / 3.4,
            color=CYAN,
            stroke_width=2.4,
            tip_length=0.15,
        )

        drop_line_1 = DashedLine(
            error_axes.c2p(3.3, 0),
            p1,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )
        arrow_1 = build_descent_arrow(3.3)

        c_text_1 = MathTex("c = 3.3", font_size=32, color=CORAL).move_to(
            c_val_text.get_center()
        )
        diff_text_1 = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 5.6",
            font_size=28,
            color=YELLOW
        ).next_to(negetive_slope_title, DOWN, buff=0.25)

        self.play(
            Create(arc_1),
            c_axis_dot.animate.move_to(error_axes.c2p(3.3, 0)),
            eval_ball.animate.move_to(p1).set_color(CYAN),
            ReplacementTransform(eval_drop_line, drop_line_1),
            ReplacementTransform(arrow_active, arrow_1),
            ReplacementTransform(c_val_text, c_text_1),
            
            run_time=1.2,
            rate_func=rate_functions.ease_in_out_sine,
        )

        self.play(
            ReplacementTransform(neg_diff_val_text, diff_text_1),
        )

        eval_drop_line = drop_line_1
        arrow_active = arrow_1
        current_c_text = c_text_1
        current_diff_text = diff_text_1
        self.wait(2)

        # --------------------------------------------------
        # 5. ITERATION 2: c = 3.3 -> c = 3.86 (Step = 0.1 * 5.6 = +0.56)
        # --------------------------------------------------
        p2 = error_axes.c2p(3.86, calc_squared_error(3.86))

        ghost_1 = Dot(p1, radius=0.08, color=CYAN, fill_opacity=0.35)
        self.add(ghost_1)

        arc_2 = CurvedArrow(
            p1,
            p2,
            angle=-PI / 3.4,
            color=CYAN,
            stroke_width=2.4,
            tip_length=0.15,
        )

        step_calc_iter2 = MathTex(
            r"\text{Step} = 0.1 \times 5.6 = 0.56 \implies c = 3.86",
            font_size=21,
            color=YELLOW
        ).move_to(active_step_calc.get_center())

        drop_line_2 = DashedLine(
            error_axes.c2p(3.86, 0),
            p2,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )
        arrow_2 = build_descent_arrow(3.86)

        c_text_2 = MathTex("c = 3.86", font_size=32, color=CORAL).move_to(
            current_c_text.get_center()
        )
        diff_text_2 = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 1.1",
            font_size=28,
            color=YELLOW
        ).next_to(negetive_slope_title, DOWN, buff=0.25)

        self.play(
            ReplacementTransform(active_step_calc, step_calc_iter2),
            run_time=0.8
        )

        self.play(
            
            Create(arc_2),
            c_axis_dot.animate.move_to(error_axes.c2p(3.86, 0)),
            eval_ball.animate.move_to(p2).set_color(CYAN),
            ReplacementTransform(eval_drop_line, drop_line_2),
            ReplacementTransform(arrow_active, arrow_2),
            ReplacementTransform(current_c_text, c_text_2),
            
            run_time=1.2,
            rate_func=rate_functions.ease_in_out_sine,
        )

        self.play(
            ReplacementTransform(current_diff_text, diff_text_2),
            run_time=0.8 
        )

        eval_drop_line = drop_line_2
        arrow_active = arrow_2
        current_c_text = c_text_2
        current_diff_text = diff_text_2
        active_step_calc = step_calc_iter2
        self.wait(2)

        # --------------------------------------------------
        # 6. ITERATION 3: c = 3.86 -> c = 3.97 (Step = 0.1 * 1.12 = +0.11)
        # --------------------------------------------------
        p3 = error_axes.c2p(3.97, calc_squared_error(3.97))

        ghost_2 = Dot(p2, radius=0.08, color=CYAN, fill_opacity=0.35)
        self.add(ghost_2)

        arc_3 = CurvedArrow(
            p2,
            p3,
            angle=-PI / 3.4,
            color=GREEN,
            stroke_width=2.4,
            tip_length=0.15,
        )

        step_calc_iter3 = MathTex(
            r"\text{Step} = 0.1 \times 1.12 \approx 0.11 \implies c = 3.97",
            font_size=21,
            color=YELLOW
        ).move_to(active_step_calc.get_center())

        drop_line_3 = DashedLine(
            error_axes.c2p(3.97, 0),
            p3,
            color=GREEN,
            stroke_width=2.2,
            dash_length=0.06
        )
        arrow_3 = build_descent_arrow(3.97, length=1.0)

        c_text_3 = MathTex("c = 3.97", font_size=32, color=CORAL).move_to(
            current_c_text.get_center()
        )
        diff_text_3 = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 0.2",
            font_size=28,
            color=YELLOW
        ).next_to(negetive_slope_title, DOWN, buff=0.25)

        self.play(
            ReplacementTransform(active_step_calc, step_calc_iter3),
            run_time=0.8
        )

        self.play(
            
            Create(arc_3),
            c_axis_dot.animate.move_to(error_axes.c2p(3.97, 0)),
            eval_ball.animate.move_to(p3).set_color(GREEN),
            ReplacementTransform(eval_drop_line, drop_line_3),
            ReplacementTransform(arrow_active, arrow_3),
            ReplacementTransform(current_c_text, c_text_3),
            
            run_time=1.2,
            rate_func=rate_functions.ease_in_out_sine,
        )

        self.play(
            ReplacementTransform(current_diff_text, diff_text_3),
            run_time=0.8
        )

        eval_drop_line = drop_line_3
        arrow_active = arrow_3
        current_c_text = c_text_3
        current_diff_text = diff_text_3
        active_step_calc = step_calc_iter3

        # Convergence highlight
        self.play(
            Flash(
                p3,
                color=GREEN,
                flash_radius=0.40,
                line_length=0.15,
                num_lines=8,
            ),
            run_time=0.8,
        )

        self.wait(2)


        
class scene8_jump(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 7 FINAL STATE (c = 0.5, dRSS/dc = -28)
        # ==================================================

        # --------------------------------------------------
        # 1. Left Side: Title, Formulas & Derivative Readout
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 0.5", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        slope_title = Text("Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])
        diff_val_text = MathTex(
            r"\frac{d\text{RSS}}{dc} = -28",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        # --------------------------------------------------
        # 2. Lower Graph (Dashed Loss Curve, Point & Arrow at c = 0.5)
        # --------------------------------------------------
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
        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        solid_loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        dashed_loss_curve = DashedVMobject(
            solid_loss_curve,
            num_dashes=44,
            dashed_ratio=0.55
        ).set_color(CORAL).set_stroke(opacity=0.35)

        # Active elements at c = 0.5
        c_axis_dot = Dot(
            error_axes.c2p(0.5, 0),
            radius=0.10,
            color=CORAL
        )

        rss_at_05 = calc_squared_error(0.5)
        pt_on_curve = error_axes.c2p(0.5, rss_at_05)

        eval_drop_line = DashedLine(
            error_axes.c2p(0.5, 0),
            pt_on_curve,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )

        eval_ball = Dot(pt_on_curve, radius=0.11, color=CYAN)

        # Ascent arrow pointing Up-Left (from Scene 7)
        slope_at_05 = 8.0 * (0.5 - 4.0)  # -28.0
        dc = 0.25
        p_ahead = error_axes.c2p(0.5 - dc, rss_at_05 - slope_at_05 * dc)
        vec_ascent = p_ahead - pt_on_curve
        unit_vec_ascent = vec_ascent / np.linalg.norm(vec_ascent)

        length = 1.3
        arrow_active = Arrow(
            start=pt_on_curve - unit_vec_ascent * (length / 2),
            end=pt_on_curve + unit_vec_ascent * (length / 2),
            color=WHITE,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.18,
            buff=0,
        )

        lower_graph = VGroup(
            error_axes, error_c_label, RSS2, origin_0,
            dashed_loss_curve, c_axis_dot,
            eval_drop_line, eval_ball, arrow_active
        )

        # --------------------------------------------------
        # Display Scene 7 Final Ending State
        # --------------------------------------------------
        self.add(
            linear_title, eq_group, slope_title, diff_val_text,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 8: NEGATIVE SLOPE & DISCRETE JUMP EXPERIMENT
        # ==================================================

        # --------------------------------------------------
        # 1. Take Negative Slope: Flip equation & Flip Arrow to Descent
        # --------------------------------------------------
        neg_diff_val_text = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 28",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)


        ##### negetive slope
        negetive_slope_title = Text("Negative Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])

        # Arrow pointing Down-Right (Direction of Descent / Decreasing Error)
        p_ahead_descent = error_axes.c2p(0.5 + dc, rss_at_05 + slope_at_05 * dc)
        vec_descent = p_ahead_descent - pt_on_curve
        unit_vec_descent = vec_descent / np.linalg.norm(vec_descent)

        arrow_descent_05 = Arrow(
            start=pt_on_curve - unit_vec_descent * (length / 2),
            end=pt_on_curve + unit_vec_descent * (length / 2),
            color=WHITE,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.18,
            buff=0,
        )

        self.play(
            ReplacementTransform(diff_val_text, neg_diff_val_text),
            ReplacementTransform(arrow_active, arrow_descent_05),
            ReplacementTransform(slope_title, negetive_slope_title),
            run_time=1.0,
        )
        arrow_active = arrow_descent_05
        current_diff_text = neg_diff_val_text
        current_c_text = c_val_text
        self.wait(2)

        # --------------------------------------------------
        # Helper function to generate tangent arrow at any c
        # --------------------------------------------------
        def build_descent_arrow(c_val):
            pt = error_axes.c2p(c_val, calc_squared_error(c_val))
            slope = 8.0 * (c_val - 4.0)
            dc_val = 0.25

            # If slope <= 0 (c <= 4), stepping right decreases error -> point down-right
            # If slope > 0 (c > 4), stepping left decreases error -> point down-left
            if slope <= 0:
                p_fwd = error_axes.c2p(c_val + dc_val, calc_squared_error(c_val) + slope * dc_val)
            else:
                p_fwd = error_axes.c2p(c_val - dc_val, calc_squared_error(c_val) - slope * dc_val)

            v = p_fwd - pt
            u = v / np.linalg.norm(v)
            return Arrow(
                start=pt - u * (length / 2),
                end=pt + u * (length / 2),
                color=WHITE,
                stroke_width=3.2,
                max_tip_length_to_length_ratio=0.18,
                buff=0,
            )

        # --------------------------------------------------
        # 2. Sequential Discrete Jumps by Step Size = +1.0
        # --------------------------------------------------
        jump_sequence = [
            (0.5, 1.5, 20),
            (1.5, 2.5, 12),
            (2.5, 3.5, 4),
            (3.5, 4.5, -4),  # Overshoots minimum!
        ]

        ghost_dots = VGroup()
        jump_arcs = VGroup()

        for c_prev, c_curr, neg_grad_val in jump_sequence:
            p_prev = error_axes.c2p(c_prev, calc_squared_error(c_prev))
            p_curr = error_axes.c2p(c_curr, calc_squared_error(c_curr))

            # Faded ghost dot at previous location
            ghost = Dot(p_prev, radius=0.08, color=CYAN, fill_opacity=0.35)
            ghost_dots.add(ghost)
            self.add(ghost)

            # Curved Jump Arc
            arc = CurvedArrow(
                p_prev,
                p_curr,
                angle=-PI / 3.2,
                color=CYAN if c_curr <= 4.0 else CORAL,
                stroke_width=2.4,
                tip_length=0.15,
            )
            jump_arcs.add(arc)

            # Updated drop line, descent arrow, and labels
            new_drop_line = DashedLine(
                error_axes.c2p(c_curr, 0),
                p_curr,
                color=CYAN if c_curr <= 4.0 else CORAL,
                stroke_width=2.2,
                dash_length=0.06
            )
            new_arrow = build_descent_arrow(c_curr)

            new_c_text = MathTex(
                f"c = {c_curr}",
                font_size=32,
                color=CORAL
            ).move_to(current_c_text.get_center())

            new_diff_text = MathTex(
                rf"-\frac{{d\text{{RSS}}}}{{dc}} = {neg_grad_val}",
                font_size=28,
                color=YELLOW
            ).next_to(slope_title, DOWN, buff=0.25)

            # Animate the jump
            self.play(
                Create(arc),
                c_axis_dot.animate.move_to(error_axes.c2p(c_curr, 0)),
                eval_ball.animate.move_to(p_curr).set_color(CYAN if c_curr <= 4.0 else CORAL),
                ReplacementTransform(eval_drop_line, new_drop_line),
                ReplacementTransform(arrow_active, new_arrow),
                ReplacementTransform(current_c_text, new_c_text),
                ReplacementTransform(current_diff_text, new_diff_text),
                run_time=1.1,
                rate_func=rate_functions.ease_in_out_sine,
            )

            eval_drop_line = new_drop_line
            arrow_active = new_arrow
            current_c_text = new_c_text
            current_diff_text = new_diff_text
            self.wait(2)

        # --------------------------------------------------
        # 3. The Seesaw: Overshoot at c = 4.5 forces step backward to c = 3.5
        # --------------------------------------------------
        # Jump Back: 4.5 -> 3.5
        p_45 = error_axes.c2p(4.5, calc_squared_error(4.5))
        p_35 = error_axes.c2p(3.5, calc_squared_error(3.5))

        arc_back = CurvedArrow(
            p_45,
            p_35,
            angle=-PI / 3.0,
            color=CORAL,
            stroke_width=2.4,
            tip_length=0.15,
        )

        drop_line_35 = DashedLine(
            error_axes.c2p(3.5, 0),
            p_35,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )
        arrow_35 = build_descent_arrow(3.5)

        c_text_35 = MathTex("c = 3.5", font_size=32, color=CORAL).move_to(
            current_c_text.get_center()
        )
        diff_text_35 = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 4",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        self.play(
            Create(arc_back),
            c_axis_dot.animate.move_to(error_axes.c2p(3.5, 0)),
            eval_ball.animate.move_to(p_35).set_color(CYAN),
            ReplacementTransform(eval_drop_line, drop_line_35),
            ReplacementTransform(arrow_active, arrow_35),
            ReplacementTransform(current_c_text, c_text_35),
            ReplacementTransform(current_diff_text, diff_text_35),
            run_time=1.0,
            rate_func=rate_functions.ease_in_out_sine,
        )

        eval_drop_line = drop_line_35
        arrow_active = arrow_35
        current_c_text = c_text_35
        current_diff_text = diff_text_35
        self.wait(2)

        # Jump Forward Again: 3.5 -> 4.5 (Seesaw oscillation)
        arc_fwd_again = CurvedArrow(
            p_35,
            p_45,
            angle=-PI / 3.0,
            color=CORAL,
            stroke_width=2.4,
            tip_length=0.15,
        )

        drop_line_45 = DashedLine(
            error_axes.c2p(4.5, 0),
            p_45,
            color=CORAL,
            stroke_width=2.2,
            dash_length=0.06
        )
        arrow_45 = build_descent_arrow(4.5)

        c_text_45 = MathTex("c = 4.5", font_size=32, color=CORAL).move_to(
            current_c_text.get_center()
        )
        diff_text_45 = MathTex(
            r"-\frac{d\text{RSS}}{dc} = -4",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        self.play(
            Create(arc_fwd_again),
            c_axis_dot.animate.move_to(error_axes.c2p(4.5, 0)),
            eval_ball.animate.move_to(p_45).set_color(CORAL),
            ReplacementTransform(eval_drop_line, drop_line_45),
            ReplacementTransform(arrow_active, arrow_45),
            ReplacementTransform(current_c_text, c_text_45),
            ReplacementTransform(current_diff_text, diff_text_45),
            run_time=0.9,
            rate_func=rate_functions.ease_in_out_sine,
        )

        # Properly update references for the seesaw state
        eval_drop_line = drop_line_45
        arrow_active = arrow_45
        current_c_text = c_text_45
        current_diff_text = diff_text_45
        self.wait(2)

        # --------------------------------------------------
        # 4. Narrative Callout: "We might never reach the minimum RSS point"
        # --------------------------------------------------
        never_reach_text = Text(
            "We might never reach the minimum RSS point",
            font_size=24,
            color=CORAL
        ).move_to([2.7, 1.4, 0])

        self.play(
            FadeIn(never_reach_text, shift=UP * 0.2),
            run_time=0.8,
        )
        self.wait(2)

        # --------------------------------------------------
        # 5. Reset & Rethink: Transform text & return point to c = 0.5 (Clean Handover)
        # --------------------------------------------------
        rethink_text = Text(
            "Let's rethink this",
            font_size=28,
            color=CYAN
        ).move_to(never_reach_text.get_center())

        all_jump_artifacts = VGroup(ghost_dots, jump_arcs, arc_back, arc_fwd_again)

        c_text_05_final = MathTex("c = 0.5", font_size=32, color=CORAL).move_to(
            current_c_text.get_center()
        )
        diff_text_05_final = MathTex(
            r"-\frac{d\text{RSS}}{dc} = 28",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        reset_drop_line = DashedLine(
            error_axes.c2p(0.5, 0),
            pt_on_curve,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )
        reset_arrow = build_descent_arrow(0.5)

        self.play(
            ReplacementTransform(never_reach_text, rethink_text),
            FadeOut(all_jump_artifacts),
            c_axis_dot.animate.move_to(error_axes.c2p(0.5, 0)),
            eval_ball.animate.move_to(pt_on_curve).set_color(CYAN),
            ReplacementTransform(eval_drop_line, reset_drop_line),
            ReplacementTransform(arrow_active, reset_arrow),
            ReplacementTransform(current_c_text, c_text_05_final),
            ReplacementTransform(current_diff_text, diff_text_05_final),
            run_time=1.4,
            rate_func=rate_functions.ease_in_out_sine,
        )

        eval_drop_line = reset_drop_line
        arrow_active = reset_arrow
        current_c_text = c_text_05_final
        current_diff_text = diff_text_05_final

        self.wait(2)




class scene7_lost(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 6 FINAL STATE (c = 4.0, m = 0)
        # ==================================================

        # --------------------------------------------------
        # 1. Upper Plot (Axes, Labels, Points, Line, Squares at c = 4.0)
        # --------------------------------------------------
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

        points_data = [(0, 1), (1, 3), (2, 5), (3, 7)]
        dots = VGroup()
        tick_labels = VGroup()

        for x_val, y_val in points_data:
            pt_coords = axes.c2p(x_val, y_val)
            dot = Dot(pt_coords, radius=0.08, color=YELLOW)
            dots.add(dot)

            y_tick = MathTex(str(y_val), font_size=28, color=PINK).next_to(
                axes.c2p(0, y_val), LEFT, buff=0.12
            )
            tick_labels.add(y_tick)

            if x_val > 0:
                x_tick = MathTex(str(x_val), font_size=28, color=CYAN).next_to(
                    axes.c2p(x_val, 0), DOWN, buff=0.12
                )
                tick_labels.add(x_tick)
            else:
                x_tick = MathTex("0", font_size=28, color=CYAN).next_to(
                    axes.c2p(0, 0), DOWN + LEFT, buff=0.08
                )
                tick_labels.add(x_tick)

        top_group_static = VGroup(
            axes, x_axis_label, y_axis_label,
            dots, tick_labels
        )
        top_group_static.scale(0.58).move_to([2.7, 1.8, 0])

        c_val = 4.0
        test_line = axes.plot(
            lambda x: c_val,
            x_range=[0, 3.4],
            color=CORAL,
            stroke_width=2.5,
        )

        error_bars = VGroup(*[
            Line(
                axes.c2p(px, c_val),
                axes.c2p(px, py),
                color=YELLOW,
                stroke_width=2.4
            )
            for px, py in points_data
        ])

        error_squares = VGroup()
        for px, py in points_data:
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
                fill_opacity=0.22,
                stroke_width=1.8,
            )
            error_squares.add(sq)

        # --------------------------------------------------
        # 2. Left Side: Title, Formulas & Derivative Readout
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 4", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        slope_title = Text("Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])
        diff_val_text = MathTex(
            r"\frac{d\text{RSS}}{dc} = 0",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        # --------------------------------------------------
        # 3. Lower Graph (RSS vs c, Parabola, Ball, Tangent Arrow, Callout)
        # --------------------------------------------------
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
        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        min_center = error_axes.c2p(4.0, calc_squared_error(4.0))

        ball = Dot(min_center, radius=0.11, color=GREEN)
        drop_line = DashedLine(
            min_center,
            error_axes.c2p(4.0, 0),
            dash_length=0.06,
            color=GREEN,
            stroke_width=2.0
        )

        tangent_arrow = Arrow(
            start=min_center + LEFT * 0.6,
            end=min_center + RIGHT * 0.6,
            color=WHITE,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.18,
            buff=0,
        )

        diff_zero_label = MathTex(
            r"\frac{d\text{RSS}}{dc} = 0",
            font_size=26,
            color=GREEN
        ).move_to(min_center + UP * 0.85 + RIGHT * 0.3)

        diff_zero_arrow = Arrow(
            start=diff_zero_label.get_bottom(),
            end=min_center + UP * 0.12,
            color=GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            buff=0.08,
        )

        lower_graph = VGroup(
            error_axes, error_c_label, RSS2, origin_0,
            loss_curve, ball, drop_line, tangent_arrow,
            diff_zero_label, diff_zero_arrow
        )

        # --------------------------------------------------
        # Display Scene 6 Initial Ending State
        # --------------------------------------------------
        self.add(
            linear_title, eq_group, slope_title, diff_val_text,
            top_group_static, test_line, error_bars, error_squares,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 7: REALITY OF OPTIMIZATION — WE ARE "LOST"
        # ==================================================

        # --------------------------------------------------
        # STEP 1: Upper plot & solid curve disappear
        # In reality, we don't have visual guidance or the full curve
        # --------------------------------------------------
        dashed_loss_curve = DashedVMobject(
            loss_curve.copy(),
            num_dashes=44,
            dashed_ratio=0.55
        ).set_color(CORAL).set_stroke(opacity=0.35)

        self.play(
            FadeOut(top_group_static),
            FadeOut(test_line),
            FadeOut(error_bars),
            FadeOut(error_squares),
        )

        self.wait(2)

        self.play(
            FadeOut(diff_zero_label),
            FadeOut(diff_zero_arrow),
            FadeOut(tangent_arrow),
            FadeOut(ball),
        )

        self.wait(2)

        self.play(
            FadeOut(drop_line),
            ReplacementTransform(loss_curve, dashed_loss_curve),
        )

        self.wait(2)

        # --------------------------------------------------
        # STEP 2: We only control 'c' (exploration on the c-axis)
        # --------------------------------------------------
        diff_question = MathTex(
            r"\frac{d\text{RSS}}{dc} = \ ?",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        c_axis_dot = Dot(
            error_axes.c2p(4.0, 0),
            radius=0.10,
            color=CORAL
        )

        self.play(
            TransformMatchingShapes(diff_val_text, diff_question),
            FadeIn(c_axis_dot, scale=0.6),
            run_time=0.8,
        )

        self.wait(2)

        # Exploration sweep along the c-axis (sliding left and right)
        c_sweep_arrow = Arrow(
            start=error_axes.c2p(0.2, 0),
            end=error_axes.c2p(7.8, 0),
            color=WHITE,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.06,
            buff=0,
        ).shift(DOWN * 0.25)

        c_sweep_text = Text("Adjust c", font_size=20, color=LAVENDER).next_to(
            c_sweep_arrow, DOWN, buff=0.1
        )

        #######################

        c_new_text = MathTex("c = ?", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )


        self.play(
            c_axis_dot.animate.move_to(error_axes.c2p(0.5, 0)),
            TransformMatchingShapes(c_val_text, c_new_text),
            Create(c_sweep_arrow),
            FadeIn(c_sweep_text),
            run_time=1.0,
            rate_func=rate_functions.ease_in_out_sine,
        )

        self.wait(2)

        self.play(
            c_axis_dot.animate.move_to(error_axes.c2p(7.0, 0)),
            run_time=1.2,
            rate_func=rate_functions.ease_in_out_sine,
        )

        self.wait(2)

        # --------------------------------------------------
        # STEP 3: Where do we start? Let's pick c = 0.5
        # --------------------------------------------------
        c_05_text = MathTex("c = 0.5", font_size=32, color=CORAL).move_to(
            c_val_text.get_center()
        )

        self.play(
            c_axis_dot.animate.move_to(error_axes.c2p(0.5, 0)),
            TransformMatchingShapes(c_new_text, c_05_text),
            FadeOut(c_sweep_arrow),
            FadeOut(c_sweep_text),
            run_time=1.0,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # --------------------------------------------------
        # STEP 4: Calculate RSS at c = 0.5 (Line shoots up to curve)
        # --------------------------------------------------
        rss_at_05 = calc_squared_error(0.5)
        pt_on_curve = error_axes.c2p(0.5, rss_at_05)

        eval_drop_line = DashedLine(
            error_axes.c2p(0.5, 0),
            pt_on_curve,
            color=CYAN,
            stroke_width=2.2,
            dash_length=0.06
        )

        eval_ball = Dot(pt_on_curve, radius=0.11, color=CYAN)

        self.play(
            Create(eval_drop_line),
            run_time=0.8,
        )

        self.wait(2)
        self.play(
            FadeIn(eval_ball, scale=0.5),
            Flash(
                pt_on_curve,
                color=CYAN,
                flash_radius=0.35,
                line_length=0.14,
                num_lines=8
            ),
            run_time=0.6,
        )
        self.wait(2)

        # --------------------------------------------------
        # STEP 5: Calculate Slope at c = 0.5 -> dRSS/dc = -28
        # Arrow points in the direction of increasing RSS (upwards-left)
        # --------------------------------------------------
        slope_at_05 = 8.0 * (0.5 - 4.0)  # -28.0
        dc = 0.25
        p_ahead = error_axes.c2p(0.5 - dc, rss_at_05 - slope_at_05 * dc)
        vec = p_ahead - pt_on_curve
        unit_vec = vec / np.linalg.norm(vec)

        length = 1.3
        arrow_at_05 = Arrow(
            start=pt_on_curve - unit_vec * (length / 2),
            end=pt_on_curve + unit_vec * (length / 2),
            color=WHITE,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.18,
            buff=0,
        )

        diff_neg_28 = MathTex(
            r"\frac{d\text{RSS}}{dc} = -28",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        self.play(
            TransformMatchingShapes(diff_question, diff_neg_28),
            Create(arrow_at_05),
            run_time=1.0,
        )

        self.wait(2)




class scene6_intro_to_diff(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 5 FINAL STATE (c = 4.0, m = 0)
        # ==================================================

        # --------------------------------------------------
        # 1. Upper Plot (Axes, Labels, Points, Line, Squares at c = 4.0)
        # --------------------------------------------------
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

        points_data = [(0, 1), (1, 3), (2, 5), (3, 7)]
        dots = VGroup()
        tick_labels = VGroup()

        for x_val, y_val in points_data:
            pt_coords = axes.c2p(x_val, y_val)
            dot = Dot(pt_coords, radius=0.08, color=YELLOW)
            dots.add(dot)

            y_tick = MathTex(str(y_val), font_size=28, color=PINK).next_to(
                axes.c2p(0, y_val), LEFT, buff=0.12
            )
            tick_labels.add(y_tick)

            if x_val > 0:
                x_tick = MathTex(str(x_val), font_size=28, color=CYAN).next_to(
                    axes.c2p(x_val, 0), DOWN, buff=0.12
                )
                tick_labels.add(x_tick)
            else:
                x_tick = MathTex("0", font_size=28, color=CYAN).next_to(
                    axes.c2p(0, 0), DOWN + LEFT, buff=0.08
                )
                tick_labels.add(x_tick)

        top_group_static = VGroup(
            axes, x_axis_label, y_axis_label,
            dots, tick_labels
        )
        top_group_static.scale(0.58).move_to([2.7, 1.8, 0])

        c_init = 4.0
        test_line = axes.plot(
            lambda x: c_init,
            x_range=[0, 3.4],
            color=CORAL,
            stroke_width=2.5,
        )

        error_bars = VGroup(*[
            Line(
                axes.c2p(px, c_init),
                axes.c2p(px, py),
                color=YELLOW,
                stroke_width=2.4
            )
            for px, py in points_data
        ])

        error_squares = VGroup()
        for px, py in points_data:
            p_top = axes.c2p(px, py)
            p_bot = axes.c2p(px, c_init)
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
                fill_opacity=0.22,
                stroke_width=1.8,
            )
            error_squares.add(sq)

        # --------------------------------------------------
        # 2. Left Side: Title, Formulas & Slope Readout
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 4", font_size=32, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.25
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        slope_title = Text("Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])
        slope_val_text = MathTex(r"\text{slope} = 0", font_size=28, color=YELLOW).next_to(
            slope_title, DOWN, buff=0.25
        )

        # --------------------------------------------------
        # 3. Lower Graph (RSS vs c, Parabola, Ball, Tangent, Slope=0 Callout)
        # --------------------------------------------------
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
        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        ball = Dot(
            error_axes.c2p(4.0, calc_squared_error(4.0)),
            radius=0.11,
            color=GREEN
        )
        drop_line = DashedLine(
            error_axes.c2p(4.0, calc_squared_error(4.0)),
            error_axes.c2p(4.0, 0),
            dash_length=0.06,
            color=GREEN,
            stroke_width=2.0
        )

        tangent_center = error_axes.c2p(4.0, calc_squared_error(4.0))
        tangent_line = DashedLine(
            tangent_center + LEFT * 0.85,
            tangent_center + RIGHT * 0.85,
            dash_length=0.08,
            color=WHITE,
            stroke_width=3.2
        )

        slope_zero_label = MathTex(
            r"\text{Slope} = 0",
            font_size=26,
            color=GREEN
        ).move_to(tangent_center + UP * 0.85 + RIGHT * 0.3)

        slope_zero_arrow = Arrow(
            start=slope_zero_label.get_bottom(),
            end=tangent_center + UP * 0.12,
            color=GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            buff=0.08,
        )

        lower_graph = VGroup(
            error_axes, error_c_label, RSS2, origin_0,
            loss_curve, ball, drop_line, tangent_line,
            slope_zero_label, slope_zero_arrow
        )

        # --------------------------------------------------
        # Display Scene 5 Initial Ending State
        # --------------------------------------------------
        self.add(
            linear_title, eq_group, slope_title, slope_val_text,
            top_group_static, test_line, error_bars, error_squares,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 6: TRANSITION SLOPE TO DERIVATIVE & TANGENT ARROW
        # ==================================================

        # 1. Smoothly fade out Scene 5's static minimum callout
        self.play(
            FadeOut(slope_zero_label),
            FadeOut(slope_zero_arrow),
            run_time=0.5,
        )

        # 2. Transform "slope = 0" into "\frac{dRSS}{dc} = 0"
        diff_val_initial = MathTex(
            r"\frac{d\text{RSS}}{dc} = 0",
            font_size=28,
            color=YELLOW
        ).next_to(slope_title, DOWN, buff=0.25)

        # Initial static flat arrow at c = 4.0
        initial_arrow = Arrow(
            start=tangent_center + LEFT * 0.6,
            end=tangent_center + RIGHT * 0.6,
            color=WHITE,
            stroke_width=3.2,
            max_tip_length_to_length_ratio=0.18,
            buff=0,
        )

        # 3. Synchronized transformation: Text morphs & Tangent line morphs into Arrow
        self.play(
            TransformMatchingShapes(slope_val_text, diff_val_initial),
            run_time=0.8,
        )
        self.wait(2)

        self.play(
            ReplacementTransform(tangent_line, initial_arrow),
            run_time=0.8,
        )

        self.wait(2)
        # --------------------------------------------------
        # DYNAMIC SYSTEM SETUP (c_tracker & always_redraw)
        # --------------------------------------------------
        c_tracker = ValueTracker(4.0)

        # Dynamic Upper Squares
        def build_dynamic_squares():
            c_val = c_tracker.get_value()
            squares = VGroup()
            for px, py in points_data:
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
                    fill_opacity=0.22,
                    stroke_width=1.8,
                )
                squares.add(sq)
            return squares

        dyn_test_line = always_redraw(
            lambda: axes.plot(
                lambda x: c_tracker.get_value(),
                x_range=[0, 3.4],
                color=CORAL,
                stroke_width=2.5,
            )
        )
        dyn_error_bars = always_redraw(
            lambda: VGroup(*[
                Line(
                    axes.c2p(px, c_tracker.get_value()),
                    axes.c2p(px, py),
                    color=YELLOW,
                    stroke_width=2.4
                )
                for px, py in points_data
            ])
        )
        dyn_squares = always_redraw(build_dynamic_squares)

        # Dynamic c value label in y = mx + c
        dyn_c_val_text = always_redraw(
            lambda: MathTex(
                f"c = {c_tracker.get_value():.1f}"
                if abs(c_tracker.get_value() - round(c_tracker.get_value())) > 0.05
                else f"c = {int(round(c_tracker.get_value()))}",
                font_size=32,
                color=CORAL
            ).move_to(c_val_text.get_center())
        )

        # Dynamic Ball & Drop Line
        dyn_ball = always_redraw(
            lambda: Dot(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                radius=0.11,
                color=GREEN
            )
        )
        dyn_drop_line = always_redraw(
            lambda: DashedLine(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                error_axes.c2p(c_tracker.get_value(), 0),
                dash_length=0.06,
                color=GREEN,
                stroke_width=2.0
            )
        )

        # Dynamic Tangent ARROW pointing in the direction of increasing RSS
        def get_tangent_arrow(length=1.2):
            c = c_tracker.get_value()
            center = error_axes.c2p(c, calc_squared_error(c))
            slope_val = 8.0 * (c - 4.0)
            dc = 0.25

            # Arrow indicates direction where error increases (dRSS > 0)
            if slope_val >= 0:
                p_ahead = error_axes.c2p(c + dc, calc_squared_error(c) + slope_val * dc)
            else:
                p_ahead = error_axes.c2p(c - dc, calc_squared_error(c) - slope_val * dc)

            vec = p_ahead - center
            norm = np.linalg.norm(vec)
            unit_vec = vec / norm if norm > 1e-6 else RIGHT

            return Arrow(
                start=center - unit_vec * (length / 2),
                end=center + unit_vec * (length / 2),
                color=WHITE,
                stroke_width=3.2,
                max_tip_length_to_length_ratio=0.18,
                buff=0,
            )

        dyn_tangent_arrow = always_redraw(get_tangent_arrow)

        # Dynamic dRSS/dc readout under "Slope" title
        dyn_diff_val = always_redraw(
            lambda: MathTex(
                rf"\frac{{d\text{{RSS}}}}{{dc}} = {8.0 * (c_tracker.get_value() - 4.0):.1f}"
                if abs(8.0 * (c_tracker.get_value() - 4.0) - round(8.0 * (c_tracker.get_value() - 4.0))) > 0.05
                else rf"\frac{{d\text{{RSS}}}}{{dc}} = {int(round(8.0 * (c_tracker.get_value() - 4.0)))}",
                font_size=28,
                color=YELLOW
            ).next_to(slope_title, DOWN, buff=0.25)
        )

        # Seamless zero-flicker background handover to always_redraw system
        self.remove(
            test_line, error_bars, error_squares, c_val_text,
            ball, drop_line, initial_arrow, diff_val_initial
        )
        self.add(
            dyn_test_line, dyn_error_bars, dyn_squares, dyn_c_val_text,
            dyn_ball, dyn_drop_line, dyn_tangent_arrow, dyn_diff_val
        )

        self.wait(2)

        # --------------------------------------------------
        # OSCILLATION SEQUENCE WITH DERIVATIVE ARROW
        # --------------------------------------------------
        # 1. Roll to c = 0.5 (Steep Negative Derivative: dRSS/dc = -28, Arrow points Up-Left)
        self.play(
            c_tracker.animate.set_value(0.5),
            run_time=2.0,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # 2. Roll to c = 6.0 (Positive Derivative: dRSS/dc = +16, Arrow points Up-Right)
        self.play(
            c_tracker.animate.set_value(6.0),
            run_time=2.4,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # 3. Roll back to c = 3.0 (Negative Derivative: dRSS/dc = -8, Arrow points Up-Left)
        self.play(
            c_tracker.animate.set_value(3.0),
            run_time=1.8,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # 4. Roll to c = 5.0 (Positive Derivative: dRSS/dc = +8, Arrow points Up-Right)
        self.play(
            c_tracker.animate.set_value(5.0),
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # 5. Settle smoothly at c = 4.0 (Global Minimum: dRSS/dc = 0, Arrow horizontal/flat)
        self.play(
            c_tracker.animate.set_value(4.0),
            run_time=1.4,
            rate_func=rate_functions.ease_in_out_sine,
        )

        # --------------------------------------------------
        # HIGHLIGHT FINAL MINIMUM: dRSS/dc = 0
        # --------------------------------------------------
        min_center = error_axes.c2p(4.0, calc_squared_error(4.0))

        diff_zero_label = MathTex(
            r"\frac{d\text{RSS}}{dc} = 0",
            font_size=26,
            color=GREEN
        ).move_to(min_center + UP * 0.85 + RIGHT * 0.3)

        diff_zero_arrow = Arrow(
            start=diff_zero_label.get_bottom(),
            end=min_center + UP * 0.12,
            color=GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            buff=0.08,
        )

        self.play(
            Flash(
                min_center,
                color=GREEN,
                flash_radius=0.42,
                line_length=0.16,
                num_lines=8,
            ),
            Write(diff_zero_label),
            Create(diff_zero_arrow),
            run_time=1.0,
        )

        self.wait(2)




class scene5_slope(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 4 FINAL STATE (c = 4.0, m = 0)
        # ==================================================

        # --------------------------------------------------
        # 1. Upper Plot (Axes, Labels, Points)
        # --------------------------------------------------
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

        points_data = [(0, 1), (1, 3), (2, 5), (3, 7)]
        dots = VGroup()
        tick_labels = VGroup()

        for x_val, y_val in points_data:
            pt_coords = axes.c2p(x_val, y_val)
            dot = Dot(pt_coords, radius=0.08, color=YELLOW)
            dots.add(dot)

            y_tick = MathTex(str(y_val), font_size=28, color=PINK).next_to(
                axes.c2p(0, y_val), LEFT, buff=0.12
            )
            tick_labels.add(y_tick)

            if x_val > 0:
                x_tick = MathTex(str(x_val), font_size=28, color=CYAN).next_to(
                    axes.c2p(x_val, 0), DOWN, buff=0.12
                )
                tick_labels.add(x_tick)
            else:
                x_tick = MathTex("0", font_size=28, color=CYAN).next_to(
                    axes.c2p(0, 0), DOWN + LEFT, buff=0.08
                )
                tick_labels.add(x_tick)

        top_group_static = VGroup(
            axes, x_axis_label, y_axis_label,
            dots, tick_labels
        )
        top_group_static.scale(0.58).move_to([2.7, 1.8, 0])

        c_init = 4.0
        test_line = axes.plot(
            lambda x: c_init,
            x_range=[0, 3.4],
            color=CORAL,
            stroke_width=2.5,
        )

        error_bars = VGroup(*[
            Line(
                axes.c2p(px, c_init),
                axes.c2p(px, py),
                color=YELLOW,
                stroke_width=2.4
            )
            for px, py in points_data
        ])

        error_squares = VGroup()
        for px, py in points_data:
            p_top = axes.c2p(px, py)
            p_bot = axes.c2p(px, c_init)
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
                fill_opacity=0.22,
                stroke_width=1.8,
            )
            error_squares.add(sq)

        # --------------------------------------------------
        # 2. Left Side: Title and Formulas
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 4", font_size=38, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.3
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        # --------------------------------------------------
        # 3. Lower Graph (RSS vs c)
        # --------------------------------------------------
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
        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        origin_0 = MathTex("0", font_size=20, color=LAVENDER).next_to(
            error_axes.c2p(0, 0), DOWN + LEFT, buff=0.06
        )

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        # Initial Ball and Drop Line from Scene 4
        ball = Dot(
            error_axes.c2p(4.0, calc_squared_error(4.0)),
            radius=0.11,
            color=GREEN
        )
        drop_line = DashedLine(
            error_axes.c2p(4.0, calc_squared_error(4.0)),
            error_axes.c2p(4.0, 0),
            dash_length=0.06,
            color=GREEN,
            stroke_width=2.0
        )
        min_final_label = MathTex(r"\text{Min } (c=4)", font_size=22, color=GREEN).next_to(
            ball, DOWN, buff=0.12
        )

        lower_graph = VGroup(
            error_axes, error_c_label, RSS2, origin_0,
            loss_curve, ball, drop_line, min_final_label
        )

        # Add All Scene 4 Ending Elements
        self.add(
            linear_title, eq_group,
            top_group_static, test_line, error_bars, error_squares,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 5 TRANSITIONS: Introducing Slope
        # ==================================================

        # Fade out Scene 4's static minimum label
        self.play(FadeOut(min_final_label), run_time=0.6)

        # "slope" Title on the Left
        slope_title = Text("Slope", font_size=32, color=WHITE).move_to([-4.1, -1.8, 0])
        self.play(Write(slope_title), run_time=0.8)

        # --------------------------------------------------
        # SETUP DYNAMIC SYSTEM & TANGENT LINE
        # --------------------------------------------------
        self.remove(test_line, error_bars, error_squares, ball, drop_line)

        c_tracker = ValueTracker(0.5)

        # Dynamic squares helper
        def build_dynamic_squares():
            c_val = c_tracker.get_value()
            squares = VGroup()
            for px, py in points_data:
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
                    fill_opacity=0.22,
                    stroke_width=1.8,
                )
                squares.add(sq)
            return squares

        # Upper plot dynamic redraws
        dyn_test_line = always_redraw(
            lambda: axes.plot(
                lambda x: c_tracker.get_value(),
                x_range=[0, 3.4],
                color=CORAL,
                stroke_width=2.5,
            )
        )
        dyn_error_bars = always_redraw(
            lambda: VGroup(*[
                Line(
                    axes.c2p(px, c_tracker.get_value()),
                    axes.c2p(px, py),
                    color=YELLOW,
                    stroke_width=2.4
                )
                for px, py in points_data
            ])
        )
        dyn_squares = always_redraw(build_dynamic_squares)

        # Dynamic left c label
        dyn_c_val_text = always_redraw(
            lambda: MathTex(
                f"c = {c_tracker.get_value():.1f}" if abs(c_tracker.get_value() - round(c_tracker.get_value())) > 0.05 else f"c = {int(round(c_tracker.get_value()))}",
                font_size=32,
                color=CORAL
            ).move_to(c_val_text.get_center())
        )

        self.remove(c_val_text)
        self.add(dyn_test_line, dyn_error_bars, dyn_squares, dyn_c_val_text)

        # Dynamic Ball & Drop Line
        dyn_ball = always_redraw(
            lambda: Dot(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                radius=0.11,
                color=GREEN
            )
        )
        dyn_drop_line = always_redraw(
            lambda: DashedLine(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                error_axes.c2p(c_tracker.get_value(), 0),
                dash_length=0.06,
                color=GREEN,
                stroke_width=2.0
            )
        )

        # Dynamic Dashed Tangent Line at current c
        def get_tangent_line(length=1.7):
            c = c_tracker.get_value()
            center = error_axes.c2p(c, calc_squared_error(c))
            # d(RSS)/dc = 8 * (c - 4)
            slope_val = 8.0 * (c - 4.0)
            dc = 0.3
            p1 = error_axes.c2p(c - dc, calc_squared_error(c) - slope_val * dc)
            p2 = error_axes.c2p(c + dc, calc_squared_error(c) + slope_val * dc)
            vec = normalize(p2 - p1)
            return DashedLine(
                center - vec * length / 2,
                center + vec * length / 2,
                dash_length=0.08,
                color=WHITE,
                stroke_width=3.2
            )

        dyn_tangent = always_redraw(get_tangent_line)

        # Dynamic Slope Value display under "Slope" title
        dyn_slope_val = always_redraw(
            lambda: MathTex(
                rf"\text{{slope}} = {8.0 * (c_tracker.get_value() - 4.0):.1f}"
                if abs(8.0 * (c_tracker.get_value() - 4.0) - round(8.0 * (c_tracker.get_value() - 4.0))) > 0.05
                else rf"\text{{slope}} = {int(round(8.0 * (c_tracker.get_value() - 4.0)))}",
                font_size=28,
                color=YELLOW
            ).next_to(slope_title, DOWN, buff=0.25)
        )

        # Place at c = 0.5 initially
        self.play(
            FadeIn(dyn_ball),
            Create(dyn_drop_line),
            Create(dyn_tangent),
            Write(dyn_slope_val),
            run_time=1.0,
        )
        self.wait(2)

        # --------------------------------------------------
        # OSCILLATION SEQUENCE WITH TANGENT SLOPE
        # --------------------------------------------------
        # 1. Roll to c = 6.0 (Positive Slope)
        self.play(
            c_tracker.animate.set_value(6.0),
            run_time=2.2,
            rate_func=rate_functions.ease_in_out_sine,
        )
        # self.wait(2)

        # 2. Roll back to c = 3.0 (Negative Slope)
        self.play(
            c_tracker.animate.set_value(3.0),
            run_time=1.8,
            rate_func=rate_functions.ease_in_out_sine,
        )
        # self.wait(2)

        # 3. Roll to c = 5.0 (Positive Slope)
        self.play(
            c_tracker.animate.set_value(5.0),
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_sine,
        )
        # self.wait(2)

        # 4. Settle at c = 4.0 (Minimum, Flat Tangent: Slope = 0)
        self.play(
            c_tracker.animate.set_value(4.0),
            run_time=1.4,
            rate_func=rate_functions.ease_in_out_sine,
        )
        # self.wait(2)

        # --------------------------------------------------
        # HIGHLIGHT FINAL MINIMUM: Slope = 0
        # --------------------------------------------------
        tangent_center = error_axes.c2p(4.0, calc_squared_error(4.0))

        slope_zero_label = MathTex(
            r"\text{Slope} = 0",
            font_size=26,
            color=GREEN
        ).move_to(tangent_center + UP * 0.85 + RIGHT * 0.3)

        slope_zero_arrow = Arrow(
            start=slope_zero_label.get_bottom(),
            end=tangent_center + UP * 0.12,
            color=GREEN,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            buff=0.08,
        )

        self.play(
            Flash(
                tangent_center,
                color=GREEN,
                flash_radius=0.42,
                line_length=0.16,
                num_lines=8,
            ),
            Write(slope_zero_label),
            Create(slope_zero_arrow),
            run_time=1.0,
        )

        self.wait(2)

class scene4_predictibility(Scene):
    def construct(self):
        # ==================================================
        # RECONSTRUCT SCENE 3 FINAL STATE
        # ==================================================

        # --------------------------------------------------
        # 1. Upper Plot (Axes, Labels, Points)
        # --------------------------------------------------
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

        points_data = [(0, 1), (1, 3), (2, 5), (3, 7)]
        dots = VGroup()
        tick_labels = VGroup()

        for x_val, y_val in points_data:
            pt_coords = axes.c2p(x_val, y_val)
            dot = Dot(pt_coords, radius=0.08, color=YELLOW)
            dots.add(dot)

            y_tick = MathTex(str(y_val), font_size=28, color=PINK).next_to(
                axes.c2p(0, y_val), LEFT, buff=0.12
            )
            tick_labels.add(y_tick)

            if x_val > 0:
                x_tick = MathTex(str(x_val), font_size=28, color=CYAN).next_to(
                    axes.c2p(x_val, 0), DOWN, buff=0.12
                )
                tick_labels.add(x_tick)
            else:
                x_tick = MathTex("0", font_size=28, color=CYAN).next_to(
                    axes.c2p(0, 0), DOWN + LEFT, buff=0.08
                )
                tick_labels.add(x_tick)

        top_group_static = VGroup(
            axes, x_axis_label, y_axis_label,
            dots, tick_labels
        )
        top_group_static.scale(0.58).move_to([2.7, 1.8, 0])

        # Top line at initial c = 8.0
        c_final = 8.0
        test_line = axes.plot(
            lambda x: c_final,
            x_range=[0, 3.4],
            color=CORAL,
            stroke_width=2.5,
        )

        # Residual bars at c = 8.0
        error_bars = VGroup(*[
            Line(
                axes.c2p(px, c_final),
                axes.c2p(px, py),
                color=YELLOW,
                stroke_width=2.4
            )
            for px, py in points_data
        ])

        # Geometric Error Squares at c = 8.0
        error_squares = VGroup()
        for px, py in points_data:
            p_top = axes.c2p(px, py)
            p_bot = axes.c2p(px, c_final)
            side_len = abs(p_top[1] - p_bot[1])
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
                fill_opacity=0.22,
                stroke_width=1.8,
            )
            error_squares.add(sq)

        # --------------------------------------------------
        # 2. Left Side: Title and Formulas
        # --------------------------------------------------
        linear_title = Text(
            "Linear Relationship",
            font_size=32,
            color=CYAN
        ).scale(0.9).move_to([-4.1, 1.8, 0])

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
        m_0 = MathTex("m = 0", font_size=38, color=YELLOW).next_to(
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
        c_val_text = MathTex("c = 8", font_size=38, color=CORAL).next_to(
            arrow_c.get_end(), DOWN, buff=0.3
        )

        eq_group = VGroup(c_val_text, gen_eq, arrow_m, m_0, arrow_c)
        eq_group.scale(0.85).move_to([-4.1, 0.4, 0])

        # --------------------------------------------------
        # 3. Lower Graph (RSS vs c)
        # --------------------------------------------------
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

        def calc_squared_error(c):
            return (1 - c)**2 + (3 - c)**2 + (5 - c)**2 + (7 - c)**2

        # Fully drawn loss curve from c = 0 to 8
        loss_curve = error_axes.plot(
            calc_squared_error,
            x_range=[0, 8.0],
            color=CORAL,
            stroke_width=3.2,
        )

        milestone_dots = VGroup(*[
            Dot(error_axes.c2p(c, calc_squared_error(c)), radius=0.06, color=YELLOW)
            for c in range(9)
        ])
        err_dot = Dot(error_axes.c2p(8, calc_squared_error(8)), radius=0.07, color=CORAL)

        min_point = error_axes.c2p(4, 20)
        min_dot = Dot(min_point, radius=0.1, color=GREEN)
        min_label = MathTex(r"\text{Min } (c=4)", font_size=22, color=GREEN).next_to(
            min_dot, DOWN, buff=0.10
        )

        lower_graph = VGroup(
            error_axes, error_c_label, error_y_label, origin_0,
            loss_curve, milestone_dots, err_dot,
            min_dot, min_label
        )

        # Add All Scene 3 Ending Elements
        self.add(
            linear_title, eq_group,
            top_group_static, test_line, error_bars, error_squares,
            lower_graph
        )
        self.wait(2)

        # ==================================================
        # SCENE 4 TRANSITIONS
        # ==================================================

        # Label transforms: Total Error^2 -> Residual Sum of Squares -> RSS
        RSS = MathTex(r"\text{Residual Sum of Squares}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        self.play(ReplacementTransform(error_y_label, RSS))
        self.wait(2)

        RSS2 = MathTex(r"\text{RSS}", font_size=22, color=YELLOW).next_to(
            error_axes.y_axis.get_end(), UP, buff=0.12
        )
        self.play(ReplacementTransform(RSS, RSS2))
        self.wait(2)

        # --------------------------------------------------
        # CLEANUP LOWER GRAPH (Keep only axes & parabola curve)
        # --------------------------------------------------
        self.play(
            FadeOut(milestone_dots),
            FadeOut(err_dot),
            FadeOut(min_dot),
            FadeOut(min_label),
            run_time=0.8,
        )
        self.wait(2)

        # --------------------------------------------------
        # SETUP DYNAMIC SYSTEM AT c = 0.5
        # --------------------------------------------------
        self.remove(test_line, error_bars, error_squares)

        c_tracker = ValueTracker(0.5)

        # Helper to construct geometric squares dynamically
        def build_dynamic_squares():
            c_val = c_tracker.get_value()
            squares = VGroup()
            for px, py in points_data:
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
                    fill_opacity=0.22,
                    stroke_width=1.8,
                )
                squares.add(sq)
            return squares

        # Dynamic upper plot components
        dyn_test_line = always_redraw(
            lambda: axes.plot(
                lambda x: c_tracker.get_value(),
                x_range=[0, 3.4],
                color=CORAL,
                stroke_width=2.5,
            )
        )
        dyn_error_bars = always_redraw(
            lambda: VGroup(*[
                Line(
                    axes.c2p(px, c_tracker.get_value()),
                    axes.c2p(px, py),
                    color=YELLOW,
                    stroke_width=2.4
                )
                for px, py in points_data
            ])
        )
        dyn_squares = always_redraw(build_dynamic_squares)

        # Dynamic left formula c-label
        dyn_c_val_text = always_redraw(
            lambda: MathTex(
                f"c = {c_tracker.get_value():.1f}" if abs(c_tracker.get_value() - round(c_tracker.get_value())) > 0.05 else f"c = {int(round(c_tracker.get_value()))}",
                font_size=32,
                color=CORAL
            ).move_to(c_val_text.get_center())
        )

        self.remove(c_val_text)
        self.add(dyn_test_line, dyn_error_bars, dyn_squares, dyn_c_val_text)

        # --------------------------------------------------
        # INTRODUCE THE ROLLING BALL & DASHED DROP-LINE
        # --------------------------------------------------
        # Ball sits on the RSS curve at c_tracker
        ball = always_redraw(
            lambda: Dot(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                radius=0.11,
                color=GREEN
            )
        )

        # Dashed line dropping from ball down to c-axis
        drop_line = always_redraw(
            lambda: DashedLine(
                error_axes.c2p(c_tracker.get_value(), calc_squared_error(c_tracker.get_value())),
                error_axes.c2p(c_tracker.get_value(), 0),
                dash_length=0.06,
                color=GREEN,
                stroke_width=2.0
            )
        )

        self.play(
            FadeIn(ball, scale=1.5),
            Create(drop_line),
            run_time=1.0,
        )
        self.wait(2)

        # --------------------------------------------------
        # OSCILLATION & ROLLING SEQUENCE: 0.5 -> 6 -> 3 -> 5 -> 4
        # --------------------------------------------------
        # Roll 1: c = 0.5 -> 6.0
        self.play(
            c_tracker.animate.set_value(6.0),
            run_time=2.2,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # Roll 2: c = 6.0 -> 3.0
        self.play(
            c_tracker.animate.set_value(3.0),
            run_time=1.8,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # Roll 3: c = 3.0 -> 5.0
        self.play(
            c_tracker.animate.set_value(5.0),
            run_time=1.5,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # Roll 4: c = 5.0 -> 4.0 (Settle at the minimum)
        self.play(
            c_tracker.animate.set_value(4.0),
            run_time=1.4,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.wait(2)

        # --------------------------------------------------
        # HIGHLIGHT OPTIMAL SETTLED POINT (c = 4)
        # --------------------------------------------------
        min_settle_pos = error_axes.c2p(4.0, calc_squared_error(4.0))
        min_final_label = MathTex(r"\text{Min } (c=4)", font_size=22, color=GREEN).next_to(
            min_settle_pos, DOWN, buff=0.12
        )

        self.play(
            Flash(
                min_settle_pos,
                color=GREEN,
                flash_radius=0.42,
                line_length=0.16,
                num_lines=8,
            ),
            Write(min_final_label),
            run_time=1.0,
        )

        self.wait(2)


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

        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

        self.play(
            ReplacementTransform(err_calc_full, err_res_16),
            run_time=0.8,
        )
        self.wait(2)

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
        self.wait(2)

        self.play(c_tracker.animate.set_value(3.0), run_time=1.6, rate_func=smooth)
        self.wait(2)

        self.play(c_tracker.animate.set_value(8.0), run_time=1.8, rate_func=smooth)
        self.wait(2)

        self.play(c_tracker.animate.set_value(0.0), run_time=1.6, rate_func=smooth)
        self.wait(2)

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

        self.wait(2)

        self.play(
            
            Write(err_sq_label),
            Create(err_sq_arrow),
            run_time=1.0,
        )
        self.wait(2)


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
        self.wait(2)

        self.play(
            ReplacementTransform(err_sq_calc_full, err_sq_res_84),
            run_time=0.8,
        )
        self.wait(2)

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
        self.wait(2)

        self.play(c_tracker.animate.set_value(3.0), run_time=1.6, rate_func=smooth)
        self.wait(2)

        self.play(c_tracker.animate.set_value(8.0), run_time=1.8, rate_func=smooth)
        self.wait(2)

        self.play(c_tracker.animate.set_value(0.0), run_time=1.6, rate_func=smooth)
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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

        self.wait(2)


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
        self.wait(2)

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
        self.wait()

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
        # self.wait(2)

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
        self.wait(2)

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

        self.wait(.5)
        
        self.play(
            Create(projections[0]),  # v_line 1
            Create(projections[1]),  # h_line 1
            FadeIn(dots[1], scale=1.5),
            Write(tick_labels[2]),  # y=3
            Write(tick_labels[3]),  # x=1
            run_time=0.9,
        )
        self.wait(.5)

        # Panel 6: Point (2,5)
        self.play(
            Create(projections[2]),
            Create(projections[3]),
            FadeIn(dots[2], scale=1.5),
            Write(tick_labels[4]),  # y=5
            Write(tick_labels[5]),  # x=2
            run_time=0.9,
        )
        self.wait(.5)

        # Panel 7: Point (3,7)
        self.play(
            Create(projections[4]),
            Create(projections[5]),
            FadeIn(dots[3], scale=1.5),
            Write(tick_labels[6]),  # y=7
            Write(tick_labels[7]),  # x=3
            run_time=0.9,
        )
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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
        self.wait(2)

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

        self.wait(2)


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

        self.wait(.7)

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

        self.wait(.7)

        # ==================================
        # STEP 3
        # Add 1 -> 3
        # ==================================

        row_1 = make_row(1, 3, 1)

        reveal_row(row_1)

        self.wait(.7)

        # ==================================
        # STEP 4
        # Add 2 -> 5
        # ==================================

        row_2 = make_row(2, 5, 2)

        reveal_row(row_2)

        self.wait(.7)

        # ==================================
        # STEP 5
        # Hold the completed table
        # ==================================

        self.wait(.7)

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

        self.wait(2)

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

        self.wait(2)

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

        self.wait(2)

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

        self.wait(2)

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

        self.wait(2)

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

        self.wait(2)

        self.play(
            ReplacementTransform(
                substitution_1,
                substitution_2
            ),
            run_time=1
        )

        self.wait(2)

        self.play(
            ReplacementTransform(
                substitution_2,
                substitution_3
            ),
            run_time=1
        )

        self.wait(2)

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

        self.wait(2)


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
        self.wait(2)

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

        self.wait(2)

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

        self.wait(2)

