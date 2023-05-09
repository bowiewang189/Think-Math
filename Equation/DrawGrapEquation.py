from manim import *

class Formula(Scene):
    def construct(self):
        #t = MathTex(r"sin^{2}(xy) = cos^{2}(xy)").scale(3)
        #t = MathTex(r"y^{\cos y}=110\ x^{\sin x}").scale(3)
        t = MathTex(r"y\ =\ xe^{\sin xy}").scale(3)
        # t.shift(UP * 2)
        # t2 = MathTex('a^2 + b^2 = c^2')
        # t2.shift(UP * 1)
        # t3 = MathTex("A = \\sqrt{(C + B)(C - B)}")
        # t4 = MathTex('\\sqrt[3]{x} = \\sqrt[4]{y}')
        # t4.shift(DOWN * 1)
        # t5 = MathTex('sin(2\\pi f_j t_i) e^{123}')
        # t5.shift(DOWN * 2)
        # t6 = MathTex('\\frac{3}{4}')
        # t6.shift(DOWN * 3)
        # t7 = Tex('The horse does not eat cucumber salad.')
        # t3.next_to(t7, LEFT)
        self.add(t)

class TextItalicAndBoldExample(Scene):
    def construct(self):
        text1 = Text("Think-Math",  weight=BOLD).scale(2)
        text1.shift(UP * 0.5)
        text2 = Text("Visit us at Think-Math.com, "
                     "or contact Email 3645bug@gmail.com",
                     t2c={"Think-Math.com": RED, "3645bug@gmail.com": RED}).scale(0.6)
        text2.shift(DOWN * 2)
        self.play(Create(text1), Create(text2))
        self.wait(3)
        #Group(*self.mobjects).arrange(DOWN, buff=.8).set_height(config.frame_height-LARGE_BUFF)

class TextEnd(Scene):
    def construct(self):
        text1 = Text("Thanks for your watching",  weight=BOLD).scale(1)
        #text1.shift(UP * 1)
        text2 = Text("Appreciate your subscription", weight=BOLD,t2c={"subscription": RED}).scale(1)
        text2.shift(DOWN * 1)
        self.play(Create(text1), Create(text2))
        self.wait(2)
        #Group(*self.mobjects).arrange(DOWN, buff=.8).set_height(config.frame_height-LARGE_BUFF)

class briefSummary(Scene):
    def construct(self):
        text1 = Text("In this video, I create a few graphs based on math formula", t2c={"graphs": RED, "formula": RED}).scale(0.6)
        text1.shift(UP * 1)
        text2 = Text("Tools are including python3, Manim, desmos and ffmpeg").scale(0.6)
        text3 = Text("Auther : Think-Math.com").scale(0.6)
        text3.shift(DOWN * 2)
        self.add(text1, text2, text3)
        self.wait(5)
        #Group(*self.mobjects).arrange(DOWN, buff=.8).set_height(config.frame_height-LARGE_BUFF)