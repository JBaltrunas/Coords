import Printer.PolyPrinter as tt
import WordGame.Game as game

start = (-300, 0)
offset = (45, 0)

game.draw_a_dead_guy()
game.draw_hearts()
for i in range(8, -1, -1):
    game.cross_heart(i)
game.draw_letters()
for i in "".join(tt.alphabet):
    game.cross_letter(i)

tt.done()


