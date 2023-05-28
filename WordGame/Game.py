import time
import Printer.PolyPrinter as tt

# Start params --------------------

# Heart
heart_scale = (10, 10)
heart_spaces = 65
first_heart_offset = (-271.25, 225)

# Heart cross
heart_cross_offset = (0, 5)
heart_cross_scale = (25, 25)

# Letter
letters_scale = (3, 3)
letters_space = 20
first_letter_offset = (-265, -200)

# Letter cross
letter_cross_offset = (0, 0)
letter_cross_scale = (5, 15)

# End params   --------------------


cross = [(-1, -1), (1, 1), (0, 0), (-1, 1), (1, -1)]
heart = [(0, 2), (1, 3), (2, 3), (3, 2), (3, 1), (0, -2),  (-3, 1), (-3, 2), (-2, 3), (-1,  3)]
heart_border = [(-3.5, 3.5), (3.5, 3.5), (3.5, -2.5), (-3.5, -2.5)]
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

heart_count = len(drawing)
letters = "".join(tt.alphabet)
letters_count = len(letters)

hearts_offsets = []
letter_offsets = {}


def draw_letters():
    offset = first_letter_offset
    for l in letters:
        letter_offsets[l] = offset
        tt.print_text(l, (0, 0), letters_scale, offset)
        offset = offset[0] + letters_space, offset[1]


def cross_letter(letter):
    offset = letter_offsets[letter][0] + letter_cross_offset[0], letter_offsets[letter][1] + letter_cross_offset[1]
    tt.print_shape(cross, letter_cross_scale, offset)


def draw_hearts():
    offset = first_heart_offset
    for i in range(heart_count):
        hearts_offsets.append(offset)
        tt.print_shape(heart, heart_scale, offset, loop=True)
        offset = offset[0] + heart_spaces, offset[1]


def cross_heart(index):
    offset = hearts_offsets[index][0] + heart_cross_offset[0], hearts_offsets[index][1] + heart_cross_offset[1]
    tt.print_shape(cross, heart_cross_scale, offset)


def draw_hearts_borders():
    pass

def draw_a_dead_guy():
    for segment in drawing[0:9]:
        tt.print_shape(segment, (30, 30))
