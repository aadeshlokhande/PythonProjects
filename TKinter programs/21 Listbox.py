from tkinter import *

root = Tk()
root.geometry("444x444")
root.title("ListBox")

def add():
    global i
    a = "Aadesh Gautam Lokhande"
    tt = a[i]
    lbx.insert(ACTIVE, tt)
    i+=1

i= 0
lbx = Listbox(root, height = 20)
lbx.pack()
lbx.insert(END, "")

Button(root, text = "Add Item", command = add).pack()



root.mainloop()