from tkinter import *
import pyautogui as pg

root = Tk()
# root.geometry("315x340")
# root.maxsize(315,340)
# root.minsize(315,340)
root.title("Numpad")


def click(event):
    global scvalue
    text = event.widget.cget("text")
    shownums.update()


f1 = Frame(root,bg = "grey", borderwidth =10, relief  =SUNKEN)
f1.pack(side = BOTTOM)


scvalue =  StringVar()
scvalue.set("")

shownums = Text(f1, width = 20, height = 7, textvar = scvalue,font = "lucida 16 bold",fg = "white",bd = 10)
shownums.grid(row = 0, column = 0, columnspan = 4)

btn = Button(f1, text = "1", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 1, column = 0)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "2", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 1, column = 1)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "3", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 1, column = 2)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "/", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 1, column = 3)
btn.bind("<Button-1>", click)

btn = Button(f1, text = "4", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 2, column = 0)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "5", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 2, column = 1)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "6", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 2, column = 2)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "x", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 2, column = 3)
btn.bind("<Button-1>", click)

btn = Button(f1, text = "7", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 3, column = 0)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "8", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 3, column = 1)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "9", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 3, column = 2)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "-", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 3, column = 3)
btn.bind("<Button-1>", click)

btn = Button(f1, text = ".", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 4, column = 0)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "0", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 4, column = 1)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "+", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 4, column = 2)
btn.bind("<Button-1>", click)
btn = Button(f1, text = "=", height = 2, width = 3, borderwidth =10,font = "lucida 16 bold",fg = "white",bg = "grey10", relief = SUNKEN)
btn.grid(row = 4, column = 3)
btn.bind("<Button-1>", click)

root.mainloop()
