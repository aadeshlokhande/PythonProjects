from tkinter import *
root = Tk()
root.geometry("555x555")
f1 = Frame(root,bg = "grey", borderwidth = 5, relief = SUNKEN)
f1.pack(side = LEFT, anchor = "nw")

def hello():
    print("Hello aadesh")

def aadesh():
    print("Long press")

b1 = Button(f1, text = "bhula" ,fg = "red", command = hello)
b1.pack()

b2 = Button(f1, text = "bhula" ,fg = "red")
b2.pack()

b3 = Button(f1, text = "bhula" ,fg = "red")
b3.pack()

b4 = Button(f1, text = "bhula" ,fg = "red")
b4.pack()

b5 = Button(f1, text = "bhula" ,fg = "red")
b5.pack()







root.mainloop()

