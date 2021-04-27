from tkinter import *

root = Tk()

root.title("Button packing")
f1 = Frame(root, borderwidth=15, bg = "grey", relief = GROOVE)
f1.pack(side = TOP, fill = "x")

def odd():
    for i in range(1,50,2):
        print(i)
btn2 = Button(f1, text = "odd",bg = "black" ,fg= "red", command = odd)
btn2.pack(side = TOP, fill = "x")

def even():
    for i in range(0,50,2):
        print(i)
btn4 = Button(f1, text = "Even number",bg = "black", fg= "red", command = even)
btn4.pack(side = BOTTOM, fill = "x")

root.mainloop()
