from tkinter import *
root = Tk()
root.geometry("200x200")
root.title("Bhula")


def name():
    print(fnamevalue.get(), lnamevalue.get())

fname = Label(root, text = "Name    = ")
lname = Label(root, text = "Surname = ")
fname.grid()
lname.grid(row = 1)

# variable classes in kinter
# BooleanVar, DoubleVar,IntVar, StringVar

fnamevalue = StringVar()
lnamevalue = StringVar()

fnameentry = Entry(root, textvariable = fnamevalue)
lnameentry = Entry(root, textvariable = lnamevalue)

fnameentry.grid(row = 0, column = 1)
lnameentry.grid(row = 1, column = 1)

Button(root, text = "Submit", command = name).grid()

root.mainloop()
