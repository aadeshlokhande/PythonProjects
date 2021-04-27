import tkinter.messagebox as mb
from tkinter import *

root = Tk()
root.geometry()
root.title("Tic Tac Toe")
root.configure(bg = "Cadet blue")

Tops = Frame(root, bg = "Cadet Blue", pady = 2 , width = 1350, height = 100, relief = RIDGE)
Tops.grid(row = 0, column = 0)

lblTitle = Label(Tops, font = "arial 50 bold", text = "Tic Tac Toe", bd = 12, bg = "cadet blue", fg = "cornsilk",justify = CENTER )
lblTitle.grid(row = 0, column = 0)

MainFrame = Frame(root, bg = "Powder Blue", pady = 2, width = 1350, height = 600, bd = 10, relief = RIDGE)
MainFrame.grid(row = 1, column = 0)

LeftFrame = Frame(MainFrame, bd = 10,width = 560, height = 500, pady = 2, padx = 10, bg = "cadet blue", relief = RIDGE )
LeftFrame.pack(side = LEFT)

RightFrame = Frame(MainFrame, bd = 10,width = 560, height = 500, pady = 2, bg = "cadet blue", relief = RIDGE )
RightFrame.pack(side = RIGHT)

RightFrame1 = Frame(RightFrame, bd = 10,width = 560, height = 200, pady = 2,  bg = "cadet blue", relief = RIDGE )
RightFrame1.grid(row =0, column = 0)

RightFrame2 = Frame(RightFrame, bd = 10,width = 560, height = 200, pady = 2, padx = 10, bg = "cadet blue", relief = RIDGE )
RightFrame2.grid(row = 1, column = 0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

click = True

btns = StringVar()

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()

    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()


def scorekeeper():
    if (btn1["text"]=="X" and (btn2["text"])=="X" and (btn3["text"])=="X"):
        btn1.configure(bg="powder blue")
        btn2.configure(bg="powder blue")
        btn3.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn4["text"]=="X" and (btn5["text"])=="X" and (btn6["text"])=="X"):
        btn4.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn6.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn7["text"]=="X" and (btn8["text"])=="X" and (btn9["text"])=="X"):
        btn7.configure(bg="powder blue")
        btn8.configure(bg="powder blue")
        btn9.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn1["text"]=="X" and (btn4["text"])=="X" and (btn7["text"])=="X"):
        btn1.configure(bg="powder blue")
        btn4.configure(bg="powder blue")
        btn7.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn2["text"] == "X" and (btn5["text"]) == "X" and (btn8["text"]) == "X"):
        btn2.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn8.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn3["text"] == "X" and (btn6["text"]) == "X" and (btn9["text"]) == "X"):
        btn3.configure(bg="powder blue")
        btn6.configure(bg="powder blue")
        btn9.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn1["text"] == "X" and (btn5["text"]) == "X" and (btn9["text"]) == "X"):
        btn1.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn9.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn3["text"] == "X" and (btn5["text"]) == "X" and (btn7["text"]) == "X"):
        btn3.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn7.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = n + 1
        PlayerX.set(score)
        box = mb.showinfo("winner X", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn1["text"] == "O" and (btn2["text"]) == "O" and (btn3["text"]) == "O"):
        btn1.configure(bg="powder blue")
        btn2.configure(bg="powder blue")
        btn3.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn4["text"] == "O" and (btn5["text"]) == "O" and (btn6["text"]) == "O"):
        btn4.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn6.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn7["text"] == "O" and (btn8["text"]) == "O" and (btn9["text"]) == "O"):
        btn7.configure(bg="powder blue")
        btn8.configure(bg="powder blue")
        btn9.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn1["text"] == "O" and (btn4["text"]) == "O" and (btn7["text"]) == "O"):
        btn1.configure(bg="powder blue")
        btn4.configure(bg="powder blue")
        btn7.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn2["text"] == "O" and (btn5["text"]) == "O" and (btn8["text"]) == "O"):
        btn2.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn8.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn3["text"] == "O" and (btn6["text"]) == "O" and (btn9["text"]) == "O"):
        btn3.configure(bg="powder blue")
        btn6.configure(bg="powder blue")
        btn9.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn1["text"] == "O" and (btn5["text"]) == "O" and (btn9["text"]) == "O"):
        btn1.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn9.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()

    if (btn3["text"] == "O" and (btn5["text"]) == "O" and (btn7["text"]) == "O"):
        btn3.configure(bg="powder blue")
        btn5.configure(bg="powder blue")
        btn7.configure(bg="powder blue")
        n = int(PlayerO.get())
        score = n + 1
        PlayerO.set(score)
        box = mb.showinfo("winner O", "You Have Just Won A Game")
        if box == "ok":
            reset()




def reset():
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "

    btn1.configure(bg = "gainsboro")
    btn2.configure(bg = "gainsboro")
    btn3.configure(bg = "gainsboro")
    btn4.configure(bg = "gainsboro")
    btn5.configure(bg = "gainsboro")
    btn6.configure(bg = "gainsboro")
    btn7.configure(bg = "gainsboro")
    btn8.configure(bg = "gainsboro")
    btn9.configure(bg = "gainsboro")

def Newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)



lblPlayerX = Label(RightFrame1, font = "arial 40 bold", text = "Player X : ", bg = "cadet blue", padx = 2, pady =2)
lblPlayerX.grid(row = 0, column = 0, sticky = W)

txtPlayerX = Label(RightFrame1, font = "arial 40 bold", bd =2, fg ="black",textvariable = PlayerX, width = 14,justify = LEFT)
txtPlayerX.grid(row = 0, column = 1, pady = 2, padx = 2)


lblPlayerO = Label(RightFrame1, font = "arial 40 bold", text = "Player O : ", bg = "cadet blue", padx = 2, pady =2)
lblPlayerO.grid(row = 1, column = 0, sticky = W)

txtPlayerO = Label(RightFrame1, font = "arial 40 bold", bd =2, fg ="black",textvariable = PlayerO, width = 14,justify = LEFT)
txtPlayerO.grid(row = 1, column = 1, pady = 2, padx = 2)

btnReset = Button(RightFrame2, text = "Reset", font = "arial 40 bold", height = 1,width =20, bg = "gainsboro",command = reset)
btnReset.grid(row =0, column = 0,padx = 10, pady = 10)

btnNewGame = Button(RightFrame2, text = "New Game", font = "arial 40 bold", height = 1,width =20,padx = 10, pady = 10, bg = "gainsboro",command = Newgame)
btnNewGame.grid(row =1, column = 0,padx = 10, pady = 10)


btn1 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn1))
btn1.grid(row =1, column = 0, sticky = S+N+E+W)
# btn1.bind("<button-1>", checker)


btn2 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn2))
btn2.grid(row =1, column = 1, sticky = S+N+E+W)

btn3 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn3))
btn3.grid(row =1, column = 2, sticky = S+N+E+W)

btn4 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn4))
btn4.grid(row =2, column = 0, sticky = S+N+E+W)

btn5 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn5))
btn5.grid(row =2, column = 1, sticky = S+N+E+W)

btn6 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn6))
btn6.grid(row =2, column = 2, sticky = S+N+E+W)

btn7 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn7))
btn7.grid(row =3, column = 0, sticky = S+N+E+W)

btn8 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn8))
btn8.grid(row =3, column = 1, sticky = S+N+E+W)

btn9 = Button(LeftFrame, text = " ", font = "times 26 bold", height = 3,width =8, bg = "gainsboro",command = lambda:checker(btn9))
btn9.grid(row =3, column = 2, sticky = S+N+E+W)

root.mainloop()