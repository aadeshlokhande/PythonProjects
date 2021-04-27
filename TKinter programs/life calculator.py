from tkinter import *
from tkcalendar import *
import tkinter.messagebox

root = Tk()
space = " "
root.title("Life Calculator")
# root.geometry("1245x700+56+0")

MainFrame = Frame(root, bd = 10,width = 1000, height = 700, relief = RIDGE, bg = "cadet blue")
MainFrame.grid()

TitleFrame = Frame(MainFrame, bd = 10,width = 1000, height = 100, relief = RIDGE, bg = "cadet blue")
TitleFrame.grid(row =0, column= 0)

TopFrame3 = Frame(MainFrame, bd=5,width=1000, height=100, relief=RIDGE)
TopFrame3.grid(row =1, column= 0)

LeftFrame = Frame(TopFrame3, bd = 5,width = 1000, height = 100, relief = RIDGE, bg = "cadet blue")
LeftFrame.pack(side = LEFT)
LeftFrame1 = Frame(LeftFrame, bd = 5,width = 600, height = 180, relief = RIDGE)
LeftFrame1.pack(side = TOP, padx=10, pady=12)

RightFrame1 = Frame(TopFrame3, bd = 5,width = 320, height = 400, relief = RIDGE, bg = "cadet blue")
RightFrame1.pack(side=RIGHT, padx = 2)
RightFrame1a = Frame(RightFrame1, bd = 5,width = 310, height = 300,padx = 2, pady=2, relief = RIDGE)
RightFrame1a.pack(side=TOP, padx = 5, pady = 6)

lblTitle = Label(TitleFrame, font ="arial 50 bold", text = "Life Calculator",fg = "White",bg = "cadet blue", bd = 7)
lblTitle.grid(row = 0, column = 0, padx = 88)
# % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %

DOB = StringVar()
CDate = StringVar()
Days = StringVar()
Ages = StringVar()
Months = StringVar()
Weeks = StringVar()
Hours = StringVar()
Minutes = StringVar()
Seconds = StringVar()

# cal = Calendar(RightFrame1a,selectmode="day", year=1, month=1, day=1, date_pattern="dd/mm/yyyy",font="arial 16 bold")
# cal.grid(row=0, column=0, padx= 10)

cal = Calendar(RightFrame1a,selectmode="day", date_pattern="dd/mm/yyyy",font="arial 16 bold")
cal.grid(row=0, column=0, padx= 10)
# % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %
def Reset():
    # DOB.set("")
    # CDate.set("")
    Days.set("")
    Ages.set("")
    Months.set("")
    Weeks.set("")
    Hours.set("")
    Minutes.set("")
    Seconds.set("")
    entFirstName.delete(0, END)
    entLastName.delete(0,END)

def iExit():
    iExit = tkinter.messagebox.askyesno("Life Calculator", "Confirm If You Want To Exit")
    if iExit == 1:
        root.destroy()

def Results():
    CurrentDate = (DentCDate.get_date())
    DOBDate = (DentDOB.get_date())

    Day = (abs((CurrentDate-DOBDate).days))
    Days.set(str(Day))

    Age = int(Days.get())
    Agess = (Age/365)
    Ages.set(str("%.0f"%(Agess)))

    Weeks.set(str("%.0f" % (Age/7)))

    Months.set(str("%.0f" % (Age/30)))

    Hours.set("%.0f" % (Age*24))

    Minutes.set("%.0f" % (Age*24*60))

    Seconds.set("%.0f" % (Age*24*60*60))


# % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %

lblFirstName = Label(LeftFrame1, font= "arial 12 bold", text="First Name",anchor = "w", justify = LEFT,bd=2)
lblFirstName.grid(row=0,column=0,sticky=W,padx=5)
entFirstName = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,width = 44,bd=5)
entFirstName.grid(row=0,column=1)

lblLastName = Label(LeftFrame1, font= "arial 12 bold", text="Last Name",anchor = "w", justify = LEFT,bd=2)
lblLastName.grid(row=1,column=0,sticky=W,padx=5)
entLastName = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,width = 44,bd=5)
entLastName.grid(row=1,column=1)

lblDOB = Label(LeftFrame1, font= "arial 12 bold", text="Date of Birth",anchor = "w", justify = LEFT,bd=2)
lblDOB.grid(row=2,column=0,sticky=W,padx=5)
DentDOB = DateEntry(LeftFrame1, font= "arial 12 bold",textvariable = DOB, width = 42, bd=5, date_pattern = "dd/mm/yyyy")
DentDOB.grid(row=2,column=1)

lblCDate = Label(LeftFrame1, font= "arial 12 bold", text="Current Birth",anchor = "w", justify = LEFT,bd=2)
lblCDate.grid(row=3,column=0,sticky=W,padx=5)
DentCDate = DateEntry(LeftFrame1, font= "arial 12 bold",textvariable = CDate, width = 42, bd=5, date_pattern = "dd/mm/yyyy")
DentCDate.grid(row=3,column=1)

lblDays = Label(LeftFrame1, font= "arial 12 bold", text="Days",anchor = "w", justify = LEFT,bd=2)
lblDays.grid(row=4,column=0,sticky=W,padx=5)
entDays = Entry(LeftFrame1, font= "arial 12 bold",textvariable = Days,justify = LEFT,width = 44,bd=5)
entDays.grid(row=4,column=1)

lblAge = Label(LeftFrame1, font= "arial 12 bold", text="Age",anchor = "w", justify = LEFT,bd=2)
lblAge.grid(row=5,column=0,sticky=W,padx=5)
entAge = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,textvariable = Ages,width = 44,bd=5)
entAge.grid(row=5,column=1)

lblMonths = Label(LeftFrame1, font= "arial 12 bold", text="Months",anchor = "w", justify = LEFT,bd=2)
lblMonths.grid(row=6,column=0,sticky=W,padx=5)
entMonths = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,textvariable = Months,width = 44,bd=5)
entMonths.grid(row=6,column=1)

lblWeeks = Label(LeftFrame1, font= "arial 12 bold", text="Weeks",anchor = "w", justify = LEFT,bd=2)
lblWeeks.grid(row=7,column=0,sticky=W,padx=5)
entWeeks = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,textvariable = Weeks,width = 44,bd=5)
entWeeks.grid(row=7,column=1)

lblHours = Label(LeftFrame1, font= "arial 12 bold", text="Hours",anchor = "w", justify = LEFT,bd=2)
lblHours.grid(row=8,column=0,sticky=W,padx=5)
entHours = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,width = 44,bd=5,textvariable = Hours)
entHours.grid(row=8,column=1)

lblMinutes = Label(LeftFrame1, font= "arial 12 bold", text="Minutes",anchor = "w", justify = LEFT,bd=2)
lblMinutes.grid(row=9,column=0,sticky=W,padx=5)
entMinutes = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,width = 44,bd=5,textvariable = Minutes)
entMinutes.grid(row=9,column=1)

lblSeconds = Label(LeftFrame1, font= "arial 12 bold", text="Seconds",anchor = "w", justify = LEFT,bd=2)
lblSeconds.grid(row=10,column=0,sticky=W,padx=5)
entSeconds = Entry(LeftFrame1, font= "arial 12 bold", justify = LEFT,width = 44,bd=5,textvariable = Seconds)
entSeconds.grid(row=10,column=1)
# % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % % %

btnCalculate = Button(RightFrame1a, padx= 18, bd=15,font= "Helvetica 18 bold",fg= "white", width = 23,relief = RIDGE,
                      text = "Calculate",bg= "cadet blue", command = Results)
btnCalculate.grid(row=1, column=0, padx=3, pady = 2)

btnClear = Button(RightFrame1a, padx= 18, bd=15,font= "Helvetica 18 bold",fg= "white", width = 23,relief = RIDGE,
                  text = "Clear",bg= "cadet blue", command = Reset)
btnClear.grid(row=2, column=0, padx=3, pady = 2)

btnExit = Button(RightFrame1a, padx= 18, bd=15,font= "Helvetica 18 bold",fg= "white", width = 23,relief = RIDGE,
                 text = "Exit",bg= "red", command = iExit)
btnExit.grid(row=3, column=0, padx=3, pady = 2)

root.mainloop()