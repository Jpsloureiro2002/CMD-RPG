import os
from global_var import Global as g
from func import *
res = lambda : os.system('mode con: cols=100 lines=30')
clsp = lambda : os.system('cls')



game_Start = True
Display.draw_raw_Map()

while (game_Start and not g.dead):
    #res()
    g.TEMP[:]
    Logs.log(f"{g.PLAYER_X}/{g.PLAYER_Y}")
    Display.update_map()
    Display.display_options()
    Option = input("")
    Colision.check_col()
    KeyEvent.KeyPress(Option)



        
    
    
    