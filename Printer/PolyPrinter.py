import turtle

letter_size = (4, 6)
alphabet =\
    {
        "A": [(0, 3), (-2, -3), (-1, 0), (1, 0), (0, 3), (2, -3)],
        "B": [(-2, 0), (-2, 3), (0, 3), (1, 2), (1, 1), (0, 0), (2, -1), (2, -2), (1, -3), (-2, -3), (-2, 0), (0, 0)],
        "C": [(2, 3), (0, 3), (-1, 2), (-1, -2), (0, -3), (2, -3)],
        "D": [(-2, -3), (-2, 3), (0, 3), (2, 1), (2, -1), (0, -3), (-2, -3)],
        "E": [(2, 3), (-2, 3), (-2, 0), (2, 0), (-2, 0), (-2, -3), (2, -3)],
        "F": [(2, 3), (-2, 3), (-2, 0), (2, 0), (-2, 0), (-2, -3)],
        "G": [(0, 0), (2, 0), (2, -2), (1, -3), (-1, -3), (-2, -2), (-2, 2), (-1, 3), (1, 3), (2, 2)],
        "H": [(-2, 3), (-2, -3), (-2, 0), (2, 0), (2, 3), (2, -3)],
        "I": [(-1, 3), (1, 3), (0, 3), (0, -3), (1, -3), (-1, -3)],
        "J": [(-1, 3), (2, 3), (2, -2), (1, -3), (-1, -3), (-2, -2),],
        "K": [(-2, 3), (-2, -3), (-2, 0), (-1, 0), (2, 3), (-1, 0), (2, -3)],
        "L": [(-2, 3), (-2, -3), (2, -3)],
        "M": [(-2, -3), (-2, 3), (0, 0), (2, 3), (2, -3)],
        "N": [(-2, -3), (-2, 3), (2, -3), (2, 3)],
        "O": [(1, 3), (2, 2), (2, -2), (1, -3), (-1, -3), (-2, -2), (-2, 2), (-1, 3), (1, 3)],
        "P": [(-2, -3), (-2, 3), (0, 3), (1, 2), (1, 1), (0, 0), (-2, 0)],
        "Q": [(1, -3), (-1, -3), (-2, -2), (-2, 2), (-1, 3), (1, 3), (2, 2), (2, -2), (1, -3), (1.5, -2.5), (2, -3)],
        "R": [(-2, -3), (-2, 3), (0, 3), (1, 2), (1, 1), (0, 0), (-2, 0), (2, -3)],
        "S": [(2, 2), (1, 3), (-1, 3), (-2, 2), (-2, 1), (-1, 0), (1, 0), (2, -1), (2, -2), (1, -3), (-1, -3), (-2, -2)],
        "T": [(-2, 3), (2, 3), (0, 3), (0, -3)],
        "U": [(2, 3), (2, -2), (1, -3), (-1, -3), (-2, -2), (-2, 3)],
        "V": [(-2, 3), (0, -3), (2, 3)],
        "W": [(-2, 3), (-1, -3), (0, 2), (1, -3), (2, 3)],
        "X": [(-2, 3), (2, -3), (0, 0), (2, 3), (-2, -3)],
        "Y": [(-2, 3), (0, 0), (2, 3), (0, 0), (0, -3)],
        "Z": [(-2, 3), (2, 3), (-2, -3), (2, -3)],
    }
t = turtle.Turtle()
t.speed(0)


def print_text(text, space=(1, 1), scale=(1, 1), offset=(0, 0)):
    lines = text.split("\n")
    cursor = (None, len(lines) / 2 * (letter_size[1] + space[1]) * scale[1] - (letter_size[1] + space[1]) / 2 * scale[1])

    for line in lines:
        cursor = (-len(line) / 2 * (letter_size[0] + space[0]) * scale[0] + (letter_size[0] + space[0]) / 2 * scale[0], cursor[1])
        for letter in line:
            if letter in alphabet:
                print_shape(alphabet[letter], scale, scale_and_offset(cursor, offset=offset))
            cursor = (cursor[0] + (space[0] + letter_size[0]) * scale[0], cursor[1])
        cursor = (None, cursor[1] - scale[1] * (space[1] + letter_size[1]))


def print_shape(points, scale=(1, 1), offset=(0, 0), loop=False):
    p = points[0]
    t.penup()
    t.setpos(scale_and_offset(p, scale, offset))
    t.pendown()
    for i in range(1, len(points)):
        t.setpos(scale_and_offset(points[i], scale, offset))
    if loop:
        t.setpos(scale_and_offset(p, scale, offset))


def scale_and_offset(point, scale=(1, 1), offset=(0, 0)):
    return point[0] * scale[0] + offset[0], point[1] * scale[1] + offset[1]


def draw_all_letters():
    letters = "".join([x for x in alphabet if len(alphabet[x]) != 0])
    letters = letters[0:10] + "\n" + letters[10:20] + "\n" + letters[20:]
    print_text(letters, scale=(10, 10), offset=(0, 0))

def done():
    turtle.done()
