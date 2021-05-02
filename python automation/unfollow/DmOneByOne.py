import pyautogui as pg
import time

# time.sleep(3)
# print(pg.position())
# exit()
list = []
a = open('DataFollowers.txt', 'r')
for aa in a:
    list.append(aa.replace("\n", ""))
count = 0

pg.click(x=502, y=138,interval=3)      # inbox
while True:
    for i in range(30):
        username = list[count]
        msg = f"Hello {username}\nDo You want Learn python?\nIf yes then follow : @tech_in_seconds\n"
        pg.click(x=268, y=200,interval=1)  # new msg
        pg.typewrite(username, 0.2,)  # type usename
        time.sleep(3)
        pg.click(x=332, y=257,interval=2)  # click to id
        pg.click(x=428, y=152, interval=5)  # next
        pg.click(x=504, y=718)      # click on text input
        pg.typewrite(msg, interval=0.1)
        print(count+1,"Send message to",username) # type msg
        count = count + 1     
    pg.click(x=80, y=136,interval=10)       # instagramm
    pg.moveTo(x=343, y=483,duration=5)      # center
    for i in range(5):
        pg.scroll(-8)
        time.sleep(1)
    # pg.click(x=90, y=57)        # refresh
    pg.click(x=502, y=138,interval=10)      # inbox