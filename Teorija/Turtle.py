import turtle


t = turtle.Turtle()
t.speed(0)


def print_square(size, center=(0, 0)):
    t.penup()
    x, y = center
    x -= size / 2
    y += size / 2
    t.setpos(x, y)
    t.pendown()
    x += size
    t.setpos(x, y)
    y -= size
    t.setpos(x, y)
    x -= size
    t.setpos(x, y)
    y += size
    t.setpos(x, y)


def done():
    turtle.done()
