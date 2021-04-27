from tkinter import *
import tkinter.messagebox as msgb

root = Tk()
root.geometry("400x100")
root.title("Sliders")

def submit():
    if slider.get()> 18:
        msgb.showinfo(f"Your Age Is {slider.get()}", "You can Drive a Vehicle")
    else:
        msgb.showinfo(f"Your Age Is {slider.get()}", "You Can't Drive a Vehicle")

Label(root, text = "What Is Your Age?").pack()
slider = Scale(root, from_ = 1, to= 100, orient = HORIZONTAL)
slider.set(18)
slider.pack(fill = "x")
Button(root, text = "Submit", command = submit).pack()

root.mainloop()