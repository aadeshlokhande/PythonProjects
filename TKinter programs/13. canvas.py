from tkinter import *

root = Tk()
root.title("Canvas")
root.configure(bg = "cadet blue")

w = 500
h = 500

root.geometry(f"{w}x{h}")
canwas_wid = Canvas(root, width = w, height = h)
canwas_wid.pack()

canwas_wid.create_line(0,0,500,500, fill = "red")
canwas_wid.create_line(0,500,500,0, fill = "red")

canwas_wid.create_rectangle(100,100,400,400, fill = "powder blue")

canwas_wid.create_text(250,250 ,text = "Aadesh", font = "44")
root.mainloop()