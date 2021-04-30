import pyautogui as pg
import time

# time.sleep(3)
# print(pg.position())
# exit()
list = []
a = open('DataFollowers.txt', 'r')
for aa in a:
    list.append(aa.replace("\n", ""))
count = 1
for username in list:
    # msg = f"Hello {username},\nDo You want Learn python?\nIf yes then follow : @tech_in_seconds\n"
    msg = f"Hello {username},\nfollow : @tech_in_seconds\n"
    pg.click(x=268, y=200)  # new msg
    time.sleep(1)
    pg.typewrite(username, 0.05)  # type usename
    time.sleep(3)
    pg.click(x=332, y=257)  # click to id
    time.sleep(1)
    pg.click(x=428, y=152)  # next
    time.sleep(5)
    pg.click(x=504, y=718)
    pg.typewrite(msg, interval=0.05)
    print(count,"Send message to",username)
    count = count + 1
    time.sleep(10)
