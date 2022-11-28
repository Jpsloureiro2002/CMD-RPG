class Global:
    rows, cols = (15, 100)
    DISPLAY_INV = [[""]*cols]*rows
    DEAD = False
    PLAYER_X = 1
    PLAYER_Y = 1
    TURNS = 0
    NEXT_LEVEL = False
    INFO_TEXT = ""
    NEW_GEN_ITEMS = []
    NEW_GEN_MONSTER = []
    GAME_WIN = False
    STATS={
        'HP':10,
        'MAXHP':10,
        'LV':0,
        'XP':0,
        'Slot':'-1',
        'Def':0,
        'Level':0,
        'Atk':1
    }
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
    #0-Swords 1-SHields 2- Armor
    inv = ["swords/0","potions/0"]
    equip = {
        99:'hand',
        0:'',
        1:'',
        2:''
    }
    items={
        "swords":[("Dagger",3),("Knife",5),("Iron Sword",10)],
        "potions":[("Life Potion S",3),("Life Potion M",5)],
        "Shield":[("Wood Shield",2)],
        "Armor":[("Wood Armor",10)]
    }
    best_list = ["$","B","&"]
    # [HP,ATACK,DEF]
    bestiary={
        0:[10,4,4],
        1:[30,7,5],
        2:[10,2,3]
    }
    skins={
        "Default":"■",
        "f":"ƒ",
        "Percent":"%"
    }
    PLAYER_SKIN = skins['Default']