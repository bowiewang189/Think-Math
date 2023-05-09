import numpy as np
from manim import *
import math


def createGraph(ax, a, b, c):
    graph_ = ax.plot_implicit_curve(
        lambda x, y: x/a + x**2/b + x**3/c - y, color=RED
    )
    return graph_

class DrawEauqtionGrap(Scene):
    def construct(self):
        ax = Axes()
        a1 = ax.plot_implicit_curve(
            lambda x, y: x**2 + (5*y/4 - np.sqrt(np.abs(x)))**2 - 1, color=RED
        )
        a1.scale(2)
        self.play(FadeIn(ax))
        self.play(Create(a1))
        self.wait(2)
        self.play(FadeOut(a1))
        self.wait(2)

        """
        graph219 = createGraph(ax, 2, 1, 9).scale(2)
        self.play(Create(graph219))
        self.wait(2)
        self.play(FadeOut(graph219))
        self.wait(2)
        
        
        
        a3 = ax.plot_implicit_curve(
            lambda x, y: np.sin((y**2) * (x**3)) - np.cos((y**3) * (x**2)), color=RED
        )
        self.play(Create(a3))
        self.wait(2)
        self.play(FadeOut(a3))
        self.wait(2)
        
        """
        a2 = ax.plot_implicit_curve(
            lambda x, y: x * np.sin(1 / x) - y, color=RED
        )
        self.play(Create(a2))
        self.wait(2)
        self.play(FadeOut(a2))
        self.wait(2)

        a3 = ax.plot_implicit_curve(
            lambda x, y: np.sin(np.cos(np.tan(x*y))) - np.sin(np.cos(np.tan(x))) - np.sin(np.cos(np.tan(y))), color=RED
        )
        self.play(Create(a3))
        self.wait(2)
        self.play(FadeOut(a3))
        self.wait(2)

        self.play(FadeOut(ax))
        ax.remove()
        ax = Axes()

        a4 = ax.plot_implicit_curve(
            lambda x, y: y - np.sin(x**np.cos(y)), color=RED
        )
        self.play(FadeIn(ax))
        self.play(Create(a4))
        self.wait(2)
        self.play(FadeOut(a4))
        self.wait(2)

class DarkThemeBanner(Scene):
    def construct(self):
        banner = MarkupText('<span foreground="White" size="x-large">Think-Math</span>')
        self.play(Create(banner))
        self.wait()


class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func.animate, sin_func_1, sin_func_2)

class CoordSysExample(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[0, 1, 0.05],  # step size determines num_decimal_places.
            y_range=[0, 1, 0.05],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": np.arange(0, 1 + 0.1, 0.1),
                "font_size": 24,
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = grid.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)

        graphs = VGroup()
        for n in np.arange(1, 20 + 0.5, 0.5):
            graphs += grid.plot(lambda x: x ** n, color=WHITE)
            graphs += grid.plot(
                lambda x: x ** (1 / n), color=WHITE, use_smoothing=False
            )

        # Extra lines and labels for point (1,1)
        graphs += grid.get_horizontal_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += grid.get_vertical_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += Dot(point=grid.c2p(1, 1, 0), color=YELLOW)
        graphs += Tex("(1,1)").scale(0.75).next_to(grid.c2p(1, 1, 0))
        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Graphs of $y=x^{ {1}\over{n} }$ and $y=x^n (n=1,2,3,...,20)$",
            include_underline=False,
            font_size=40,
        )

        self.add(title, graphs, grid, grid_labels)

