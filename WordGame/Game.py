import time
import Printer.PolyPrinter as tt

cross = [(-1, -1), (1, 1), (0, 0), (-1, 1), (1, -1)]
heart = [(0, 2), (1, 3), (2, 3), (3, 2), (3, 1), (0, -2),  (-3, 1), (-3, 2), (-2, 3), (-1,  3)]
drawing = [
    [(-3, 0), (-2, 2), (-1, 0)],
    [(-2, 2), (-2, 6)],
    [(-2, 6), (2, 6)],
    [(2, 6), (2, 5.5)],
    [(2, 5.5), (2.3, 5.3), (2.5, 5), (2.3, 4.7), (2, 4.5), (1.7, 4.7), (1.5, 5), (1.7, 5.3), (2, 5.5)],
    [(2, 4.5), (2, 2)],
    [(2, 2), (1, 0.5)],
    [(2, 2), (3, 0.5)],
    [(1, 3.7), (3, 3.7)]
]

hearts_offsets = []
letter_offsets = {}


def draw_letters():
    letters = "".join(tt.alphabet)
    count = len(letters)
    scale = (3, 3)
    space = 20
    offset = (-count / 2 * (space / 2) - 135, -200)

    for l in letters:
        letter_offsets[l] = offset
        tt.print_text(l, (0, 0), scale, offset)
        offset = offset[0] + space, offset[1]


def cross_heart(index):
    offset = (0, 5)
    offset = hearts_offsets[index][0] + offset[0], hearts_offsets[index][1] + offset[1]
    tt.print_shape(cross, (25, 25), offset)


def cross_letter(letter):
    scale = (5, 15)
    offset = (0, 0)
    offset = letter_offsets[letter][0] + offset[0], letter_offsets[letter][1] + offset[1]
    tt.print_shape(cross, scale, offset)


def draw_hearts():
    count = len(drawing)
    scale = (10, 10)
    space = 65
    offset = (-count / 2 * (30 + space / 2) + 10, 225)

    for i in range(count):
        hearts_offsets.append(offset)
        tt.print_shape(heart, scale, offset, loop=True)
        offset = offset[0] + space, offset[1]


def draw_a_dead_guy():
    for segment in drawing[0:9]:
        tt.print_shape(segment, (30, 30))
        time.sleep(1)
