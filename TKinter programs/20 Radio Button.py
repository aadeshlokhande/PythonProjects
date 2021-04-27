from tkinter import *
import tkinter.messagebox as mb

root = Tk()
root.geometry("444x444")
root.title("Radio Button")

def submit():
    mb.showinfo( f"{var.get()}", "Its A Very Big Company")

Label(root, text = "Which Company's Mobile You Are Using?", font = "lucida 14 bold").pack()
var = StringVar()
var.set("bhula")                    #for blank radiobuttons
Radiobutton(root, text = "Xiomi", padx = 12, variable = var, value = "Xiomi").pack(anchor = "w")
Radiobutton(root, text = "Samsung", padx = 12, variable = var, value = "Samsung").pack(anchor = "w")
Radiobutton(root, text = "Asus", padx = 12, variable = var, value = "Asus").pack(anchor = "w")
Radiobutton(root, text = "Micromax", padx = 12, variable = var, value = "Micromax").pack(anchor = "w")
Button(text = "Submit", command = submit).pack()

root.mainloop()