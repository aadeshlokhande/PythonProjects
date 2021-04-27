from tkinter import *
import wikipedia
root = Tk()
root.title("wikipedia")
root.geometry("500x500")

def search():
    result = wikipedia.page(topic.get())
    showresults.insert("end", result.summary)

frametop = Frame(root, width = 400, height = 300, relief = RIDGE, bd = 5)
frametop.pack(fill = BOTH, side = TOP)

topic = StringVar()

topictxt = Entry(frametop, width = 30, relief = RIDGE,textvariable = topic, bd = 3)
topictxt.pack(fill = BOTH)

search = Button(frametop, text="search",command=search, relief=RAISED, bd=2, font="arial 8 bold")
search.pack()

showresults = Text(root, width=20, height=12,font="lucida 16 bold", relief=SUNKEN, bd=10)
showresults.pack(fill=X, padx=3, pady=5)

root.mainloop()