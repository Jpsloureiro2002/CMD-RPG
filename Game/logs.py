import time
import os
from datetime import datetime
clsp = lambda : os.system('cls')
clsp()
date = datetime.today().strftime('%Y_%m_%d')
creat = open(f"Logs/logs_{date}.txt","a")
file = open(f"Logs/logs_{date}.txt","r")
while 1:
    where = file.tell()
    line = file.readline()
    line = line.replace("\n","")
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        print (line) # already has newline
