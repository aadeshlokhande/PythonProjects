from tkinter import *

root = Tk()
root.geometry("444x444")
root.title("Menus & Submenus")

def adds():
    print("bhula")

# # menus without dropdown
# mymenu = Menu(root)                                         # creat menu
# mymenu.add_command(label= "files", command = adds)          # 1st menu
# mymenu.add_command(label= "Exit", command = quit)           # 2nd menu
# root.config(menu=mymenu)                                    # pack menu

def newpro():
    print("New Projects")
def save():
    print("Save")
def saveas():
    print("Save as")
def printa():
    print("Print")


# dropdown menus
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff = 0)
m1.add_command(label = "New Project", command = newpro)
m1.add_separator()
m1.add_command(label = "Save", command = save)
m1.add_command(label = "Save as", command = saveas)
m1.add_separator()
m1.add_checkbutton(label = "yes")
m1.add_command(label = "Exit", command = quit)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "Files", menu = m1)


m2 = Menu(mainmenu, tearoff = 0)
m2.add_command(label = "copy", command = newpro)
m2.add_separator()
m2.add_command(label = "Paste", command = save)
m2.add_command(label = "Cut", command = saveas)
m2.add_separator()
m2.add_checkbutton(label = "No")
m2.add_command(label = "Move", command = quit)
root.config(menu = mainmenu)
mainmenu.add_cascade(label = "Edit", menu = m2)






root.mainloop()