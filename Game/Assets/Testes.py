"""

def Move_Monster_Agr():
        i = 0
        new_Gen=[]
        for info in g.NEW_GEN_MONSTER:
            item = info.split("/")
            x_m,y_m = (int(item[1]),int(item[0]))
            #cima
            dist_up = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m-1) - g.PLAYER_Y), 2)))
            dist_down = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m+1) - g.PLAYER_Y), 2)))
            dist_left = math.sqrt((math.pow(((x_m + 1) - g.PLAYER_X), 2) + math.pow((y_m - g.PLAYER_Y), 2)))
            dist_right = math.sqrt((math.pow(((x_m - 1) - g.PLAYER_X), 2) + math.pow((y_m - g.PLAYER_Y), 2)))
            mine = min(dist_up,dist_down,dist_left,dist_right)
            values = [dist_up,dist_down,dist_left,dist_right]
            random.shuffle(values)
            row = g.Map[y_m]
            row_d = g.Map[y_m + 1]
            row_u = g.Map[y_m - 1]
            choose = False
            randoms = False
            iterador = 0
            maxim_attempts = 10000
            at = 0
            while (not choose and at < maxim_attempts):
                at = at +1
                if randoms == True:
                    try:
                        values.remove(mine)
                    except:
                        pass           
                    mine = random.choice(values)
                    iterador = iterador + 1
                if (dist_up == mine and row_u[x_m] != "█") and not choose:
                    new_Gen.append(f"{str(y_m-1)}/{str(x_m)}/{item[2]}")
                    choose = True
                else:
                    mine = min(dist_down,dist_left,dist_right)
                if (dist_down == mine and row_d[x_m] != "█") and not choose:
                    new_Gen.append(f"{str(y_m+1)}/{str(x_m)}/{item[2]}")
                    choose = True
                else:
                    mine = min(dist_left,dist_right)
                if (dist_left == mine and row[x_m+1] != "█") and not choose:
                    new_Gen.append(f"{str(y_m)}/{str(x_m + 1)}/{item[2]}")
                    choose = True
                else:
                    mine = dist_right
                if (dist_right == mine and row[x_m-1] != "█") and not choose:
                    new_Gen.append(f"{str(y_m)}/{str(x_m-1)}/{item[2]}")
                    choose = True
                else:
                    randoms = True
            if at >= maxim_attempts:
                Logs.log(f"[Monster AI ({item[2]})] Reatch Max Attempts")
                new_Gen.append(f"{str(y_m)}/{str(x_m)}/{item[2]}")
            Logs.log(f"[Monster Move ({item[2]})]Dist: {mine}")
        it = 0
        for info in new_Gen:
            Logs.log(f"[New Gen List {str(it)}] --> {info}")
            Logs.log(f"[Enemy Move]From [{g.NEW_GEN_MONSTER[it]}] --> [{info}]")
            g.NEW_GEN_MONSTER[it] = info
            it = it + 1
    def Move_Monster_Afraid():
        i = 0
        new_Gen=[]
        for info in g.NEW_GEN_MONSTER:
            item = info.split("/")
            x_m,y_m = (int(item[1]),int(item[0]))
            #cima
            dist_up = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m-1) - g.PLAYER_Y), 2)))
            dist_down = math.sqrt((math.pow((x_m - g.PLAYER_X), 2) + math.pow(((y_m+1) - g.PLAYER_Y), 2)))
            dist_left = math.sqrt((math.pow(((x_m + 1) - g.PLAYER_X), 2) + math.pow((y_m - g.PLAYER_Y), 2)))
            dist_right = math.sqrt((math.pow(((x_m - 1) - g.PLAYER_X), 2) + math.pow((y_m - g.PLAYER_Y), 2)))
            mine = max(dist_up,dist_down,dist_left,dist_right)
            values = [dist_up,dist_down,dist_left,dist_right]
            random.shuffle(values)
            row = g.Map[y_m]
            row_d = g.Map[y_m + 1]
            row_u = g.Map[y_m - 1]
            choose = False
            randoms = False
            iterador = 0
            maxim_attempts = 10000
            at = 0
            while (not choose and at < maxim_attempts):
                at = at +1
                if randoms == True:
                    try:
                        values.remove(mine)
                    except:
                        pass           
                    mine = random.choice(values)
                    iterador = iterador + 1
                if (dist_up == mine and row_u[x_m] != "█") and not choose:
                    new_Gen.append(f"{str(y_m-1)}/{str(x_m)}/{item[2]}")
                    choose = True
                else:
                    mine = max(dist_down,dist_left,dist_right)
                if (dist_down == mine and row_d[x_m] != "█") and not choose:
                    new_Gen.append(f"{str(y_m+1)}/{str(x_m)}/{item[2]}")
                    choose = True
                else:
                    mine = max(dist_left,dist_right)
                if (dist_left == mine and row[x_m+1] != "█") and not choose:
                    new_Gen.append(f"{str(y_m)}/{str(x_m + 1)}/{item[2]}")
                    choose = True
                else:
                    mine = dist_right
                if (dist_right == mine and row[x_m-1] != "█") and not choose:
                    new_Gen.append(f"{str(y_m)}/{str(x_m-1)}/{item[2]}")
                    choose = True
                else:
                    randoms = True
            if at >= maxim_attempts:
                Logs.log(f"[Monster AI ({item[2]})] Reatch Max Attempts")
        it = 0
        for info in new_Gen:
            Logs.log(f"[New Gen List {str(it)}] --> {info}")
            Logs.log(f"[Enemy Move]From [{g.NEW_GEN_MONSTER[it]}] --> [{info}]")
            g.NEW_GEN_MONSTER[it] = info
            it = it + 1
            

"""