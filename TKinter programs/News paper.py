from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Cars Paper")

root.geometry("700x700")

def aadesh():
    pass



data = ["lambo", "bmw", "jaguar"]

texts = []
photos = []
for i in data:
    with open(f"{i}.txt") as f:
        text = f.read()
        texts.append(text)

    image = Image.open(f"{i}.png")
    #TODO: resize the img
    image = image.resize((222,222), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width = 600, height = 20)
Label(root, text = "CARS PAPER",  font = "lucida 24 bold" ).pack()
Label(root, text = "September 12 2020",  font = "lucida 9 bold" ).pack()
f0.pack()

f1 = Frame(root, width = 60, height = 20)
Label(f1, text = texts[0], padx =22, pady = 2).pack(side = "left")
Label(f1, image = photos[0], anchor = "e", padx= 22, pady = 2).pack()
f1.pack(anchor = "w")

f2 = Frame(root, width = 600, height = 20)
Label(f2, text = texts[1], padx =22, pady = 2).pack(side = "left")
Label(f2, image = photos[1], anchor = "e", padx= 22, pady = 2).pack()
f2.pack(anchor = "w")

f3 = Frame(root, width = 600, height = 20)
Label(f3, text = texts[2], padx =22, pady =2).pack(side = "left")
Label(f3, image = photos[2], anchor = "e", padx= 22, pady = 2).pack()
f3.pack(anchor = "w")

root.mainloop()