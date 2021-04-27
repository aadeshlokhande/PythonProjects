import pyautogui as pg
import time
from datetime import datetime
#print(pg.position())
#exit()

#---------------uploadpost------------------------

now = datetime.now()
current_time = int(now.strftime("%H"))
if current_time > 12 and current_time < 18:
    cap = "Good afternoon Guys..."
elif current_time > 18 and current_time < 21:
    cap = "Good Evening Guys..."
elif current_time > 4 and current_time < 12:
    cap = "Good Morning Guys..."
else:
    cap = "Good Night Guys..."

caption= f'''{cap}\n
Follow and share post if you like...\n

@asian_girls_villa\n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
. \n
#cutegirl #cute #girl #kawaii #anime #love #kawaiigirl #beautiful #follow #animegirl #art #like #model #cosplay #prettygirl #pretty #smile #sexy #instagood #sexygirl #beauty #beautifulgirl #selfie #girls #hotgirl #manga #drawing #photography #followme #bhfyp \n
@somya_daundkar @avneetkaur_13 @zannarassi @francescafarago @riya.kulkarni @sexeducation @hot.asian.gravure @redchilliesent @hot.portraits @xx_hot_couple_romance_xx @hot.actresses.hotties @hot_latinas18 @hottest185'''

time.sleep(3)
pg.click(20,20)                                             #click to menu btn
time.sleep(1)
pg.typewrite("vivaldi",0.2)                                 #type vivaldi
pg.press("enter")                                           #press enter
time.sleep(15)
pg.click(227,719)                                           #click to plus btn
time.sleep(2)
pg.press("enter")                                           #press enter
time.sleep(3)
pg.click(388,130)                                           #click to next
time.sleep(2)
pg.click(181,189)                                           #click to caption feild
time.sleep(2)
pg.typewrite(caption,0.03)
pg.click(388,130)                                           #click to share
time.sleep(5)
print("Image Uploaded")
#
# time.sleep(3)
# print(pg.position())
# exit()
#-------------------delete image-------------------

pg.hotkey("alt","z")
time.sleep(3)
pg.click(83,368)                        # other location
time.sleep(2)
pg.click(83,368)                        # other location
time.sleep(2)
pg.click(335,150)                       # data
time.sleep(2)
pg.doubleClick(241, 107)                 # Aadesh lokhande
time.sleep(1)
pg.doubleClick(241,107)                 # study material
time.sleep(1)
pg.doubleClick(707,243)                 # w3school
time.sleep(1)
pg.doubleClick(253,157)                 # insta post
time.sleep(2)
pg.click(253,157)                   # select pic
time.sleep(2)
pg.hotkey("shift","del")
time.sleep(2)
pg.press("enter")
pg.click(21,24)
time.sleep(2)
pg.click(1351,16)
print("Image Deleted")
