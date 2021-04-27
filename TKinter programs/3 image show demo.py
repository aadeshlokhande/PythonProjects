from tkinter import *

root = Tk()

# photoImage
img = PhotoImage(file = "1.png")

label = Label(image = img)
label.pack()


root.mainloop()