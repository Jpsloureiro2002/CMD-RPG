import time
import os
clsp = lambda : os.system("cls")
while True:
    clsp()
    file = open("logs.txt", "r")
    lis = file.readlines()
    for l in lis:
        print(l)
