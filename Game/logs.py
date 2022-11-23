import time
file = open("logs.txt","r")
while 1:
    where = file.tell()
    line = file.readline()
    line = line.replace("\n","")
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        print (line) # already has newline
