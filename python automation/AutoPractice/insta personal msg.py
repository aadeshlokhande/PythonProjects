import pyautogui as pg
import time as t

print(pg.position())
link = "https://youtu.be/xqTTlLpu9ck"
# Point(x=440, y=368), x=398, y=353
for i in range(0,30):
    pg.move(118, 593,1)
    t.sleep(1)
    pg.click(118, 593)
    t.sleep(1)
    pg.move(822,400)
    pg.write(f'''Do You want Earn Money Online, Are You Intrested?\n admin is a Boy so dont show your lust in chat box... \nEnjoy the posts\nthank you\n {link}''',0.0)
    # pg.move(612,729)
    t.sleep(1)
    pg.click(612,729)
    t.sleep(1)

    print(i)