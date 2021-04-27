from instabot import Bot
from tkinter import *

# bot = Bot()
#
# bot.login(username = "love_hyper_cars",
#                 password = "poplolpop007")
# bot.upload_photo("/home/aadesh/Downloads/1.jpg",
#                  caption = "upload pic using python")

root = Tk()
# root.geometry("500x500")
root.title("Instagram Post Scheduler")
root.configure(bg = "powder blue")
frametop = Frame(root, bg = "cadet blue", bd =20, relief = RIDGE)
frametop.pack(fill = BOTH)

user_value = StringVar()
password_value = StringVar()
path_value = StringVar()
caption_value = StringVar()

titletxt = Label(frametop, text = "Instagram post scheduler", font = "arial 24 bold",
                 bg = "cadet blue", fg = "yellow")
titletxt.pack(pady = 20)

entry_f = Frame(root, bg = "powder blue", relief = RIDGE, bd =10)
entry_f.pack(fill = BOTH)

usertxt = Label(entry_f, text = "Username\t= ", font = "lucida 18 bold",bg= "powder blue", fg = "magenta2", width = 12)
usertxt.grid(row = 0, column = 0,pady = 5)
userentry = Entry(entry_f, textvariable = user_value , font = "lucida 18 bold",width = 15)
userentry.grid(row = 0, column = 1,pady = 5)

passwordtxt = Label(entry_f, text = "Password\t= ", font = "lucida 18 bold",bg= "powder blue", fg = "magenta2", width = 12)
passwordtxt.grid(row = 1, column = 0,pady = 5)
passwordentry = Entry(entry_f, textvariable = password_value , font = "lucida 18 bold",width = 15)
passwordentry.grid(row = 1, column = 1,pady = 5)

pathtxt = Label(entry_f, text = "File Path\t= ", font = "lucida 18 bold",bg= "powder blue",fg = "magenta2", width = 12)
pathtxt.grid(row = 2, column = 0,pady = 5)
pathentry = Entry(entry_f, textvariable = path_value , font = "lucida 18 bold",width = 15)
pathentry.grid(row = 2, column = 1,pady = 5)

captiontxt = Label(entry_f, text = "Caption\t= ", font = "lucida 18 bold",bg= "powder blue", fg = "magenta2", width = 12)
captiontxt.grid(row = 3, column = 0,pady = 5)
captionentry = Entry(entry_f, textvariable = caption_value , font = "lucida 18 bold",width = 15)
captionentry.grid(row = 3, column = 1,pady = 5)

btn_f = Frame(root, bd = 10, relief = SUNKEN, bg = "powder blue")
btn_f.pack(fill = BOTH)

def reset():
    user_value.set("")
    password_value.set("")
    path_value.set("")
    caption_value.set("")
    root.title("Instagram post scheduler")

resetbtn = Button(btn_f, text= "Reset",command = reset, font = "lucida 18 bold", width = 11,bg = "red", fg = "white", bd = 10, relief = SUNKEN)
resetbtn.grid(row = 0, column = 1)

def upload():
    print(user_value.get(),password_value.get(),path_value.get(),caption_value.get())
    root.title("Uploading...")
    bot = Bot()

    bot.login(username = f"{user_value.get()}",
                    password = f"{password_value.get()}")
    bot.upload_photo(f"{path_value.get()}",
                     caption = f"{caption_value.get()}")
    root.title("Uploaded")

uploadbtn = Button(btn_f, text= "Upload",command = upload, font = "lucida 18 bold", width = 12,bg = "red", fg = "white", bd = 10, relief = SUNKEN)
uploadbtn.grid(row = 0, column = 0)

root.mainloop()