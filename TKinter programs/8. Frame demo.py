from tkinter import *

root = Tk()
root.geometry("300x300")
f1 = Frame(root,bg = "grey", borderwidth =10, relief  =SUNKEN)
f1.pack(side = LEFT, fill  = "y")

lbl = Label(f1, text = "Gandu hai tu BSDK", bg = "yellow")
lbl.pack(side = LEFT, )

f2 = Frame(root, bg = "grey", borderwidth = 10, relief = SUNKEN)
f2.pack(side = TOP, fill = "x")

lbl1 = Label(f2, text= "tu bhi kam nhi hai")
lbl1.pack()


root.mainloop()