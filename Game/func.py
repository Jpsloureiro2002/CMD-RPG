from global_var import Global as g
import os
from PIL import Image
import random
import math
from datetime import datetime
import pyfiglet
import pickle
clsp = lambda : os.system('cls')
class Func:
    def setStatsLvup():
        g.STATS['Def']= int(g.STATS["LV"]*5*0.2)
        g.STATS['HP'], g.STATS['MAXP']= int(g.STATS["LV"] *9*0.2)
    def setMaxP():
        lv = g.STATS["LV"]
        maxxp= (lv+(lv+1))*100*0.5
        g.STATS['MAXP'] = int(maxxp)
        pass
    def givexp(Monster_level):
        xp = 50*(0.8* Monster_level)
        g.STATS['XP'] += int(xp)
        if Func.levelup():
            Display.draw_Battle_win(xp,True,0,g.STATS["LV"])
            Logs.log("[LEVEL UP] True")
        else:
             Display.draw_Battle_win(xp,False)
    def levelup():
        if g.STATS['XP'] >= g.STATS['MAXP']:
            rest = g.STATS['XP']-g.STATS['MAXP']
            g.STATS['XP'] = 0
            g.STATS['XP'] += int(rest)
            g.STATS['LV'] += 1
            Func.setMaxP()
            Func.setStatsLvup()
            return True
        if g.STATS['LV'] >= 50:
            return True
        else:
            return False
        pass
    def remove_Monster(x,y,types):
        New_gen_string = f"{y}/{x}/{types}"
        if New_gen_string in g.NEW_GEN_MONSTER:
            g.NEW_GEN_MONSTER.remove(New_gen_string)
    def item_pick_up(i_x,i_y):
        g.INFO_TEXT = "New Item Found Check your Inv"
        pos = Data.find_Item(i_x,i_y)
        if pos:
            str_clear = g.NEW_GEN_ITEMS[pos]
            str_info = g.NEW_GEN_ITEMS[pos].split("/")
            item_name = str_info[3]
            Logs.log(f"ITEM NAME : {str_clear}")
            dic_item = g.items.get(item_name)
            if dic_item:
                tup_Item = eval(str_info[2])
                ids = dic_item.index(tup_Item)
                str_formated = f"{item_name}/{ids}"
                if item_name != "potions":
                    if str_formated in g.inv:
                        g.NEW_GEN_ITEMS.remove(g.NEW_GEN_ITEMS[pos])
                        return False     
                g.inv.append(str_formated)
                g.NEW_GEN_ITEMS.remove(g.NEW_GEN_ITEMS[pos])
                Logs.log("[ITEM REMOVE] Item is now in your inv")
            else:
                Logs.log("[DICTIONARY ERROR] Dictionary is giving Null")
        else:
            Logs.log("[ITEM] Pos is False")
class Stats:
    def set_atrib():
        #ID/NOME
        g.STATS["Def"] = 0
        #lst list of the splited string and LSTD list of the dictionary
        if g.equip[0] != "":
            lst = g.equip[0].split("/")
            idi = int(lst[1])
            nome_dic = lst[0]
            lstd = g.items[nome_dic]
            g.STATS["Atk"] = 1 + lstd[idi][1]
        else:
            g.STATS["Atk"] = 1
        if g.equip[1] != "":
            lst = g.equip[1].split("/")
            idi = int(lst[1])
            nome_dic = lst[0]
            lstd = g.items[nome_dic]
            g.STATS["Def"] = g.STATS["Def"] + lstd[idi][1]
        else:
            g.STATS["Def"] = 0
        if g.equip[2] != "":
            lst = g.equip[2].split("/")
            idi = int(lst[1])
            nome_dic = lst[0]
            lstd = g.items[nome_dic]
            g.STATS["Def"] =g.STATS["Def"] + lstd[idi][1]

class Display:
    def draw_Battle_win(xp_gain, levelup = False, rest = 0, level = 0):
        clsp()
        Display.title("You Win!")
        print("\n"*2)
        if g.STATS['LV'] <= 50:
            if levelup:
                print(f"You defeat the monster and get {int(xp_gain)} xp and level up to NV: {level}")
            else:
                print(f"You defeat the monster and get {int(xp_gain)}")
        else:
            print(f"You defeat the monster and get {int(xp_gain)} xp but you reach the maximum level :(")
        input("\n\nWrite something to quit:\n")
        
    def draw_infos(Monster_stats):
        none = ""
        #HP, Def, ATK, Inv, Stats, ambos do monstro e HP Hint Gerar um Nome Difrente
        print(f"Player{none:49} Monster")
        #HP bar
        print(f"HP:{g.STATS['HP']}|{g.STATS['MAXHP']}{none:50} Monster HP: {Monster_stats[0]}/{Monster_stats[1]}")
    def draw_battle(Stats_M):
        file = os.path.join("Assets","Maps","script_MB_start.gif")
        img = Image.open(file).convert("RGB")
        pix = img.load()

        for y in range(15):
            row = ""
            for x in range(100):
                if pix[x,y] == (0,0,0):
                    row = row + "█"
                else:
                    row = row + " "
            print(row)
        Display.draw_infos(Stats_M)
    def draw_stats():
        clsp()
        Display.title("Stats!")
        print("#"*100)
        for key, value in g.STATS.items():
            if key != "Slot":
                print(f'{key:8}: {value}')
        print("#"*100)
        if g.equip[0] != "":
            r = g.equip[0].split("/")
            dicR = g.items.get(r[0])
            print(f"Right Hand: {dicR[int(r[1])][0]}")
        else:
            print("Right Hand: None")
        if g.equip[1] != "":
            l = g.equip[1].split("/")
            dicl = g.items.get(l[0])
            print(f"Left Hand: {dicl[int(l[1])][0]}")
        else:
            print("Left Hand: None")
        if g.equip[2] != "":
            a = g.equip[2].split("/")
            dica = g.items.get(a[0])
            print(f"Armor: {dica[int(a[1])][0]}")
        else:
            print("Armor: None")
        print("#"*100)
        input("Write Something to go back!\n")
    def title(str):
        banner = pyfiglet.figlet_format(str)
        print(banner)
    def draw_inv():
        page = 1
        LIST_ITEMS = 10
        items_info_list = []
        iterador_list_info = 0
        while True:
            clsp()
            Display.title("Inventory!")
            print("#"*100)
            reg = page * LIST_ITEMS
            iterador = reg - LIST_ITEMS
            ids = reg - LIST_ITEMS
            while (iterador <= reg and iterador <= len(g.inv)-1):
                none = ""
                inventario = g.inv[ids].split("/")
                name = inventario[0]
                dic = g.items[name]
                id_dic = int(inventario[1])
                if name == "potions":
                    prefix = f"Heal:{dic[id_dic][1]}"
                elif name == "swords":
                    prefix = f"Damage:{dic[id_dic][1]}"
                elif name == "Shield":
                    prefix = f"Armor:{dic[id_dic][1]}"
                info_intem = f"{id_dic}/{name}"
                items_info_list.append(f"{info_intem}")
                print(f"ID[{items_info_list.index(info_intem)}] -> {dic[id_dic][0]:15} : {prefix}")
                ids += 1
                iterador += 1
            iterador = reg - LIST_ITEMS
            print("#"*100)
            print(f"Page {page}")
            print("Commands: page, back, equip(e) or use(u)")
            option = input("Write Here:\n")
            if option == "back":
                break
            if option == "page":
                pg = int(input("Chose the Page:\n"))
                dif = len(g.inv) - (pg * LIST_ITEMS)
                if (pg <= 0 or  dif > LIST_ITEMS+1):
                    pg = 1
                page = pg
            if (option == "e" or option == "u"):
                comand = input(">ID Ex:. 1\n>")
                try:
                    
                    if items_info_list[int(comand)]:
                        comand_id = items_info_list[int(comand)]
                        cm_info = comand_id.split("/")
                        comand_id = cm_info[1] + "/" + cm_info[0]
                        id_item = int(cm_info[0])
                        nome_dic = cm_info[1]
                        #Logs.log(str(comand))
                        #Logs.log(str(g.inv))
                        #Logs.log(str(comand in g.inv))
                        if comand_id in g.inv:
                            if nome_dic == "swords":
                                ids_equip = 0
                            elif nome_dic == "potions":
                                ids_equip = 98
                            elif nome_dic == "Shield":
                                ids_equip = 1
                            elif nome_dic == "Armor":
                                ids_equip = 2
                            if ids_equip == 98:
                                lstPotiuon = g.items[nome_dic]
                                hpRegen = lstPotiuon[id_item][1]
                                if g.STATS["HP"] == g.STATS["MAXHP"]:
                                    print("You Have Full Health .-.")
                                else:
                                    g.inv.remove(comand_id)
                                g.STATS["HP"] = g.STATS["HP"] + hpRegen
                                if g.STATS["HP"] > g.STATS["MAXHP"]:
                                    g.STATS["HP"] = g.STATS["MAXHP"]
                                
                            else:
                                g.equip[ids_equip] = comand_id
                                Stats.set_atrib()
                except:
                    print("Something is wrong!")

    def draw_raw_Map():
        file = os.path.join("Assets","Maps","level"+str(g.STATS['Level'])+".gif")
        img = Image.open(file).convert("RGB")
        pix = img.load()
        for y in range(15):
            row =""
            r_m = []
            for x in range(100):
                temp_char = ""
                if pix[x,y] == (0,0,0):
                    r_m.append("█")
                    temp_char = "█"
                if pix[x,y] == (0,255,0):
                    r_m.append("≡")
                    temp_char = "≡"
                elif pix[x,y] == (255,255,255):
                    r_m.append(" ")
                    temp_char = " "
                elif pix[x,y] == (255,0,0):
                    r_m.append(g.PLAYER_SKIN)
                    temp_char = g.PLAYER_SKIN
                    g.PLAYER_X = x
                    g.PLAYER_Y = y
                row = row + temp_char
                g.Map[y+1] = r_m
            print(row)
    def display_options():
        print("Options:\nUse de wasd to move around the screen but will cost you a turn\nOr see your items with the key I and then press enter")
    def update_map():
        row = g.Map[g.PLAYER_Y+1]
        row[g.PLAYER_X] = " "
        file = os.path.join("Assets","Maps","level"+str(g.STATS['Level'])+".gif")
        img = Image.open(file).convert("RGB")
        pix = img.load()
        for y in range(15):
            row =""
            r_m = []
            for x in range(100):
                if pix[x,y] == (0,0,0):
                    r_m.append("█")
                elif pix[x,y] == (0,255,0):
                    r_m.append("≡")
                elif pix[x,y] == (255,255,255):
                    r_m.append(" ")
                elif pix[x,y] == (255,0,0):
                    r_m.append(" ")
                if (y == g.PLAYER_Y and x == g.PLAYER_X):
                    r_m[x-1] = g.PLAYER_SKIN
                g.Map[y+1] = r_m
        if g.NEW_GEN_ITEMS:
            for item in g.NEW_GEN_ITEMS:
                info = item.split("/")
                y, x=(int(info[0]),int(info[1]))
                row = g.Map[y]
                row[x] = "I"
                pass
        if g.NEW_GEN_MONSTER:
            for item in g.NEW_GEN_MONSTER:
                info = item.split("/")
                y, x=(int(info[0]),int(info[1]))
                display = (info[2])
                row = g.Map[y]
                row[x] = display
                pass
        for y in range(15):
            row = g.Map[y+1]
            r = ""
            for i in row:
                r = r + i
            print(r)
    def end_game():
        clsp()
        banner = pyfiglet.figlet_format("Congrats You Finish the Game")
        print(banner)
        print("For Now :)...")
        input("\nWrite Something to go to the start!!\n")
        g.GAME_WIN = True

class KeyEvent():
    def KeyPress(option):
        if (option == "d" and not g.Move_Lock.get('d')):
            g.PLAYER_X = g.PLAYER_X + 1
        elif (option == "a" and not g.Move_Lock.get('a')):
            g.PLAYER_X = g.PLAYER_X - 1
        elif (option == "w" and not g.Move_Lock.get('w')):
            g.PLAYER_Y = g.PLAYER_Y - 1
        elif (option == "s" and not g.Move_Lock.get('s')):
            g.PLAYER_Y = g.PLAYER_Y + 1

class Colision():
    def check_col():
        wall = "█"
        net_lv = "≡"
        item = "I"
        #print(g.Map[g.PLAYER_Y+1]) #Isto representa a linha do player
        row = g.Map[g.PLAYER_Y+1]
        row_Up = g.Map[g.PLAYER_Y]
        row_Down = g.Map[g.PLAYER_Y+2]
        #Logs.log(str(row[g.PLAYER_X] == item))
        ##########################################
        #If Inside the player
        if row[g.PLAYER_X+1] in  g.best_list:
            g.MONSTER_INFO = g.best_list.index(row[g.PLAYER_X+1])
            Func.remove_Monster(g.PLAYER_X+1,g.PLAYER_Y+1,row[g.PLAYER_X+1])
            g.IS_BATTLE = True
            pass
        elif row[g.PLAYER_X+1] == item:
            Func.item_pick_up(g.PLAYER_X-2,g.PLAYER_Y+1)
            pass
        ##########################################
        #UP Left CORNER (w a)
        if row_Up[g.PLAYER_X-2] in  g.best_list:
            g.MONSTER_INFO = g.best_list.index(row_Up[g.PLAYER_X-2])
            Func.remove_Monster(g.PLAYER_X-2,g.PLAYER_Y,row_Up[g.PLAYER_X-2])
            g.IS_BATTLE = True
            pass
        ##########################################
        #UP Right CORNER (w d)
        if row_Up[g.PLAYER_X] in  g.best_list:
            g.MONSTER_INFO = g.best_list.index(row_Up[g.PLAYER_X])
            Func.remove_Monster(g.PLAYER_X,g.PLAYER_Y,row_Up[g.PLAYER_X])
            g.IS_BATTLE = True
            pass
        ##########################################
        #Down Left CORNER (s a)
        if row_Down[g.PLAYER_X-2] in  g.best_list:
            g.MONSTER_INFO = g.best_list.index(row_Down[g.PLAYER_X-2])
            Func.remove_Monster(g.PLAYER_X-2,g.PLAYER_Y+2,row_Down[g.PLAYER_X-2])
            g.IS_BATTLE = True
            pass
        ##########################################
        #Down Right CORNER (s d)
        if row_Down[g.PLAYER_X] in  g.best_list:
            g.MONSTER_INFO = g.best_list.index(row_Down[g.PLAYER_X])
            Func.remove_Monster(g.PLAYER_X,g.PLAYER_Y+2,row_Down[g.PLAYER_X])
            g.IS_BATTLE = True
            pass
        ##########################################
        #Left (a)
        if row[g.PLAYER_X-2] == wall:
            g.Move_Lock['a'] = True
        elif row[g.PLAYER_X-2] == net_lv:
            Level.next_level()
            g.Move_Lock['a'] = False
        elif row[g.PLAYER_X-2] == item:
            Func.item_pick_up(g.PLAYER_X-2,g.PLAYER_Y+1)
            g.Move_Lock['a'] = False
        elif row[g.PLAYER_X-2] in g.best_list:
            g.MONSTER_INFO = g.best_list.index(row[g.PLAYER_X-2])
            Func.remove_Monster(g.PLAYER_X-2,g.PLAYER_Y+1,row[g.PLAYER_X-2])
            g.IS_BATTLE = True
            g.Move_Lock['a'] = False
        else:
            g.Move_Lock['a'] = False
        ############################################
        #right(d)
        if row[g.PLAYER_X] == wall:
            g.Move_Lock['d'] = True
        elif row[g.PLAYER_X] == net_lv:
            Level.next_level()
            g.Move_Lock['d'] = False
        elif row[g.PLAYER_X] == item:
            Func.item_pick_up(g.PLAYER_X,g.PLAYER_Y+1)
            g.Move_Lock['d'] = False
        elif row[g.PLAYER_X] in g.best_list:
            g.MONSTER_INFO = g.best_list.index(row[g.PLAYER_X])
            Func.remove_Monster(g.PLAYER_X,g.PLAYER_Y+1,row[g.PLAYER_X])
            g.IS_BATTLE = True
            g.Move_Lock['d'] = False
        else:
            g.Move_Lock['d'] = False
        ############################################
        #Up (w)
        if row_Up[g.PLAYER_X-1] == wall:
            g.Move_Lock['w'] = True
        elif row_Up[g.PLAYER_X-1] == net_lv:
            Level.next_level()
        elif row_Up[g.PLAYER_X-1] == item:
            Func.item_pick_up(g.PLAYER_X-1,g.PLAYER_Y)
        elif row_Up[g.PLAYER_X-1] in g.best_list:
            g.MONSTER_INFO = g.best_list.index(row_Up[g.PLAYER_X-1])
            Func.remove_Monster(g.PLAYER_X-1,g.PLAYER_Y,row_Up[g.PLAYER_X-1])
            g.IS_BATTLE = True
            g.Move_Lock['w'] = False
        else:
            g.Move_Lock['w'] = False
        ############################################
        #Down (s)
        if row_Down[g.PLAYER_X-1] == wall:
            g.Move_Lock['s'] = True
        elif row_Down[g.PLAYER_X-1] == net_lv:
            Level.next_level()
            g.Move_Lock['s'] = False
        elif row_Down[g.PLAYER_X-1] == item:
            Func.item_pick_up(g.PLAYER_X-1,g.PLAYER_Y+2)
            g.Move_Lock['s'] = False
        elif row_Down[g.PLAYER_X-1] in g.best_list:
            g.MONSTER_INFO = g.best_list.index(row_Down[g.PLAYER_X-1])
            Func.remove_Monster(g.PLAYER_X-1,g.PLAYER_Y+2,row_Down[g.PLAYER_X-1])
            g.IS_BATTLE = True
            g.Move_Lock['s'] = False
        else:
            g.Move_Lock['s'] = False
        ############################################
class Level:
    def next_level():
        g.STATS["Level"] = g.STATS['Level'] + 1
        path = "Assets/Maps/level"+str(g.STATS["Level"])+".gif"
        if os.path.exists(path):
            g.NEXT_LEVEL = True
        else:
            Display.end_game()

class Logs:
    def log(log):
        date = datetime.today().strftime('%Y_%m_%d')
        file = open(f"Logs\logs_{date}.txt", "a")
        file.write(log + "\n")

class Generation():
    def gen_item(n,types):

        item_list = g.items[types]
        for i in range(n):
            item_temp = random.choice(item_list)
            y = random.randint(1,15)
            x = random.randint(0,99)
            check = False
            while check == False:
                row = g.Map[y]
                Logs.log(f"[Item Spawn]x:{x} y:{y}")
                if (row[x] != "█" and row[x] != g.PLAYER_SKIN and row[x] != "I" and row[x] != "≡"):
                    row[x] = "I"
                    g.NEW_GEN_ITEMS.append(f"{y}/{x}/{item_temp}/{types}")
                    check = True
                y = random.randint(1,15)
                x = random.randint(0,99)
    def gen_monster(n):
        for i in range(n):
            item_temp = random.choice(g.best_list)
            y = random.randint(1,15)
            x = random.randint(0,100)
            check = False
            while check == False:
                row = g.Map[y]
                Logs.log(f"[Monster Spawn]x:{x} y:{y}")
                if (row[x] != "█" and row[x] != g.PLAYER_SKIN and row[x] != "I" and row[x] != "≡"):
                    row[x] = item_temp
                    g.NEW_GEN_MONSTER.append(f"{y}/{x}/{item_temp}")
                    check = True
                y = random.randint(1,15)
                x = random.randint(0,100)
    def clearGen():
        g.NEW_GEN_ITEMS.clear()
        g.NEW_GEN_MONSTER.clear()
class AI():
    def Monster_AI():
        IDs = 0
        for h in g.NEW_GEN_MONSTER:
            info = h
            item = info.split("/")
            x_m, y_m = (int(item[1]),int(item[0])) 
            dist = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m) - g.PLAYER_Y), 2)))
            if dist <= 5:
                AI.Move_Monster_Agr(IDs)
            else:
                AI.Move_random(IDs)
            IDs = IDs+1

    def Move_Monster_Agr(ID):
        new_Gen=[]
        info = g.NEW_GEN_MONSTER[ID]
        item = info.split("/")
        x_m,y_m = (int(item[1]),int(item[0]))
        #cima
        dist_up = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m-1) - g.PLAYER_Y), 2)))
        dist_down = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m+1) - g.PLAYER_Y), 2)))
        dist_left = math.sqrt((math.pow(((x_m + 1) - g.PLAYER_X), 2) + math.pow((y_m - g.PLAYER_Y), 2)))
        dist_right = math.sqrt((math.pow(((x_m - 1) - g.PLAYER_X), 2) + math.pow((y_m - g.PLAYER_Y), 2)))
        mine = min(dist_up,dist_down,dist_left,dist_right)
        values = [dist_up,dist_down,dist_left,dist_right]
        random.shuffle(values)
        row = g.Map[y_m]
        row_d = g.Map[y_m + 1]
        row_u = g.Map[y_m - 1]
        choose = False
        randoms = False
        iterador = 0
        maxim_attempts = 10000
        at = 0
        while (not choose and at < maxim_attempts):
            at = at +1
            if randoms == True:
                try:
                    values.remove(mine)
                except:
                    pass           
                mine = random.choice(values)
                iterador = iterador + 1
            if (dist_up == mine and row_u[x_m] != "█") and not choose:
                new_Gen.append(f"{str(y_m-1)}/{str(x_m)}/{item[2]}")
                choose = True
            else:
                mine = min(dist_down,dist_left,dist_right)
            if (dist_down == mine and row_d[x_m] != "█") and not choose:
                new_Gen.append(f"{str(y_m+1)}/{str(x_m)}/{item[2]}")
                choose = True
            else:
                mine = min(dist_left,dist_right)
            if (dist_left == mine and row[x_m+1] != "█") and not choose:
                new_Gen.append(f"{str(y_m)}/{str(x_m + 1)}/{item[2]}")
                choose = True
            else:
                mine = dist_right
            if (dist_right == mine and row[x_m-1] != "█") and not choose:
                new_Gen.append(f"{str(y_m)}/{str(x_m-1)}/{item[2]}")
                choose = True
            else:
                randoms = True
        if at >= maxim_attempts:
            Logs.log(f"[Monster AI ({item[2]})] Reatch Max Attempts")
            new_Gen.append(f"{str(y_m)}/{str(x_m)}/{item[2]}")
        Logs.log(f"[Monster Move ({item[2]})]Dist: {mine}")

        info = new_Gen[0]
        Logs.log(f"[New Gen List {str(ID)}] --> {info}")
        Logs.log(f"[Enemy Move]From [{g.NEW_GEN_MONSTER[ID]}] --> [{info}]")
        g.NEW_GEN_MONSTER[ID] = info
    def Move_random(ID):
        inforand = g.NEW_GEN_MONSTER[ID]
        Logs.log(f"[DEBUG]: {inforand}")
        itemrand = inforand.split("/")
        x,y = (int(itemrand[1]),int(itemrand[0]))
        skin = itemrand[2]
        choice = random.randint(1,5)
        row = g.Map[y]
        row_d = g.Map[y + 1]
        row_u = g.Map[y - 1]
        #1 up, 2 Down, 3 Left, 4 Right, 5 Nothing
        if (choice == 1 and row_u[x] != "█"):
            g.NEW_GEN_MONSTER[ID] = f"{y-1}/{x}/{skin}"
        elif (choice == 2 and row_d[x] != "█"):
            g.NEW_GEN_MONSTER[ID] = f"{y+1}/{x}/{skin}"
        elif (choice == 3 and row[x-1] != "█"):
            g.NEW_GEN_MONSTER[ID] = f"{y}/{x-1}/{skin}"
        elif (choice == 4 and row[x+1] != "█"):
            g.NEW_GEN_MONSTER[ID] = f"{y}/{x+1}/{skin}"
    def Monster_Turn(M_Stats):
        dmg = (5.6*M_Stats[4]+M_Stats[2])-(g.STATS.get("Def")*2)
        if dmg > 0:
            g.STATS['HP'] = int(g.STATS.get('HP') - dmg)

class Data():
    def save(slot):
        try:
            file = open(f'Saves/Save_{slot}.pkl', 'wb')
            pickle.dump([g.TURNS,g.Map,g.STATS,g.DEAD,g.PLAYER_X,g.PLAYER_Y,g.NEW_GEN_ITEMS,g.NEW_GEN_MONSTER,g.Move_Lock,g.inv,g.equip],file)
            Logs.log("[SAVE] Sucess Saving all Data")
            file.close()
            print("Save Done!")
        except:
            Logs.log("[ERROR] Slot Invalid")
    def load(slot):
        with open(f'Saves/Save_{slot}.pkl','rb') as f:
            g.TURNS,g.Map,g.STATS,g.DEAD,g.PLAYER_X,g.PLAYER_Y,g.NEW_GEN_ITEMS,g.NEW_GEN_MONSTER,g.Move_Lock,g.inv,g.equip = pickle.load(f)
        Logs.log("[LOAD] Sucess LOADING all Data")
    def find_Item(x_Item,y_Item):
        pos = 0
        for lis in g.NEW_GEN_ITEMS:
            str_info = lis.split("/")
            if (int(str_info[0]) == y_Item and int(str_info[1]) == x_Item):
                return pos
            pos +=1
        return False
    def attackMonster(M_Stats):
        dmg = g.STATS.get("Atk")-(M_Stats[3]*2)
        if dmg > 0:
            M_Stats[0] =M_Stats[0] - dmg
        else:
            M_Stats[0] -=1
        return M_Stats
    def is_dead(Player = False,Monster = False, M_stats = []):
        if Player:
            if g.STATS.get("HP") <= 0:
                g.DEAD = True
                return "PlayerDead"
        else:
            return None
        if Monster:
            if len(M_stats) > 0:
                if M_stats[0] <= 0:
                    return "MonsterDead"
        else:
            return None


