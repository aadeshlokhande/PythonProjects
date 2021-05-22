import pyautogui as pg
from time import sleep
from chatid import username
# Note:
# 1) screen and vs code 50-50 screen
# 2) page zoom 100%
# 3) dark theme enable


# sleep(2)
# print(pg.position())
# exit()

usernames = username()
counter = 0
# print(usernames)
# print(len(use))
for i in range(len(usernames)):
    pg.click(323,139)           # click on search
    sleep(1)

    pg.typewrite(usernames[i],0.05)
    sleep(2)

    pg.click(294,200)           # click on username
    sleep(3)

    pg.scroll(-5)
    sleep(1)

    x,y = pg.locateCenterOnScreen("grid.png")
    pg.click(x,y+100,1)
    sleep(1)

    try:                            # like
        x,y = pg.locateCenterOnScreen('like.png')
        pg.click(x,y)
        sleep(1)
        counter = counter + 1
    except:
        pass

    try:                            # save
        x,y = pg.locateCenterOnScreen('save.png')
        pg.click(x,y)
        sleep(1)
    except:
        pass
    print(counter,usernames[i])
    pg.click(646,144)               # close post
    sleep(1)