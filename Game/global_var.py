class Global:
    rows, cols = (15, 100)
    DISPLAY_INV = [[""]*cols]*rows
    DEAD = False
    PLAYER_X = 1 #SAVE
    PLAYER_Y = 1 #SAVE
    TURNS = 0 #SAVE
    NEXT_LEVEL = False
    IS_BATTLE = False
    MONSTER_INFO = None
    INFO_TEXT = ""
    NEW_GEN_ITEMS = [] #SAVE
    NEW_GEN_MONSTER = [] #SAVE
    GAME_WIN = False
    STATS_DEF={
        'HP':10,
        'MAXHP':10,
        'LV':0,
        'XP':0,
        'MAXP':0,
        'Slot':'-1',
        'Def':0,
        'Level':0,
        'Atk':10
    }
    STATS={
        'HP':10,
        'MAXHP':10,
        'LV':0,
        'XP':0,
        'MAXP':0,
        'Slot':'-1',
        'Def':0,
        'Level':0,
        'Atk':10
    } #SAVE
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
    } #SAVE
    Move_Lock = {
        'w':False,
        's':False,
        'd':False,
        'a':False,
    }
    #0-Swords 1-SHields 2- Armor
    inv = ["swords/0","potions/0"] #SAVE
    equip_def = {
        99:'hand',
        0:'',
        1:'',
        2:''
    } 
    equip = {
        99:'hand',
        0:'',
        1:'',
        2:''
    } #SAVE
    items={
        "swords":[("Dagger",3),("Knife",5),("Iron Sword",10)],
        "potions":[("Life Potion S",3),("Life Potion M",5)],
        "Shield":[("Wood Shield",2)],
        "Armor":[("Wood Armor",10)]
    }
    best_list = ["$","B","&"]
    # [HP,MAXHP,ATACK,DEF,LV]
    # *NOT YET A FEATURE
    # If LV is 0 then gen a monster with more or less the LV of the player*
    bestiary={
        0:[10,10,4,4,1],
        1:[30,30,7,3,2],
        2:[10,10,2,3,5]
    }
    skins={
        "Default":"■",
        "f":"ƒ",
        "Percent":"%"
    }
    PLAYER_SKIN = skins['Default'] #SAVE