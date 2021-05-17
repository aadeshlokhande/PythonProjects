# pip3 install pyautogui
import pyautogui as pg
import time


# time.sleep(2)
# print(pg.position())
# exit()
for aa in range(5):
    pg.click(x=302, y=140)
    time.sleep(2)
    pg.typewrite("bhumii_jain",0.09)
    time.sleep(2)
    pg.click(x=225, y=200)
    time.sleep(2)
    pg.click(x=225, y=200)
    time.sleep(2)
    pg.click(x=104, y=685)
    time.sleep(2)
    try:
        a,b = pg.locateCenterOnScreen("like.png")
        pg.click(a,b)
    except:
        pass
    time.sleep(2)
    pg.click(x=644, y=142)
    time.sleep(2)