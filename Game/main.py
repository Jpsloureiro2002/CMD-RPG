import os
from global_var import Global as g
from func import *
import pyfiglet
import sys
import time

res = lambda : os.system('mode con: cols=100 lines=30')
clsp = lambda : os.system('cls')

def Game(game_Start, Load):
    if not Load:
        Logs.log(f"#######[TURN{g.TURNS}]##########")
        Display.draw_raw_Map()
        Generation.gen_item(3,"potions")
        Generation.gen_item(1,"swords")
        Generation.gen_item(1,"Shield")
        Generation.gen_item(1,"Armor")
        Generation.gen_monster(1+int(g.STATS["Level"]))
    else:
        slot = input("Witch Slot 1~5:\n")
        Data.load(slot)
    while (game_Start and not g.DEAD and not g.GAME_WIN):
        if g.NEXT_LEVEL:
            Generation.clearGen()
            g.TURNS = 0
            Logs.log(f"#######[TURN{g.TURNS}]##########")
            Display.draw_raw_Map()
            Generation.gen_item(3,"potions")
            Generation.gen_item(2,"swords")
            Generation.gen_monster(2)
            g.NEXT_LEVEL = False
        res()
        Logs.log(f"[Player Coords]x:{g.PLAYER_X} y:{g.PLAYER_Y}")
        Display.update_map()
        Display.display_options()
        while True:
            Option = input("")
            if (Option == "save"):
                slot_chose= input("Witch Slot 1~5:\n")
                Data.save(slot_chose)
            elif(Option == "quit"):
                choise = input("Are you shure your progress won't be save(y/n)!\n")
                if choise == "y":
                    clsp()
                    banner = pyfiglet.figlet_format("Bye :(")
                    print(banner)
                    time.sleep(3)
                    sys.exit()
            elif (Option == "inv" or Option == "i"):
                Display.draw_inv()
            elif (Option == "stats" or Option == "st"):
                Display.draw_stats()
                break
            else:
                break
        Colision.check_col()
        KeyEvent.KeyPress(Option)
        AI.Monster_AI()
        g.TURNS +=1
        Logs.log(f"#######[TURN{g.TURNS}]##########")
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
    g.GAME_WIN = False
    g.STATS["Level"] = 0
    g.TURNS = 0
    banner = pyfiglet.figlet_format("Math Dungeons!!")
    print(banner)
    print("Choose your Option: start(s), options(o), load(l),quit(q)")
    op = input("Type Here:\n")
    if (op == "start" or op == "s"):
        game_Start = True
        Game(game_Start, False)
    if (op == "quit" or op == "q"):
        clsp()
        banner = pyfiglet.figlet_format("Bye :(")
        print(banner)
        time.sleep(3)
        sys.exit()
    if (op == "o" or op =="options"):
        Options()
    if (op == "l" or op =="load"):
        game_Start = True
        Game(game_Start, True)




        
    
    
    