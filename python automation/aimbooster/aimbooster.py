import pyautogui as pg
import time

time.sleep(3)
while True:
    x,y = pg.locateCenterOnScreen("aim.png",region = (), confidence=0.9)
    pg.click(x,y)