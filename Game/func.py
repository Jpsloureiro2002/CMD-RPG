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
        print("\n")
        print("Options:\nUse de wasd to move around the screen but will cost you a turn\nOr see your items with the key I and then press enter")
    def update_map():
        g.MAP[g.PLAYER_Y,g.PLAYER_X] = " "
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
                if (x == g.PLAYER_X and g.PLAYER_Y == y):
                    g.MAP[y][x] = g.PLAYER_SKIN
                row = row + g.MAP[y][x]
            print(row)       