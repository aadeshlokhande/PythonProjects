from tkinter import *
import calendar

root = Tk()
root.geometry("400x400")
root.minsize(200,450)
root.title("Calendar")

def show():
    cal.delete(1.0, END)
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y,m)
    cal.insert("end", output)

def clear():
    cal.delete(1.0, END)

def exit():
    root.destroy()

mtxt = Label(root, text = "Month : ", font = "verdana 10 bold")
mtxt.pack(fill = X, padx = 30)

month = Spinbox(root,from_ = 1, to = 12, width = 10)
month.pack(fill = X, padx = 30)

ytxt = Label(root, text = "Year : ", font = "verdana 10 bold")
ytxt.pack(fill = X, padx = 30)

year = Spinbox(root,from_ = 1900, to = 3000, width = 10)
year.pack(fill = X, padx = 30)

cal = Text(root, width = 33, height = 8,font = "lucida 12 bold",fg = "white",bg = "cadet blue", relief = SUNKEN, bd = 10)
cal.pack(fill = X, padx = 30, pady = 5)

show =  Button(root, text = "Show",bg = "cadet blue", font = "lucida 10 bold", relief = RIDGE,width = 15, bd = 10, command = show)
show.pack(fill = X, padx = 30)

clear =  Button(root, text = "Clear",bg = "cadet blue", font = "lucida 10 bold", relief = RIDGE,width = 15, bd = 10, command = clear)
clear.pack(fill = X, padx = 30)

exit =  Button(root, text = "Exit",bg = "cadet blue", font = "lucida 10 bold", relief = RIDGE,width = 15, bd = 10, command = exit)
exit.pack(fill = X, padx = 30)

root.mainloop()