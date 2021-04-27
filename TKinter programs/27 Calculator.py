from tkinter import *

root = Tk()
# root.geometry("400x450")

root.title("Calculator By Aadesh Lokhande")
# root.wm_iconbitmap("1.ico")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        totaltext.configure(text = f"Answer is {value}", bg = "orange red")
        screen.update()

    elif text == "C":
        scvalue.set("")
        totaltext.configure(bg = "blue violet",text="Calculator By Aadesh Lokhande")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue =  StringVar()
scvalue.set("")

f1 = Frame(root, borderwidth =10, relief  =SUNKEN)


screen = Entry(f1, textvar = scvalue, font = "lucida 16 bold",bg = "grey30", fg = "white", bd = 10)
screen.grid(row = 0, column = 0, columnspan = 4, ipadx = 20)


b = Button(f1, text = "7", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 1, column = 0)
b.bind("<Button-1>", click)

b = Button(f1, text = "8", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 1, column = 1)
b.bind("<Button-1>", click)

b = Button(f1, text = "9", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 1, column = 2)
b.bind("<Button-1>", click)

b = Button(f1, text = "/", font = "lucida 16 bold", bg = "blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 1, column = 3)
b.bind("<Button-1>", click)


b = Button(f1, text = "4", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 2, column = 0)
b.bind("<Button-1>", click)

b = Button(f1, text = "5", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 2, column = 1)
b.bind("<Button-1>", click)

b = Button(f1, text = "6", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 2, column = 2)
b.bind("<Button-1>", click)

b = Button(f1, text = "*", font = "lucida 16 bold", bg = "blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 2, column = 3)
b.bind("<Button-1>", click)


b = Button(f1, text = "1", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 3, column = 0)
b.bind("<Button-1>", click)

b = Button(f1, text = "2", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 3, column = 1)
b.bind("<Button-1>", click)

b = Button(f1, text = "3", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 3, column = 2)
b.bind("<Button-1>", click)

b = Button(f1, text = "-", font = "lucida 16 bold", bg = "blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 3, column = 3)
b.bind("<Button-1>", click)


b = Button(f1, text = "C", font = "lucida 16 bold", bg = "crimson", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 4, column = 0)
b.bind("<Button-1>", click)

b = Button(f1, text = "0", font = "lucida 16 bold", bg = "Cadet blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 4, column = 1)
b.bind("<Button-1>", click)

b = Button(f1, text = "=", font = "lucida 16 bold", bg = "blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 4, column = 2)
b.bind("<Button-1>", click)

b = Button(f1, text = "+", font = "lucida 16 bold", bg = "blue", fg = "white", height = 2, width = 3, borderwidth =10)
b.grid(row = 4, column = 3)
b.bind("<Button-1>", click)

totaltext = Label(f1,
                  text = "Calculator By Aadesh Lokhande", height = 2, font = "lucida 12 bold",bg = "blue violet",fg = "white",width = 22,borderwidth =5,relief = SUNKEN)
totaltext.grid(row = 5, column = 0, columnspan = 4, ipadx = 55)

f1.pack(side = TOP)

root.mainloop()
