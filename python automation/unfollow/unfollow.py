import pyautogui as pg
import time
# time.sleep(3)
# print(pg.position())
# exit()
x=361
y=506
i = 1

while True:    
    try:
        a,b = pg.locateCenterOnScreen("following.png")
        pg.click(int(a),int(b))
        pg.moveTo(x,y)
        time.sleep(1)
        c,d = pg.locateCenterOnScreen("unfollow.png")
        pg.click(int(c),int(d))
        pg.moveTo(x,y)
        print("follow : ",i)
        time.sleep(37)
        i+=1
    # except:
        pg.moveTo(x,y,1)
        pg.scroll(-4)
        # pg.press("pagedown")
        # time.sleep(1)
        print("Scroll...")
    except:
        time.sleep(2)