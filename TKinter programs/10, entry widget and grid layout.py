from tkinter import *
root= Tk()
root.title("Addmission Form")

def submit():
    print(f"name is {name_value.get()}")
    print(f"surename is {surename_value.get()}")
    print(f"age is {age_value.get()}")
    print(f"mobile number is {mobile_value.get()}")
    print(f"email is {email_value.get()}")

# name, surname, age, mobile, email

name_lbl = Label(root, text = "Name").grid(row = 0, column = 0)
surename_lbl = Label(root, text = "Surename").grid(row = 1, column = 0)
age_lbl = Label(root, text = "Age").grid(row = 2, column = 0)
mobile_lbl = Label(root, text = "Mobile").grid(row = 3, column = 0)
email_lbl = Label(root, text = "Email").grid(row = 4, column = 0)

# veriable class in TKinter
name_value = StringVar()
surename_value = StringVar()
age_value = StringVar()
mobile_value = StringVar()
email_value = StringVar()

# Entry widgets
name_entry = Entry(root, textvariable = name_value)
surename_entry = Entry(root, textvariable = surename_value)
age_entry = Entry(root, textvariable = age_value)
mobile_entry = Entry(root, textvariable = mobile_value)
email_entry = Entry(root, textvariable = email_value)

# pack entry in grid
name_entry.grid(row = 0, column = 1)
surename_entry.grid(row = 1, column = 1)
age_entry.grid(row = 2, column = 1)
mobile_entry.grid(row = 3, column = 1)
email_entry.grid(row = 4, column = 1)

# button
submit_btn = Button(root, text = "Submit", command = submit).grid()

root.mainloop()