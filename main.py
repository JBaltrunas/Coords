import Printer.PolyPrinter as tt
import WordGame.Game as game

game.select_word()
game.draw_all()
print(game.selected_word)
while True:
    letter = input()
    game.draw_letter(letter)
tt.done()

