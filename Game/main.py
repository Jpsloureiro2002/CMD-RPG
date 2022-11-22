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
    while (game_Start and not g.DEAD):
        res()
        Logs.log(f"{g.PLAYER_X}/{g.PLAYER_Y}")
        Display.update_map()
        Display.display_options()
        #print(g.Map)
        Option = input("")
        Colision.check_col()
        KeyEvent.KeyPress(Option)


##Start of Program
while True:
    clsp()
    banner = pyfiglet.figlet_format("Math Dungeons!!")
    print(banner)
    print("Choose your Option: start, options*, load*,quit")
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




        
    
    
    