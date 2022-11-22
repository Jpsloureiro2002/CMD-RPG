class Global:
    rows, cols = (15, 100)
    MAP = [[""]*cols]*rows
    TEMP = [[""]*cols]*rows
    DISPLAY_INV = [[""]*cols]*rows
    dead = False
    WALL = []
    LEVEL = 0
    HP = 10
    PLAYER_X = 1
    PLAYER_Y = 1
    TURNS = 0
    PLAYER_SKIN = "■"
    Move_Lock = {
        'w':False,
        's':False,
        'd':False,
        'a':False,
    }
    inv = {
        '0':'n',
        '1':'n',
        '2':'n',
        '3':'n',
        '4':'n'
    }
    items={
        "swords":[("knife",5),("iron_sword",10)],
        "potions":[("life_b",3),("life_g",5)]
    }
    bestiary={
        "$":[10,4,0],
        "B":[30,7,0],
    }
    skins={
        "Default":"■",
        "F":"ƒ"
    }