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
        y_ = 0
        x_ = 0
        for y in g.TEMP:
            row =""
            x_ = 0
            for x in y:
                if pix[x_,y_] == (0,0,0):
                    g.TEMP[y_][x_] = "1"
                    g.WALL.append(f"{y}/{x}")               
                elif pix[x_,y_] == (255,255,255):
                    g.TEMP[y_][x_] = "0"
                if (x == g.PLAYER_X and g.PLAYER_Y == y):
                    g.TEMP[y_][x_] = g.PLAYER_SKIN
                x_ = x_ +1
                row = row + x
            y_ = y_ + 1
        for i in g.TEMP:
            r = ""
            for j in i:
                r = r + j
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
        Wall = "█"
        for row in g.TEMP:
            r = ""
            for col in row:
                r = r + col
            print(r)
        x = input("")
        
        if g.TEMP[g.PLAYER_Y-1][g.PLAYER_X] == Wall:
            g.Move_Lock.update({"w":True})
        else:
            g.Move_Lock.update({"w":False})
            
class Logs:
    def log(log):
        file = open("logs.txt", "w")
        file.write(log + "\n")


        
