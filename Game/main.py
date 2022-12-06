import os
from global_var import Global as g
from func import *
import pyfiglet
import sys
import time

res = lambda : os.system('mode con: cols=100 lines=30')
clsp = lambda : os.system('cls')

def Game(game_Start, Load):
    Func.setMaxP()
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
    while (game_Start) and (not g.DEAD) and (not g.GAME_WIN):
        #Logs.log(f"[DEBUG] GAME START : {g.DEAD}")
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
        if g.IS_BATTLE:
            """Logs.log(f"[DEBUG] EQUAL: {g.MONSTER_INFO in g.NEW_GEN_MONSTER}")
            Logs.log(f"[DEBUG] MOSNTER INFO: {g.MONSTER_INFO}")
            Logs.log(f"[DEBUG] NEW GEM MONSTER: {g.NEW_GEN_MONSTER}")"""
            ##Erro alguns mosntros não dão o mosntro serto
            if g.MONSTER_INFO:
                if g.bestiary[g.MONSTER_INFO]:
                    #Monster_stats = g.bestiary.get(g.MONSTER_INFO)
                    Monster_stats = Generation.create_montser_stat()
                else:
                    Monster_stats = Generation.create_montser_stat()
            else:
                    Monster_stats = Generation.create_montser_stat()
        win = False
        while (g.IS_BATTLE and not win):
            nextt = False
            while not nextt:
                clsp() 
                Display.draw_battle(Monster_stats)
                print("\n"*2)
                print("If you find this *, it will cost youa  turn!")
                print("Commands: Atack(a)*, inv(i)*, stats(s)")
                option = input("What will you do?\n")
                if option == "a":
                    Monster_stats = Data.attackMonster(Monster_stats)
                    nextt = True
                elif (option == "inv" or option == "i"):
                    Display.draw_inv()
                    nextt = True
                elif (option == "stats" or option == "s"):
                    Display.draw_stats()
                    nextt = False
            
            Is_Monster_Dead = Data.is_dead_M(Monster_stats)
            if Is_Monster_Dead:
                win = True
                g.IS_BATTLE = False
                g.MONSTER_INFO = None
                Func.givexp(Monster_stats[4])
                Monster_stats.clear()
                break
            else:
                AI.Monster_Turn(Monster_stats)
            Is_PLayer_Dead = Data.is_dead_P()
            if Is_PLayer_Dead:
                Logs.log("[DEBUG] PLAYER IS DEAD")
                Display.draw_Game_over()
                g.IS_BATTLE = False
                g.MONSTER_INFO = None
                break

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
    g.STATS = g.STATS_DEF.copy()
    g.equip = g.equip_def.copy()
    g.NEW_GEN_ITEMS.clear()
    g.NEW_GEN_MONSTER.clear()
    g.DEAD = False
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




        
    
    
    