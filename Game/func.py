from global_var import Global as g
import os
from PIL import Image


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
                temp_char = " "
                if pix[x,y] == (0,0,0):
                    r_m.append("█")
                    temp_char = "█"
                elif pix[x,y] == (255,255,255):
                    r_m.append(" ")
                    temp_char = " "
                if (y == g.PLAYER_Y and x == g.PLAYER_X):
                    r_m.append(g.PLAYER_SKIN)
                    temp_char = g.PLAYER_SKIN
                row = row + temp_char
                g.Map[y+1] = r_m
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
        wall = "█"
        #print(g.Map[g.PLAYER_Y+1]) #Isto representa a linha do player
        row = g.Map[g.PLAYER_Y+1]
        row_Up = g.Map[g.PLAYER_Y]
        row_Down = g.Map[g.PLAYER_Y+2]
        if row[g.PLAYER_X-1] == wall:
            g.Move_Lock['a'] = True
        else:
            g.Move_Lock['a'] = False
        # o x+1 vai ser a pos do Player o x+2 vai ser a pos a direita do player isto por causa do temp na criação do mapa
        if row[g.PLAYER_X+2] == wall:
            g.Move_Lock['d'] = True
        else:
            g.Move_Lock['d'] = False
        if row_Up[g.PLAYER_X] == wall:
            g.Move_Lock['w'] = True
        else:
            g.Move_Lock['w'] = False
        if row_Down[g.PLAYER_X] == wall:
            g.Move_Lock['s'] = True
        else:
            g.Move_Lock['s'] = False
            
class Logs:
    def log(log):
        file = open("logs.txt", "w")
        file.write(log + "\n")


        
