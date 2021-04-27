import PIL
from PIL import Image
import os

mywidth = 2000
source_dir = 'C:\Users\CooL\Desktop\GOW'
destination_dir = 'C:\Users\CooL\Desktop\GOW1'

def resize_pic(old_pic, new_pic, mywidth):
    img = Image.open(old_pic)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
    img.save(new_pic)


def entire_directory(source_dir, destination_dir, width):
    files = os.listdir(source_dir)

    for file in files:
        old_pic = source_dir + file
        new_pic = destination_dir + file

        print("old_pic = " , old_pic)
        print("new_pic = " , new_pic)

