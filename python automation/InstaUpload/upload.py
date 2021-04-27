import pyautogui as pg
import time
import os

def pos():
    time.sleep(3)
    print(pg.position())
    exit()
# pos()

#---------------uploadpost------------------------
caption= '''Follow and share post if you like...\n

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

folderPath = "/home/aadesh/Videos/Study_Material/Python_PDF/Insta_post"

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

#-------------------delete image-------------------
os.system(f"xdg-open {folderPath}")
time.sleep(2)
pg.click(221,108)
time.sleep(1)
pg.hotkey("shift","del")
time.sleep(1)
pg.press("enter")
pg.click(1347,21)
time.sleep(1)
pg.click(1347,21)
print("Image Deleted")