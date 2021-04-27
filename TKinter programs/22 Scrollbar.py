from tkinter import *

root = Tk()
root.geometry("444x444")
root.title("ScrollBar")

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = "both")



listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(122):
    listbox.insert(END, f"Item {i}")

listbox.pack(fill = "both", padx = 22)
scrollbar.config(command = listbox.yview)



root.mainloop()