import turtle

def get_color(index: int) -> (int, int, int):
    def get_max(idx, m_lst):
        for max_value in m_lst:
            distance_to_max = abs(idx - max_value)
            if distance_to_max < 255:
                return 255 - distance_to_max
        return 0
    
    considered_index = index % 765
    red = get_max(considered_index, [0, 765])
    green = get_max(considered_index, [255])
    blue = get_max(considered_index, [510])
    return (red, green, blue)

def square_spiral(turtle: object, length: float, side_bar: float, nb_iteration: int, show_numbers: bool = False):
    xTarget, yTarget = length, 0
    for i in range(nb_iteration):
        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        turtle.setheading(t.towards(xTarget, yTarget))
        turtle.goto(xTarget, yTarget)
        if show_numbers:
            turtle.write(i+1)
        turtle.left(90)
        t.forward(side_bar)
        xTarget, yTarget = t.pos()

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.getscreen().colormode(255)
print(t.getscreen().colormode())
t.speed(1000)
t.hideturtle()
t.pencolor("white")
square_spiral(t, 20, 20, 250, True)
t.showturtle()

turtle.done()