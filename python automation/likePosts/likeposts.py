import pyautogui as pg
import time

num_of_posts = int(input("Number of posts = "))

for i in range(num_of_posts):
    try:
        unfollow = pg.locateCenterOnScreen("like.png")
        a = str(unfollow)[8:11]
        b = str(unfollow)[15:18]
        pg.click(int(a), int(b))
    except:
        pg.press("right")
    pg.moveTo(100,100)
    print(i)
    time.sleep(1)