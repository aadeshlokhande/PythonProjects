from tkinter import *
root = Tk()
root.geometry("222x250")

root.title("Application Form")
# funtion for button
def submit():

    if okvalue.get() == 1:
        ready = "Yes"
    else:
        ready = "No"

    f = open("read.txt", 'w')
    f.write("Name = "+namevalue.get()+"\n"+
            "Phone = "+phonevalue.get()+"\n"+
            "Education = "+educationvalue.get()+"\n"+
            "Gender = "+gendervalue.get()+"\n"+
            "Ready = "+ ready +
            "\n-x-x-x-x-x-x-x-x-x-\n"
            )
    f.close()


Label(root, text = "Application", font = "comicsansms 15 bold", pady = 15).grid(row = 0, column = 3)
# Heading

name = Label(root, text = "Name ")
# text for our application
phone = Label(root, text = "Phone ")
education = Label(root, text = "Education ")
gender = Label(root, text = "Gender ")

# pack text in our application
name.grid(row= 1, column = 2)
phone.grid(row= 2, column = 2)
education.grid(row= 3, column = 2)
gender.grid(row= 4, column = 2)


# tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
educationvalue = StringVar()
gendervalue = StringVar()
okvalue = IntVar()


# Entry for a application
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
educationentry = Entry(root, textvariable = educationvalue)
genderentry = Entry(root, textvariable = gendervalue)


#  Packing Entries
nameentry.grid(row = 1,column = 3)
phoneentry.grid(row = 2,column = 3)
educationentry.grid(row = 3,column = 3)
genderentry.grid(row = 4,column = 3)

# Checkbox and packing
ok = Checkbutton(text = " Are you Ready? ", variable = okvalue)
ok.grid(row = 6, column = 3)


# button and packing & assign in cammand
Button(text = "submit", command = submit).grid(row = 7, column = 3)


root.mainloop()
