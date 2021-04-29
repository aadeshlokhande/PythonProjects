import pyautogui as pg 
import time

list = []
a = open('DataFollowers.txt','r')
for aa in a:
    list.append(aa.replace("\n", ""))

count = 0
countfile = open("count.txt",'w')

for username in list:
    msg = f"Hello {username},\nDo You want Learn python?\nIf yes then follow : @tech_in_seconds\n"
    pg.click(x=268, y=168)              #new msg
    time.sleep(1)
    pg.typewrite(username,0.05)    #type usename
    time.sleep(3)
    pg.click(x=312, y=235)                  #click to id
    time.sleep(1)
    pg.click(x=434, y=123)                          #next
    time.sleep(5)
    pg.click(x=497, y=724)
    pg.typewrite(msg,interval=0.05)
    countfile.write(str(count))
    count = count + 1
h