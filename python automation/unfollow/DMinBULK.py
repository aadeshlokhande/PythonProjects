import pyautogui as pg
import time

# time.sleep(3)
# print(pg.position())
# exit()
list = []
file = open('DataFollowers.txt', 'r')
for line in file:
    list.append(line.replace("\n", ""))

count = 0

def gola():
    try:
        x,y = pg.locateCenterOnScreen('gola.png',grayscale=True)
        pg.click(x,y)
        pg.move(100,0,duration=0.5)
    except:
        pg.hotkey("shift","home")
        time.sleep(1)
        pg.press("backspace")
        time.sleep(1)

msg = f"Hey guys...\nDo You want Learn python?\nIf yes then follow : @tech_in_seconds\n"

pg.click(x=502, y=138,interval=3)      # inbox

while True:
    for j in range(5):
        pg.click(x=268, y=200,interval=1)  # new msg
        pg.typewrite("tec_in_seconds",0.06)
        time.sleep(2)
        gola()

        for i in range(10):
            username = list[count]
            count = count + 1
            pg.typewrite(username,0.05)  # type usename
            time.sleep(6)
            gola()
            

        pg.click(x=428, y=152, interval=3)  # next
        pg.click(x=504, y=718)      # click on text input
        pg.typewrite(msg, interval=0.04)
                
    pg.click(x=80, y=136,interval=10)       # instagramm
    pg.moveTo(x=343, y=483,duration=5)      # center
    for i in range(5):
        pg.scroll(-10)
        time.sleep(1)
    pg.hotkey("ctrl","shift","r")        # refresh
    pg.click(x=502, y=138,interval=10)      # inbox