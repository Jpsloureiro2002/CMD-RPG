import os
from global_var import Global as g
from func import *
import pyfiglet
import sys
import time

res = lambda : os.system('mode con: cols=100 lines=30')
clsp = lambda : os.system('cls')

def Game(game_Start):
    Display.draw_raw_Map()
    Generation.gen_item(3,"potions")
    Generation.gen_item(2,"swords")
    Generation.gen_monster(2)
    while (game_Start and not g.DEAD):
        res()
        Logs.log(f"{g.PLAYER_X}/{g.PLAYER_Y}")
        Display.update_map()
        Display.display_options()
        #print(g.Map)
        Option = input("")
        Colision.check_col()
        KeyEvent.KeyPress(Option)
def Options():
    while True:
        clsp()
        banner = pyfiglet.figlet_format("Options!")
        print(banner)
        print("Here o can costumise your Character and Change some Things\nHere is the List: skin, back")
        op = input("Type Here:\n")
        if op == "skin":
            clsp()
            print(banner)
            stop = False
            while not stop:
                clsp()
                print(banner)
                key = list(g.skins.keys())
                for i in key:
                    print(f"Code:{i} --> {g.skins.get(i)}")
                op = input("\nType Here the code of the skin:\n")
                if op in key:
                    g.PLAYER_SKIN = g.skins.get(op)
                    stop = True
                else:
                    clsp()
        if op == "back":
            break    
##Start of Program
while True:
    clsp()
    banner = pyfiglet.figlet_format("Math Dungeons!!")
    print(banner)
    print("Choose your Option: start, options(o), load*,quit(q)")
    op = input("Type Here:\n")
    if op == "start":
        game_Start = True
        Game(game_Start)
    if (op == "quit" or op == "q"):
        clsp()
        banner = pyfiglet.figlet_format("Bye :(")
        print(banner)
        time.sleep(3)
        sys.exit()
    if (op == "o" or op =="options"):
        Options()




        
    
    
    