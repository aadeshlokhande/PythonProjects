import pyautogui as pg
import time
x=357
y=446
i = 1

while True:    
    try:
        a,b = pg.locateCenterOnScreen("follow.png")
        pg.click(x,y,interval=1)
        pg.click(int(a),int(b))
        pg.moveTo(x,y)
        time.sleep(15)
        print("follow : ",i)
        i+=1
    except:
        pg.moveTo(x,y,1)
        pg.scroll(-4)
        time.sleep(1)
        print("Scroll...")