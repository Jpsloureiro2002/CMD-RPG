list ={
    "inv" : ["sword/1", "sword/0"]
}
items = {
    "sword" : [("axe", 10),("sword", 5)]
}
x = "#" * 100
print(x)
i = 0
for y in list["inv"]:
    item_info = y.split("/")
    ids = int(item_info[1])
    ilist = items[item_info[0]] 
    print(f"[{i}]Item Name: {ilist[ids][0]:3} -> Dmg: {ilist[ids][1]}")
    i +=1