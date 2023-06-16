import random
import time
import Printer.PolyPrinter as tt

# Start params --------------------
bg_color = (0, 0, 0)

# Selected word
selected_word_scale = (7, 7)
selected_word_color = (15, 19, 118)
selected_word_offset = (0, -100)
selected_word_width = 3

# Underline
underline_color = (15, 19, 118)
underline_width = 2
underline_vertical_offset = -25

# Border
border_offset = (-10, -20)
border_scale = (100, 85)
border_color = (50, 50, 255)
border_size = 10

# Dead guy
dead_guy_color = (255, 255, 100)
dead_guy_size = 10

# Heart
heart_scale = (10, 10)
heart_spaces = 75
first_heart_offset = (-310, 225)
heart_color = (255, 0, 0)
heart_size = 3

# Heart border
heart_border_color = (120, 0, 0)
heart_border_size = 2

# Heart cross
heart_cross_offset = (0, 5)
heart_cross_scale = (25, 25)
heart_cross_color = (0, 255, 255)
heart_cross_size = 5

# Letter
letters_scale = (3, 3)
letters_space = 20
first_letter_offset = (-265, -200)
letters_color = (255, 255, 255)
letters_size = 1.5

# Letter cross
letter_cross_offset = (0, 0)
letter_cross_scale = (5, 15)
letter_cross_color = (255, 0, 255)
letter_cross_size = 3

# End params   --------------------


cross = [(-1, -1), (1, 1), (0, 0), (-1, 1), (1, -1)]
heart = [(0, 2), (1, 3), (2, 3), (3, 2), (3, 1), (0, -2),  (-3, 1), (-3, 2), (-2, 3), (-1,  3)]
heart_border = [(-3.5, 3.5), (3.5, 3.5), (3.5, -2.5), (-3.5, -2.5)]
full_border = [(-3.5, 3.5), (3.5, 3.5), (3.5, -2.5), (-3.5, -2.5)]
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


tt.set_background_color(bg_color)

# Logic
selected_word = ""
gues_word = ""
used_letters = ""
health = len(drawing)


def start_game():
    global used_letters, health, gues_word
    select_word()

    draw_underlines()
    draw_full_border()
    draw_letters()
    draw_hearts()
    draw_heart_borders()

    while health > 0 and " " in gues_word:
        letter = read_letter_nicht()
        if letter in used_letters:
            print("Letter already used")
            continue
        cross_letter(letter)
        used_letters += letter
        if letter in selected_word:
            draw_letter(letter)
            word = ""
            for i in range(len(selected_word)):
                if selected_word[i] == letter:
                    word += letter
                else:
                    word += gues_word[i]
            gues_word = word
            print(gues_word)
        else:
            draw_a_dead_guy_part(heart_count - health)
            health -= 1
            cross_heart(health)

    if health > 0:
        print("You won")
    else:
        print(f"You lose ({selected_word})")


def read_letter_nicht():
    while True:
        letter = input('Write letter: ')[0].upper()
        if letter not in letters:
            print(f"'{letter}' no")
            continue
        return letter


def select_word():
    f = open("WordGame/Word.txt")
    words = f.read().split("\n")
    f.close()
    global selected_word, gues_word
    selected_word = random.choice(words).upper()
    gues_word = " " * len(selected_word)


# GUI

def draw_underlines():
    lines = "V" * len(selected_word)
    tt.set_pen_color(underline_color)
    tt.set_pen_width(underline_width)
    scale = selected_word_scale[0], 0
    offset = selected_word_offset[0], selected_word_offset[1] + underline_vertical_offset
    tt.print_text(lines, scale=scale, offset=offset)


def draw_letter(letter):
    tt.set_pen_color(selected_word_color)
    tt.set_pen_width(selected_word_width)
    letter = letter[0].upper()
    line = ""
    for ltt in selected_word:
        if ltt == letter:
            line += letter
        else:
            line += " "
    tt.print_text(line, scale=selected_word_scale, offset=selected_word_offset)


def draw_selected_word():
    tt.set_pen_color(selected_word_color)
    tt.set_pen_width(selected_word_width)
    tt.print_text(selected_word, scale=selected_word_scale, offset=selected_word_offset)


def draw_letters():
    tt.set_pen_color(letters_color)
    tt.set_pen_width(letters_size)
    offset = first_letter_offset
    for l in letters:
        letter_offsets[l] = offset
        tt.print_text(l, (0, 0), letters_scale, offset)
        offset = offset[0] + letters_space, offset[1]


def cross_letter(letter):
    tt.set_pen_color(letter_cross_color)
    tt.set_pen_width(letter_cross_size)
    offset = letter_offsets[letter][0] + letter_cross_offset[0], letter_offsets[letter][1] + letter_cross_offset[1]
    tt.print_shape(cross, letter_cross_scale, offset)


def draw_hearts():
    tt.set_pen_color(heart_color)
    tt.set_pen_width(heart_size)
    offset = first_heart_offset
    for i in range(heart_count):
        hearts_offsets.append(offset)
        tt.print_shape(heart, heart_scale, offset, loop=True)
        offset = offset[0] + heart_spaces, offset[1]


def draw_heart_borders():
    tt.set_pen_color(heart_border_color)
    tt.set_pen_width(heart_border_size)
    for offset in hearts_offsets:
        tt.print_shape(heart_border, heart_scale, offset, loop=True)


def cross_heart(index):
    tt.set_pen_color(heart_cross_color)
    tt.set_pen_width(heart_cross_size)
    offset = hearts_offsets[index][0] + heart_cross_offset[0], hearts_offsets[index][1] + heart_cross_offset[1]
    tt.print_shape(cross, heart_cross_scale, offset)


def draw_full_border():
    tt.set_pen_color(border_color)
    tt.set_pen_width(border_size)
    tt.print_shape(full_border, border_scale, border_offset, True)


def draw_a_dead_guy_part(part_nr):
    tt.set_pen_color(dead_guy_color)
    tt.set_pen_width(dead_guy_size)
    tt.print_shape(drawing[part_nr], (30, 30))


def draw_a_dead_guy():
    tt.set_pen_color(dead_guy_color)
    tt.set_pen_width(dead_guy_size)
    for segment in drawing[0:9]:
        tt.print_shape(segment, (30, 30))


def draw_all():
    draw_underlines()
    draw_full_border()
    draw_a_dead_guy()
    draw_hearts()
    draw_heart_borders()
    draw_selected_word()
    for i in range(8, -1, -1):
        cross_heart(i)
    draw_letters()
    for l in letters:
        cross_letter(l)
