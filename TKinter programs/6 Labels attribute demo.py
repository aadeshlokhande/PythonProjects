from tkinter import *

root = Tk()
# root.geometry("400x400")
root.minsize(500,200)
root.title("Label's Attibute Demo")
lbl = Label(text = '''Python is a general-purpose coding language—which means that,\nunlike HTML, CSS, and JavaScript, it can be used for other types\nof programming and software development besides web development.\nThat includes back end development, software development,\ndata science and writing system scripts among other things.''', bg = "yellow", padx = 10, pady = 10, font = "comicsansms 14 bold", borderwidth = 10, relief = SUNKEN)
lbl.pack(side = LEFT, fill = X)

root.mainloop()