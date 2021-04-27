from tkinter import *
from tkinter import messagebox as mb

i = 0

def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    box = mb.askokcancel(f"Abara Ka Dabara", f"Your Number Is : {decimal}")
    if box == "ok":
        exit()

mainbinary = ""

def yes():
    global mainbinary
    mainbinary = "1" + mainbinary
    show()

def no():
    global mainbinary
    mainbinary = "0" + mainbinary
    show()

def show():
    global i
    list = [
        "1, 3, 5, 7, 9,\n11, 13, 15, 17, 19,\n21, 23, 25, 27, 29,\n31, 33, 35, 37, 39,\n41, 43, 45, 47, 49,\n51, 53, 55, 57, 59.",
        "2, 3, 6, 7, 10,\n11, 14, 15, 18, 19,\n22, 23, 26, 27, 30,\n31, 34, 35, 38, 39,\n42, 43, 46, 47, 50,\n51, 54, 55, 58, 59.",
        "4, 5, 6, 7, 12,\n13, 14, 15, 20, 21,\n22, 23, 28, 29, 30,\n31, 36, 37, 38, 39,\n44, 45, 46, 47, 52,\n53, 54, 55, 60.",
        "8, 9, 10, 11, 12,\n13, 14, 15, 24, 25,\n26, 27, 28, 29, 30,\n31, 40, 41, 42, 43,\n44, 45, 46, 47, 56,\n57, 58, 59, 60.",
        "16, 17, 18, 19, 20,\n21, 22, 23, 24, 25,\n26, 27, 28, 29, 30,\n31, 48, 49, 50, 51,\n52, 53, 54, 55, 56,\n57, 58, 59, 60.",
        "32, 33, 34, 35, 36,\n37, 38, 39, 40, 41,\n42, 43, 44, 45, 46,\n47, 48, 49, 50, 51,\n52, 53, 54, 55, 56,\n57, 58, 59, 60."]

    # shownums.configure(text = "", font = "lucida 16 bold")
    subtitletxt.configure(text="Don't Forget Your Number", font="lucida 16 bold")
    if i < 6:
        shownums.configure(text=list[i])
        i += 1
    else:

        binary = int(mainbinary[0:6])
        binaryToDecimal(binary)

root = Tk()
root.title("Guess The Number")
# root.geometry("365x430")
# root.minsize(365, 430)
# root.maxsize(365, 430)

# top frame
frameTop = Frame(root)
frameTop.pack(side=TOP, fill=BOTH)

titletxt = Label(frameTop, text="Magic Box", fg="deep pink", font="lucida 25 bold")
titletxt.pack(fill=BOTH)

subtitletxt = Label(frameTop, text="Think About A Number In\nRange 0 To 60", font="lucida 12 bold")
subtitletxt.pack(fill=BOTH)

frameMiddle = Frame(root)
frameMiddle.pack(fill=BOTH)

shownums = Label(frameMiddle, width=20, height=7, bd=10, font="lucida 15 bold",
                 text=f"1 2 3 4 5 6 7 8 9 10\n11 12 13 14 15 16 17 18 19 20\n21 22 23 24 25 26 27 28 29 30\n31 32 33 34 35 36 37 38 39 40\n41 42 43 44 45 46 47 48 49 50\n51 52 53 54 55 56 57 58 59 60")
shownums.pack(fill=X, padx=3, pady=5)

frameBottom = Frame(root)
frameBottom.pack(fill=BOTH)

Label(frameBottom, text="Is Your Number In The List?", fg="grey1",
      font="lucida 12 bold").grid(row=0, column=0, columnspan=2)

yesBtn = Button(frameBottom, text="Yes", bg="cadet blue",
                font="lucida 10 bold", relief=RIDGE, width=15, bd=10, command=yes)
yesBtn.grid(row=1, column=0)

noBtn = Button(frameBottom, text="No", bg="cadet blue",
               font="lucida 10 bold", relief=RIDGE, width=15, bd=10, command=no)
noBtn.grid(row=1, column=1)

exitBtn = Button(frameBottom, text="Exit", bg="cadet blue",
                 font="lucida 10 bold", relief=RIDGE, width=35, bd=10, command=exit)
exitBtn.grid(row=2, column=0, columnspan=2)

root.mainloop()