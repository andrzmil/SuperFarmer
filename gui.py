from tkinter import *
from tkinter import ttk
from super_farmer import dice_roll, Player, Game

G= Game()

root = Tk()
root.geometry("800x600")
root.title("Super Farmer")
result_var = StringVar()
board_var = StringVar()

#DICE ROLL
def res_on_click():
    result_var.set(dice_roll())

#ANIMALS STATUS


dice_btn = Button(root, text = 'Rzuc kostka', command= res_on_click)
dice_btn.pack()





#BOARDW
board = LabelFrame(root, text = 'Główne Stado')
board.pack(side= TOP,  anchor="w", pady="20")

#board_lbl = Label(board, text="🐇: 0 🐏: 0 🐖: 0 🐄: 0 🐎: 0 🐩: 0 🐕‍🦺: 0")
board_lbl = Label(board, text=G.print_deck())
board_lbl.pack()

#RESULT
result = LabelFrame(root, text = 'Wynik rzutu')
result.pack(fill= "both")
result_lbl = Label(root, textvariable= result_var)
result_lbl.pack(fill = "both")







if __name__ == '__main__':
    root.mainloop()
