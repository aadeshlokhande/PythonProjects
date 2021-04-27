import pyautogui as pg
import time

time.sleep(3)

for i in range(5):
    pg.hotkey('ctrl', 'a')
    time.sleep(1)
    pg.hotkey('ctrl', 'x')
    time.sleep(1)
    pg.press('backspace')
    time.sleep(1)
    pg.press('down')
    time.sleep(1)
    pg.press('enter')
    time.sleep(1)
    pg.hotkey('ctrl', 'v')
    time.sleep(2)

