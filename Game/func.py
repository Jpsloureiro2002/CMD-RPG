from global_var import Global as g
import pathlib
import os
from PIL import Image


class Display:
    def draw_raw_Map():
        file = os.path.join("Assets","Maps","level"+str(g.LEVEL)+".gif")
        img = Image.open(file).convert("RGB")
        pix = img.load()
        for y in range(15):
            row =""
            for x in range(100):
                if pix[x,y] == (0,0,0):
                    g.MAP[y][x] = "█"
                elif pix[x,y] == (255,255,255):
                    g.MAP[y][x] = " "
                elif pix[x,y] == (255,0,0):
                    g.MAP[y][x] = g.PLAYER_SKIN
                    g.PLAYER_X = x
                    g.PLAYER_Y = y
                row = row + g.MAP[y][x] 
            print(row)
    def display_options():
        print("Options:\nUse de wasd to move around the screen but will cost you a turn\nOr see your items with the key I and then press enter")
    def update_map():
        g.TEMP[g.PLAYER_Y][g.PLAYER_X] = " "
        file = os.path.join("Assets","Maps","level"+str(g.LEVEL)+".gif")
        img = Image.open(file).convert("RGB")
        pix = img.load()
        g.WALL.clear()
        for y in range(15):
            row =""
            for x in range(100):
                if pix[x,y] == (0,0,0):
                    g.TEMP[y][x] = "█"
                    g.WALL.append(f"{y}/{x}")               
                elif pix[x,y] == (255,255,255):
                    g.TEMP[y][x] = " "
                if (x == g.PLAYER_X and g.PLAYER_Y == y):
                    g.TEMP[y][x] = g.PLAYER_SKIN
                row = row + g.TEMP[y][x]
            print(row)
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
        Wall = "█"
        print(g.TEMP[g.PLAYER_Y][g.PLAYER_X])
        x = input("")
        
        if g.TEMP[g.PLAYER_Y-1][g.PLAYER_X] == Wall:
            g.Move_Lock.update({"w":False})
        else:
            g.Move_Lock.update({"w":True})
            
class Logs:
    def log(log):
        file = open("logs.txt", "w")
        file.write(log + "\n")


        
