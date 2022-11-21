import os
from global_var import Global as g
from func import *
res = lambda : os.system('mode con: cols=100 lines=30')



game_Start = True
Display.draw_raw_Map()
while (game_Start and not g.dead):
    res()
    #fix
    Display.draw_raw_Map()
    Display.display_options()
    
    Option = input("")
    if Option == "d":
        g.PLAYER_X = g.PLAYER_X + 1
    Display.update_map()
    Display.display_options()