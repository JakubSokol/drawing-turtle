import turtle
from random import randint, choice, uniform, shuffle, seed
from time import sleep


class Shape:
    def __init__(self, anchor, angle, fillcolor, bordersize, bordercolor):
        self.anchor = anchor
        self.angle = angle
        self.fillcolor = fillcolor
        self.bordersize = bordersize
        self.bordercolor = bordercolor

    def draw(self):
        self.setup()
        if self.fillcolor:
            turtle.fillcolor(self.fillcolor)
            turtle.begin_fill()
            self.draw_style()
            turtle.end_fill()
        else:
            self.draw_style()

    def draw_style(self):
        raise NotImplementedError

    def setup(self):
        turtle.right(turtle.heading())
        turtle.penup()
        turtle.goto(self.anchor[0], self.anchor[1])
        turtle.pendown()
        turtle.left(self.angle)
        turtle.pencolor(self.bordercolor)
        turtle.width(self.bordersize)


class Rectangle(Shape):
    def __init__(self, anchor, angle, fillcolor, bordersize, bordercolor, lenx, leny):
        super().__init__(anchor, angle, fillcolor, bordersize, bordercolor)
        self.lenx = lenx
        self.leny = leny

    def draw_style(self):
        for x in range(0, 2):
            turtle.forward(self.lenx)
            turtle.left(90)
            turtle.forward(self.leny)
            turtle.left(90)


class Pentagon(Shape):
    def __init__(self, anchor, angle, fillcolor, bordersize, bordercolor, pen_len):
        super().__init__(anchor, angle, fillcolor, bordersize, bordercolor)
        self.pen_len = pen_len

    def draw_style(self):
        for x in range(0, 5):
            turtle.forward(self.pen_len)
            turtle.left(72)


class Octagon(Shape):
    def __init__(self, anchor, angle, fillcolor, bordersize, bordercolor, oct_len):
        super().__init__(anchor, angle, fillcolor, bordersize, bordercolor)
        self.oct_len = oct_len

    def draw_style(self):
        for x in range(0, 8):
            turtle.forward(self.oct_len)
            turtle.left(45)


class Heart(Shape):
    def __init__(self, anchor, angle, fillcolor, bordersize, bordercolor, heart_len):
        super().__init__(anchor, angle, fillcolor, bordersize, bordercolor)
        self.heart_len = heart_len

    def draw_style(self):
        turtle.left(45)
        turtle.forward(self.heart_len)
        turtle.circle(self.heart_len / 2, 180)
        turtle.right(90)
        turtle.circle(self.heart_len / 2, 180)
        turtle.forward(self.heart_len)


class Semicircle(Shape):
    def __init__(self, anchor, angle, fillcolor, bordersize, bordercolor, semi_rad):
        super().__init__(anchor, angle, fillcolor, bordersize, bordercolor)
        self.semi_rad = semi_rad

    def draw_style(self):
        turtle.left(90)
        turtle.circle(self.semi_rad, 180)
        turtle.left(90)
        turtle.forward(self.semi_rad * 2)


def myname():
    turtle.penup()
    turtle.goto(330, 300)
    turtle.pendown()
    turtle.write("Jakub Sokol  ZZIAS1-1112", align="right", font=("Arial", 15))
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def random_color():
    return (uniform(0, 1), uniform(0, 1), uniform(0, 1))


def random_fillcolor():
    is_fill = choice([True, False])
    if is_fill:
        return random_color()
    else:
        return None


if __name__ == "__main__":
    seed(42)
    turtle.speed(0)
    turtle.bgcolor("lightgrey")
    figures = []
    for i in range(0, 10):
        figures.append(
            Rectangle(
                [randint(-300, 300), randint(-250, 250)],
                randint(0, 359),
                random_fillcolor(),
                randint(0, 10),
                random_color(),
                randint(0, 100),
                randint(0, 150),
            )
        )
    for shape in [Pentagon, Heart, Octagon, Semicircle]:
        for i in range(0, 10):
            figures.append(
                shape(
                    [randint(-200, 200), randint(-200, 200)],
                    randint(0, 359),
                    random_fillcolor(),
                    randint(0, 10),
                    random_color(),
                    randint(0, 100),
                )
            )
    myname()
    shuffle(figures)
    for shape in figures:
        shape.draw()
    sleep(5)
