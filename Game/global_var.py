class Global:
    rows, cols = (15, 100)
    DISPLAY_INV = [[""]*cols]*rows
    dead = False
    WALL = []
    LEVEL = 0
    HP = 10
    PLAYER_X = 1
    PLAYER_Y = 1
    TURNS = 0
    PLAYER_SKIN = "P"
    Map = {
        1:[],
        2:[],
        3:[],
        4:[],
        5:[],
        6:[],
        7:[],
        8:[],
        9:[],
        10:[],
        11:[],
        12:[],
        13:[],
        14:[],
        15:[],
    }
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