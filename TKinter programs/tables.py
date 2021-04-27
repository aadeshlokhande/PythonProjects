from tkinter import *

def table():
    shownums.delete(1.0, "end")
    try :
        shownums.configure(fg="white")
        if (minvalue.get()+10) > (maxvalue.get()):
            for i in range(1,11):
                for j in range(minvalue.get(), maxvalue.get() + 1):
                    shownums.insert("end", str(i*j))
                    shownums.insert("end", "\t")
                shownums.insert("end","\n")
        else:
            shownums.configure(fg="orange")
            titlelbl.configure(text = "Bhosdike")
            titlelbl.configure(fg = "red")
            shownums.insert("end", f"this Program can show you only 10 tables. {maxvalue.get()} is a big number. enter {minvalue.get()+9} or below")
    except:
        shownums.configure(fg = "red")
        shownums.insert("end", "Enter a valid input")

root =Tk()
root.title("Tables in two numbers")
root.geometry("1300x400")

# Frame
frame = Frame(root)
frame.pack()

titlelbl = Label(frame,text = "Enter A Numbers",fg = "green" , font = "lucida 18 bold")
titlelbl.pack()

minvalue = IntVar()
maxvalue = IntVar()

minvalue.set("")
maxvalue.set("")

minentry = Entry(frame, textvariable = minvalue,font = "lucida 14 bold" )
minentry.pack(side = LEFT)
maxentry = Entry(frame, textvariable = maxvalue,font = "lucida 14 bold")
maxentry.pack(side= LEFT)

btn = Button(root,width = 15, text = "Submit", font = "lucida 12 bold",
                bd = 10,fg = "white",bg = "green", relief =SUNKEN, command = table)
btn.pack()

shownums = Text(root, width=20, height=17, font="lucida 16 bold",
                fg="yellow", bg="grey50", relief=SUNKEN, bd=10)
shownums.pack(fill = X)

root.mainloop()