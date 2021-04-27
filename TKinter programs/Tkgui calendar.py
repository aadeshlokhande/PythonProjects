from tkinter import *
from tkcalendar import *
root = Tk()
# root.geometry("")
root.title("Calendar")
root.configure(bg="cadet blue")

def goto():
    pass
    # cal.configure(year=year.get(), month=month.get(), day=day.get())

frameTop = Frame(root, bg="Cadet blue")
frameTop.pack()

cal = Calendar(frameTop, selectmode="day", date_pattern="dd/mm/yyyy", font="arial 16 bold")
cal.grid(row=0, column=0)

BottomFrame = Frame(root, bg="cadet blue")
BottomFrame.pack()

Label(BottomFrame, text = "Day",font = "arial 14 bold",fg = "white", bg = "cadet blue", ).grid(row=0, column=0)
day = Spinbox(BottomFrame,from_ = 1, to = 31, width = 10)
day.grid(row = 1, column=0)

Label(BottomFrame, text = "Month",font = "arial 14 bold",fg = "white", bg="cadet blue").grid(row=0, column=1)
month = Spinbox(BottomFrame,from_ = 1, to = 12, width = 10)
month.grid(row = 1, column=1)

Label(BottomFrame, text = "Year",font = "arial 14 bold",fg = "white", bg = "cadet blue").grid(row=0, column=2)
year = Spinbox(BottomFrame,from_ = 1000, to = 3000, width = 10)
year.grid(row = 1, column=2)

btnFrame = Frame(root, bg = "cadet blue")
btnFrame.pack()
btnGoto = Button(btnFrame, text ="GoTo", font = "lucida 14 bold", bg= "powder blue",
                 fg = "Black",relief = SUNKEN, bd=7, command = goto)
btnGoto.pack(padx =10, pady=10, side = LEFT)

btnclose = Button(btnFrame, text ="Close", font = "lucida 14 bold", bg= "powder blue",
                  fg="Black",relief=SUNKEN, bd=7, command=exit)
btnclose.pack(padx=10, pady=10)

root.mainloop()
