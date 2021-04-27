# open all photos in your tabs from wallpaperflare.com
import pyautogui as pg
import time
# print(pg.position())
time.sleep(2)
# exit()
for i in range(45):
    pg.click(1213, 303)                         #click on download for current screen
    time.sleep(8)
    pg.click(524, 602)                          #click on download wallpaper
    time.sleep(1)
    pg.hotkey('ctrl', 'w')
    time.sleep(3)
