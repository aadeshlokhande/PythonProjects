from tkinter import *
from pytube import YouTube

root = Tk()

root.geometry("400xx400")
root.title("youtube vdo downloader")

def download():
    try:
        myVar.set("Downoading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Successfully")
    except Exception as e:
        myVar .set("Mistake")
        root.update()
        link.set("Enter currect link")

Label(root, text = "Welcome to DownTube", font = "Consolas 18 bold").pack()
myVar = StringVar()
myVar.set("Paste Video Link")

Entry(root, textvariable = myVar, width = 40).pack(pady = 10)

link = StringVar()

Entry(root, textvariable = link, width = 40).pack(pady = 10)

Button(root, text = "Download", command = download).pack()


root.mainloop()