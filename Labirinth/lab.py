import random

import Printer.PolyPrinter as tt

up_border = [(-0.5, 0.5), (0.5, 0.5)]
right_border = [(0.5, 0.5), (0.5, -0.5)]
down_border = [(0.5, -0.5), (-0.5, -0.5)]
left_border = [(-0.5, -0.5), (-0.5, 0.5)]

scale = (10, 10)
offset = (10, 10)

labirinth = map()


my_lab_1 = [
    ((True, True, True, False), (0, 0)),
    ((True, False, True, False), (-1, 0)),
    ((True, False, False, True), (-2, 0)),
    ((False, False, True, False), (-2, -1)),
    ((True, False, True, False), (-1, -1)),
    ((False, True, False, False), (0, -1)),
    ((False, True, False, True), (0, -2)),
    ((False, True, True, True), (0, -3)),
    ((True, False, True, True), (-3, -1))
]


def draw_lab(lab):
    for bor, cor in lab:
        draw_borders(bor, cor)


def draw_borders(borders, coord):
    x, y = coord
    ox, oy = offset
    new_offset = x * ox, y * oy
    if borders[0] == True:
        tt.print_shape(up_border, scale, new_offset)
    if borders[1] == True:
        tt.print_shape(right_border, scale, new_offset)
    if borders[2] == True:
        tt.print_shape(down_border, scale, new_offset)
    if borders[3] == True:
        tt.print_shape(left_border, scale, new_offset)


def generate_lab():
    labirinth[(0, 0)] = (bool(random.random(1)), bool(random.random(1)), bool(random.random(1)), bool(random.random(1)))
    draw_borders(labirinth[(0, 0)], (0, 0))