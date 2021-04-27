from tkinter import *
root = Tk()
root.geometry("555x555")
f1 = Frame(root,bg = "red", borderwidth = 5, relief = SUNKEN)
f1.pack(side = LEFT, fill = "y")

f2 = Frame(root,bg = "gray", borderwidth = 5, relief = SUNKEN)
f2.pack(side = TOP, fill = "x")

l = Label(f1, text = "Project aadesh lokhande", font = ( "comicsansms",12, "bold"))
l.pack(pady = 3, side = LEFT)

l = Label(f2, text = "this is corono time", fg = "red")
l.pack(pady = 3)





root.mainloop()