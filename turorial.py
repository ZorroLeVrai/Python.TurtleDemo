import turtle
import random

MIN_SCREEN = -300
MAX_SCREEN = 300


class Samples:
    def __init__(self, turtle):
        self.turtle = turtle

    def draw_right_angle(self: object, color: str, length: int) -> None:
        self.turtle.color(color)
        self.turtle.forward(length)
        self.turtle.left(90)
        self.turtle.forward(length)

    def draw_square(self: object, color: str, size: int) -> None:
        self.turtle.color(color)

        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(size)
            self.turtle.left(90)
        self.turtle.end_fill()

    def draw_star(self: object, size: int) -> None:
        for _ in range(5):
            self.turtle.forward(size)
            self.turtle.left(216)

    def draw_complexe_star(self: object, x: int, y: int) -> None:
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.color("red", "yellow")
        self.turtle.begin_fill()

        for _ in range(36):
            self.turtle.forward(150)
            self.turtle.left(170)

        self.turtle.end_fill()

    def fancy_spiral(self):
        colors = ["red", "yellow", "green", "blue", "purple", "orange"]
        self.turtle.speed(500)
        turtle.bgcolor("black")

        for x in range(360):
            self.turtle.pencolor(colors[x % 6])
            self.turtle.width(x // 100 + 1)
            self.turtle.forward(x)
            self.turtle.left(59)

    def draw_interconnected_line(self: object, color: str, length: int, nb_steps: int = 10) -> None:
        self.turtle.color(color)
        cur = 0
        step = length / (2*10+1.0)
        isPenDown = True

        while cur + step < length:
            cur += step
            if isPenDown:
                self.turtle.pendown()
            else:
                self.turtle.penup()
            self.turtle.forward(step)
            isPenDown = not isPenDown
        
        self.turtle.forward(length - cur)

    def color_background(self: object, color: str):
        self.turtle.getscreen().bgcolor(color)


def generate_random_stars(turtle: object, outline_color: str, fill_color: str, nb: int) -> None:
    sample = Samples(turtle)
    turtle.color(outline_color, fill_color)

    for _ in range(nb):
        x = random.randint(MIN_SCREEN, MAX_SCREEN)
        y = random.randint(MIN_SCREEN, MAX_SCREEN)

        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        sample.draw_star(random.randint(5, 25))
        turtle.end_fill()

def register_use_shape():
    # register square shape
    turtle.begin_poly()
    turtle.color("white")
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_poly()
    turtle.register_shape("Square", turtle.get_poly())

    turtle.goto(-200, -200)
    # use square shape
    turtle.shape("Square")

t = turtle.Turtle()

#set the speed for drawing
t.speed(200)
sample_draw = Samples(t)
sample_draw.color_background("#000000")

# set absolute direction
t.setheading(90)

# clear screen
t.clear()

sample_draw.fancy_spiral()

#bound the click to the goto function
t.getscreen().onclick(sample_draw.draw_complexe_star)

turtle.done()