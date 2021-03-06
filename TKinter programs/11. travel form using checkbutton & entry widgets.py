from tkinter import *
root = Tk()
root.geometry("250x250")
root.title("Dance Academy Form")

# function
def submit():
    with open("addmission list.txt", "a") as r:
        if checkvalue.get() == 0:
            r.write(f"{namevalue.get()},{surenamevalue.get()},{agevalue.get()},{classvalue.get()},{addressvalue.get()},{mobilevalue.get()},{emailvalue.get()},No.\n")
        else:
            r.write(f"{namevalue.get()},{surenamevalue.get()},{agevalue.get()},{classvalue.get()},{addressvalue.get()},{mobilevalue.get()},{emailvalue.get()},Yes.\n")

# Title
# title = Label(root, text = "Dance Academy Form", ).grid()

# Labels
namelbl = Label(root, text = "Name ", fg = "blue").grid(row = 2, column = 0)
surenamelbl = Label(root, text = "Surename ", fg = "blue").grid(row = 3, column = 0)
agelbl = Label(root, text = "Age ", fg = "blue").grid(row = 4, column = 0)
classlbl = Label(root, text = "Class ", fg = "blue").grid(row = 5, column = 0)
addresslbl = Label(root, text = "Address ", fg = "blue").grid(row = 6, column = 0)
mobilelbl = Label(root, text = "Mobile ", fg = "blue").grid(row = 7, column = 0)
emaillbl = Label(root, text = "Gmail ", fg = "blue").grid(row = 8, column = 0)

# value
namevalue = StringVar()
surenamevalue = StringVar()
agevalue = StringVar()
classvalue = StringVar()
addressvalue = StringVar()
mobilevalue = StringVar()
emailvalue = StringVar()
checkvalue = IntVar()

# Entry
nameentry = Entry(root, textvariable = namevalue).grid(row = 2, column = 1)
surenameentry = Entry(root, textvariable = surenamevalue).grid(row = 3, column = 1)
ageentry = Entry(root, textvariable = agevalue).grid(row = 4, column = 1)
classentry = Entry(root, textvariable = classvalue).grid(row = 5, column = 1)
addressentry = Entry(root, textvariable = addressvalue).grid(row = 6, column = 1)
mobileentry = Entry(root, textvariable = mobilevalue).grid(row = 7, column = 1)
emailentry = Entry(root, textvariable = emailvalue).grid(row =8, column = 1)

# Checkbutton
checkentry = Checkbutton(text = "Are you Intrested?", variable = checkvalue).grid(row = 9, column = 1)

# Button
btn = Button(root, text = "Submit", command = submit).grid()

root.mainloop()