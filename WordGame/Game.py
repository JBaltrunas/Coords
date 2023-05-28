import threading
import time

import Printer.PolyPrinter as tt


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


def draw_hearts():
    count = len(drawing)


def draw_a_dead_guy():
    for segment in drawing[0:9]:
        tt.print_shape(segment, (30, 30))
        time.sleep(1)
