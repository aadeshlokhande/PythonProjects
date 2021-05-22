import pyautogui as pg
import time

# time.sleep(3)
# print(pg.position())
# exit()
x=450
y=410
i = 1

while True:    
    try:
        a,b = pg.locateCenterOnScreen("follow.png")
        pg.click(x,y,interval=1)
        pg.click(int(a),int(b))
        pg.moveTo(x,y)
        print("follow : ",i)
        time.sleep(60)
        i+=1
    except:
        pg.moveTo(x,y,1)
        pg.scroll(-4)
        time.sleep(1)
        print("Scroll...")

# # Printing a String
# print("TECH_IN_SECONDS")
# # OUTPUT : TECH_IN_SECONDS