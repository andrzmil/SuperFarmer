import collections
from random import choice, random, shuffle
from typing import Counter
import numpy as np
from numpy.core.defchararray import index
import operator

change_matrix = [
    ["KROLIK", "OWCA", 6, 1],
    ["OWCA", "KROLIK", 1, 6],
    ["OWCA", "SWINIA", 2, 1],
    ["SWINIA", "OWCA", 1, 2],
    ["SWINIA", "KROWA", 3, 1],
    ["KROWA", "SWINIA", 1, 3],
    ["KROWA", "KON", 2, 1],
    ["KON", "KROWA", 1, 2],
    ["MALY_PIES", "OWCA", 1, 1],
    ["OWCA", "MALY_PIES", 1, 1,],
    ["KROWA", "DUZY_PIES", 1, 1],
    ["DUZY_PIES", "KROWA", 1, 1,]
    ]

class Game:
    def __init__(self):
        self.deck = { "KROLIK": 60, "OWCA": 24, "SWINIA": 20, "KROWA": 12, "KON": 6, "MALY_PIES": 4, "DUZY_PIES": 2 }
        self.green_dice = ["KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","OWCA","OWCA","OWCA","SWINIA","KROWA","WILK"]
        self.red_dice = ["KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","OWCA","OWCA","OWCA","SWINIA","KON","LIS"]
        self.curr_pl = 0
        self.no_of_pl = 0
        
    def change_deck(self, animal, action):
        self.deck[animal] = self.deck[animal] + action 

    def print_deck(self):
        rpl_dict = {"KROLIK": "🐇", "OWCA": "🐏", "SWINIA": "🐖", "KROWA": "🐄", "KON": "🐎", "MALY_PIES": "🐩", "DUZY_PIES": "🦮"}
        return dict((rpl_dict[key], value) for (key, value) in self.deck.items())


class Dice:
    def __init__(self):
        self.green_dice = ["KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","OWCA","OWCA","OWCA","SWINIA","KROWA","WILK"]
        self.red_dice = ["KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","KROLIK","OWCA","OWCA","OWCA","SWINIA","KON","LIS"]
        self.result = collections.Counter([choice(self.green_dice), choice(self.red_dice)])


    def print_dice_roll(self):
        rpl_dict = {"KROLIK": "🐇", "OWCA": "🐏", "SWINIA": "🐖", "KROWA": "🐄", "KON": "🐎", "WILK": "🐺", "LIS": "🦊"}
        return dict((rpl_dict[key], value) for (key, value) in dict(self.result).items())

    
d = Dice()
print(d.result)




class Player:
    def __init__(self, pname):
        self.player_deck = { "KROLIK": 0, "OWCA": 0, "SWINIA": 0, "KROWA": 0, "KON": 0, "MALY_PIES": 0, "DUZY_PIES": 0 }
        self.pname = pname
        self.state = False

    def change_player_deck(self, animal, action):
        self.player_deck[animal] = self.player_deck[animal] + action

    def print_player_deck(self):
        rpl_dict = {"KROLIK": "🐇", "OWCA": "🐏", "SWINIA": "🐖", "KROWA": "🐄", "KON": "🐎", "MALY_PIES": "🐩", "DUZY_PIES": "🦮"}
        return dict((rpl_dict[key], value) for (key, value) in self.player_deck.items()) 




# #generate players
# no_players = None
# while type(no_players) is not int or no_players < 2 or no_players > 4:
#     try:
#         no_players = input(r"Wybierz liczbę graczy między 2 a 4: ")
#         no_players = int(no_players)
#     except ValueError:
#         print("Nieprawidłowa liczba graczy!")

# pl_pool = []

# for i in range(no_players):
#     cur_pname = input("Podaj imie gracza numer " + str(i+1) + ": ")
#     temp_pl = Player(cur_pname)
#     pl_pool.append(temp_pl)
#     print("Cześć " + pl_pool[i].pname)

# #shuffle players
# shuffle(pl_pool)

# for i in range(3):
#     for p in pl_pool:
#         print("-------------------------------------------------------------------------------")
#         print("Tura " + p.pname)

#         #change part


#         print("Wynik rzutu kostką: ")
#         draw_result = p.players_draw()
#         merged_result = dict(Counter(draw_result) + Counter(p.player_deck))
#         for v,c in draw_result.items():
#             print(v,c)

#         #get animals from the deck
#         for k in draw_result.keys():    
#             print("Liczba zwierząt " + str(k) + " " + str(merged_result[k]))
#             #check wolf
#             if k == "WILK":
#                 p.player_deck = dict.fromkeys(p.player_deck, 0)
#                 print("Tracisz wszystkie zwierzęta!")
#                 print("Stan posiadania " + str(p.pname) + ": ")
#                 print(p.player_deck)
#                 break
#             #check fox - if there is rabbit within drawn animals exit loop
#             elif k == "LIS":
#                 p.player_deck["KROLIK"] = 0
#                 print("Tracisz wszystkie króliki")
#                 print(p.player_deck)
#                 if "KROLIK" in draw_result:
#                     print("Stan posiadania " + str(p.pname) + ": ")
#                     print(p.player_deck)
#                     break
#                 print("Stan posiadania " + str(p.pname) + ": ")
#                 print(p.player_deck)            
#             #check if there is at least one pair
#             elif merged_result[k] >= 2:
#                 #round down to nearest integer
#                 no_of_cur_animal = int(merged_result[k] / 2)
#                 if (deck[k] - no_of_cur_animal) > 0:
#                     deck[k] = deck[k] - no_of_cur_animal
#                     p.player_deck[k] = p.player_deck[k] + no_of_cur_animal
#                 else:
#                     deck[k] = 0
#                     p.player_deck[k] = p.player_deck[k] + (no_of_cur_animal - deck[k])
                
#                 print(p.pname + " otrzymuje " + str(no_of_cur_animal) + "x " + k)
#             print(p.player_deck)

# print(deck)


    