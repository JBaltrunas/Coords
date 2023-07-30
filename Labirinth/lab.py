import random

import Printer.PolyPrinter as tt

# Params start

block_count = 100000000

size = 20
scale = (size, size)
offset = (size, size)

max_x = 500 // size
min_x = -500 // size
max_y = 250 // size
min_y = -250 // size

# Colors

border_color = (0, 255, 255)
border_width = 3
cell_background_color = (100, 100, 0)
background_color = (0, 0, 0)

# Params end

up_border = [(-0.5, 0.5), (0.5, 0.5)]
right_border = [(0.5, 0.5), (0.5, -0.5)]
down_border = [(0.5, -0.5), (-0.5, -0.5)]
left_border = [(-0.5, -0.5), (-0.5, 0.5)]



labirinth = {}
path = []
target = (0, 0)
distance_to_target = 0
tt.set_background_color(background_color)

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
my_lab_2 = [
    ((True, True, True, True), (0, 0)),
    ((True, True, True, True), (50, 0)),
    ((True, True, True, True), (0, 25)),
    ((True, True, True, True), (-50, 0)),
    ((True, True, True, True), (0, -25)),
]


def draw_lab(lab):
    for bor, cor in lab:
        draw_borders(bor, cor)


def draw_cell_background(x, y, offset):
    tt.set_pen_color(cell_background_color)
    tt.set_pen_width(1)
    tt.t.fillcolor(cell_background_color)
    tt.t.begin_fill()
    tt.print_shape(up_border, scale, offset)
    tt.print_shape(right_border, scale, offset)
    tt.print_shape(down_border, scale, offset)
    tt.print_shape(left_border, scale, offset)
    tt.t.end_fill()


def draw_borders(borders, coord):
    x, y = coord
    ox, oy = offset
    new_offset = x * ox, y * oy
    draw_cell_background(x, y, new_offset)
    tt.set_pen_width(border_width)
    tt.set_pen_color(border_color)
    if borders[0]:
        tt.print_shape(up_border, scale, new_offset)
    if borders[1]:
        tt.print_shape(right_border, scale, new_offset)
    if borders[2]:
        tt.print_shape(down_border, scale, new_offset)
    if borders[3]:
        tt.print_shape(left_border, scale, new_offset)


def generate_lab():
    global distance_to_target, target
    # TODO: Do not close all
    first_block = (0, 0)
    add_block(first_block)
    draw_borders(labirinth[first_block], first_block)
    for i in range(block_count):
        clear_path_if_no_directions()
        if len(path) == 0:
            break
        new_coord = get_new_block_coords()
        add_block(new_coord)
        if distance_to_target < len(path):
            distance_to_target = len(path)
            target = path[-1][1]
        draw_borders(labirinth[new_coord], new_coord)

    close_labirinth()


def add_block(coord):
    up, right, down, left = get_block_borders(coord)
    if up == None:
        up = bool(random.random() > 0.5)
    if right == None:
        right = bool(random.random() > 0.5)
    if down == None:
        down = bool(random.random() > 0.5)
    if left == None:
        left = bool(random.random() > 0.5)

    borders = up, right, down, left
    path.append((borders, coord))
    labirinth[coord] = borders


def get_block_borders(coord):
    x, y = coord
    up = right = down = left = None
    if (x, y + 1) in labirinth:
        up = labirinth[(x, y + 1)][2]
    if (x + 1, y) in labirinth:
        right = labirinth[(x + 1, y)][3]
    if (x, y - 1) in labirinth:
        down = labirinth[(x, y - 1)][0]
    if (x - 1, y) in labirinth:
        left = labirinth[(x - 1, y)][1]

    if y + 1 > max_y:
        up = True
    if x + 1 > max_x:
        right = True
    if y - 1 < min_y:
        down = True
    if x - 1 < min_x:
        left = True

    return up, right, down, left


def get_available_directions(coord):
    x, y = coord
    up = right = down = left = False
    if (x, y + 1) not in labirinth:
        if not labirinth[coord][0]:
            up = True
    if (x + 1, y) not in labirinth:
        if not labirinth[coord][1]:
            right = True
    if (x, y - 1) not in labirinth:
        if not labirinth[coord][2]:
            down = True
    if (x - 1, y) not in labirinth:
        if not labirinth[coord][3]:
            left = True

    return up, right, down, left


def has_available_directions(directions):
    up, right, down, left = directions
    return up or right or down or left


def get_random_direction(available_directions):
    count_of_directions = 0
    for i in range(4):
        if available_directions[i]:
            count_of_directions += 1

    if count_of_directions == 0:
        return None

    skip = random.randrange(count_of_directions)
    res = [False, False, False, False]
    for i in range(4):
        if skip > 0 and available_directions[i]:
            skip -= 1
        elif available_directions[i]:
            res[i] = True
            break

    up, right, down, left = res
    return up, right, down, left


def get_new_block_coords():
    directions = get_available_directions(path[-1][1])
    direction = get_random_direction(directions)
    x, y = path[-1][1]
    if direction[0]:
        y += 1
    if direction[1]:
        x += 1
    if direction[2]:
        y -= 1
    if direction[3]:
        x -= 1

    return x, y


def clear_path_if_no_directions():
    global path
    while len(path) > 0 and not (has_available_directions(get_available_directions(path[-1][1]))):
        path = path[:-1]


def close_block(origin, coord):
    ox, oy = origin
    x, y = coord
    if x > ox:
        labirinth[coord] = (True, True, True, False)
    elif x < ox:
        labirinth[coord] = (True, False, True, True)
    elif y > oy:
        labirinth[coord] = (True, True, False, True)
    else:
        labirinth[coord] = (False, True, True, True)

    return labirinth[coord]


def get_coords_by_directions(origin):
    available_directions = get_available_directions(origin)
    x, y = origin
    coords = []
    if available_directions[0]:
        coords.append((x, y + 1))
    if available_directions[1]:
        coords.append((x + 1, y))
    if available_directions[2]:
        coords.append((x, y - 1))
    if available_directions[3]:
        coords.append((x - 1, y))

    return coords


def close_labirinth():
    global  min_x, max_x, min_y, max_y
    min_y -= 1
    min_x -= 1
    max_x += 1
    max_y += 1
    clear_path_if_no_directions()
    while len(path) > 0:
        coords = get_coords_by_directions(path[-1][1])
        for coord in coords:
            borders = close_block(path[-1][1], coord)
            draw_borders(borders, coord)
        clear_path_if_no_directions()
