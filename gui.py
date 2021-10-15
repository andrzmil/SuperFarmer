from random import shuffle
from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from super_farmer import Player, Game, Dice
import collections
from typing import Counter



root = Tk()
root.geometry("800x700")
root.title("Super Farmer")


curr_pl = 0
result_var = StringVar()
board_var = StringVar()
crn_state_var = StringVar()

##########TOP FRAME
top_frame = Frame(root)
top_frame.pack(side= "top", fill="x")

#NO PLAYERS
no_pl_lbl = Label(top_frame, text="Liczba graczy")
no_pl_lbl.pack(side="left")
no_pl = ttk.Combobox(top_frame, values=(2,3,4,5,6), state="readonly")
no_pl.set(2)
no_pl.pack(side="left")

#second TOP FRAME
second_top_frame = Frame(root)
second_top_frame.pack(side= "top", fill="x")

#third TOP FRAME
third_top_frame = Frame(root)
third_top_frame.pack(side= "top", fill="x")


#Bottom frame
bottom_frame = Frame(root)
bottom_frame.pack(side="bottom", fill="x")




def new_game():
    global pl_pool
    global pl_board
    global pl_deck_pool
    global pl_txt_var
    global G
    pl_pool = []
    pl_board = []
    pl_deck_pool = []
    pl_txt_var = []
    
    
    G = Game()
    G.no_of_pl = no_pl
    board_var.set(G.print_deck())
    
    

    

    #BOARD
    board = LabelFrame(second_top_frame, text = 'Główne Stado')
    board.pack(side= "left")

    board_lbl = Label(board , font=(36), textvariable=board_var)
    board_lbl.pack()

    #RESULT
    draw_result = LabelFrame(third_top_frame, text = 'Wynik rzutu')
    draw_result.pack(side="left")
    draw_result_lbl = Label(draw_result, textvariable= result_var, font=(36))
    draw_result_lbl.pack(fill = "both")

    #current state
    crn_state = Label(third_top_frame, textvariable=crn_state_var)
    crn_state.pack(side="left")
    
    for i in range(int(no_pl.get())):
        tmp_pl = askstring("Podaj imię:", "Gracz numer " + str(i+1))
        pl_pool.append(Player(tmp_pl))
        #widgets
        tmp_pl_board = LabelFrame(root, text = 'Stan posiadania ' + str(pl_pool[i].pname))
        pl_board.append(tmp_pl_board)
        pl_board[i].pack(side= TOP,  anchor="w", pady="20")
        tmp_pl_txt_var = StringVar()
        pl_txt_var.append(tmp_pl_txt_var)
        pl_txt_var[i].set(pl_pool[i].print_player_deck())
        tmp_pl_deck = Label(pl_board[i], textvariable= pl_txt_var[i], font=(36))
        pl_deck_pool.append(tmp_pl_deck)
        pl_deck_pool[i].pack()
        

    #shuffle players
    shuffle(pl_pool)
    G.no_of_pl = int(no_pl.get())
  

    turn_btn = Button(top_frame, text = 'Tura gracza', command=players_turn)
    turn_btn.pack(side="left")



def players_turn():
    crn_state_var.set("Tura gracza: " + pl_pool[G.curr_pl].pname + " " + str(G.curr_pl))
    d = Dice()
    print("starttestu")
    print(d.print_dice_roll())
    print(pl_pool[G.curr_pl].pname)
    print(pl_pool[G.curr_pl].player_deck)
    result_var.set(d.print_dice_roll())
    merged_result = dict(Counter(d.result) + Counter(pl_pool[G.curr_pl].player_deck))
        
    for k in d.result.keys():
        print(k)
        if merged_result[k] >= 2:
            #check if rounded number of drawn animal + current resources gives at letas one pair
            no_of_cur_animal = int(merged_result[k] / 2)

            #adjust deck
            G.change_deck(k, -(no_of_cur_animal))
            #refresh board state
            board_var.set(G.print_deck())
            #add animals to player deck
            pl_pool[G.curr_pl].change_player_deck(k, no_of_cur_animal)
            pl_txt_var[G.curr_pl].set(pl_pool[G.curr_pl].print_player_deck())
            print(pl_txt_var[G.curr_pl])
    if (G.curr_pl == G.no_of_pl-1):
        G.curr_pl = 0
    else:
        G.curr_pl += 1

        
    print(pl_pool[G.curr_pl].player_deck)
    del d
        
        
        
        
        
        



    #players turn
    







new_game_btn = Button(top_frame, text = 'Nowa gra', command=new_game)
new_game_btn.pack(side="left")















if __name__ == '__main__':
    root.mainloop()
