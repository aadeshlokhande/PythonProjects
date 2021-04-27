import os

path = r'C:\Users\CooL\Downloads\Telegram Desktop\ChatExport_14_06_2020\photos ori - Copy'
a = 1

for filename in os.listdir(path):
    os.rename(path + '\\' + filename,path + '\\' + str(a) + ".jpg")
    print(a)
    a +=1

