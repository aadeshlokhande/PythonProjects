import pyautogui as pg
import time

print(pg.position())

for i in range(0,100):
    follow= pg.click(x=320, y=328)
    time.sleep(2)
    pg.scroll(-1)
    time.sleep(1)
    print(i)