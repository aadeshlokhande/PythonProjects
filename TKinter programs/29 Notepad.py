from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfile
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfile(initialfile = "Untitled.txt",defaultextension = ".txt", filetypes = [("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None

        else:
#             save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))
    pass
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Aadesh Lokhande")



if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    # root.wm_iconbitmap("1.ico")
    root.geometry("644x600")
    root.configure(bg = "Cadet blue")
    # add textarea
    TextArea = Text(root, font = "lucida 14 bold",fg = "white",bg = "black")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    # lets create a menu bar
    MenuBar = Menu(root)

    # File menu start
    FileMenu = Menu(MenuBar, tearoff = 0)

    # open new file
    FileMenu.add_command(label = "New", command = newFile)

    # to open already existing file
    FileMenu.add_command(label = "Open", command = openFile)

    # to save the current file
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label = "File", menu = FileMenu)
    # File menu Ends

    # Edit menu starts
    EditMenu = Menu(MenuBar, tearoff = 0)
    # to give a feature of cut, copy and paste
    EditMenu.add_command(label = "cut", command = cut)
    EditMenu.add_command(label = "copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label = "Edit", menu = EditMenu)
    # Edit menu Ends

    # help menu starts
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)
    MenuBar.add_cascade(label = "Help", menu = HelpMenu)
    # help menu ENDS

    root.config(menu = MenuBar)

    # Adding scrollBar
    ScrollBar = Scrollbar(TextArea)
    ScrollBar.pack(side = RIGHT, fill = Y)
    ScrollBar.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = ScrollBar.set)


    root.mainloop()
