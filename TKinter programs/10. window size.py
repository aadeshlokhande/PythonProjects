from tkinter import *
root = Tk()
root.title("window size")
root.geometry("")

# function
def resize():
    root.geometry(f"{heightvalue.get()}x{widthvalue.get()}")
    note = f"{heightvalue.get()}x{widthvalue.get()}"
    Label(f"{heightvalue.get()}x{widthvalue.get()}").grid(row=2, column = 1)

# lbl
heightlbl = Label(root, text = "Height : ").grid(row=0, column = 0)
widthlbl = Label(root, text = "Width : ").grid(row= 1, column = 0)

# variable
heightvalue = StringVar()
widthvalue = StringVar()

#Entry
Entry(root, textvariable = heightvalue).grid(row = 0,column = 1)
Entry(root, textvariable = widthvalue).grid(row = 1,column = 1)

# Button
Button(root, text = "Resize", command = resize).grid()

Label("").grid(row=2, column = 1)
root.mainloop()