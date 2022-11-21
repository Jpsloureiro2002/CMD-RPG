import os
from global_var import Global as g
from func import *
res = lambda : os.system('mode con: cols=100 lines=30')



game_Start = True

while (game_Start and not g.dead):
    res()
    Display.draw_raw_Map()
    Display.display_options()
    

    Pause = input("")