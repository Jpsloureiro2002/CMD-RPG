from global_var import Global as g
import os
from PIL import Image
import random
import math
from datetime import datetime
import pickle

class Display:
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
        #print(g.Map[g.PLAYER_Y+1]) #Isto representa a linha do player
        row = g.Map[g.PLAYER_Y+1]
        row_Up = g.Map[g.PLAYER_Y]
        row_Down = g.Map[g.PLAYER_Y+2]
        
        if row[g.PLAYER_X-2] == wall:
            g.Move_Lock['a'] = True
            #Logs.log(f"[Player Pos Row({g.PLAYER_Y+1}) and Col({g.PLAYER_X-1})] Value is = Wall")
        else:
            #Logs.log(f"[Player Pos Row({g.PLAYER_Y+1}) and Col({g.PLAYER_X-1})] Value is = Space")
            g.Move_Lock['a'] = False
        # o x+1 vai ser a pos do Player o x+2 vai ser a pos a direita do player isto por causa do temp na criação do mapa
        if row[g.PLAYER_X] == wall:
            g.Move_Lock['d'] = True
        else:
            g.Move_Lock['d'] = False
        if row_Up[g.PLAYER_X-1] == wall:
            g.Move_Lock['w'] = True
        else:
            g.Move_Lock['w'] = False
        if row_Down[g.PLAYER_X-1] == wall:
            g.Move_Lock['s'] = True
        else:
            g.Move_Lock['s'] = False
            
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
                if (row[x] != "█" and row[x] != g.PLAYER_SKIN) and row[x] != "I":
                    row[x] = "I"
                    g.NEW_GEN_ITEMS.append(f"{y}/{x}/{item_temp}")
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
                if (row[x] != "█" and row[x] != g.PLAYER_SKIN) and row[x] != "I":
                    row[x] = item_temp
                    g.NEW_GEN_MONSTER.append(f"{y}/{x}/{item_temp}")
                    check = True
                y = random.randint(1,15)
                x = random.randint(0,100)

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

