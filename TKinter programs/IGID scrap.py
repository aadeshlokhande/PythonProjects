from tkinter import *
from instagramy import InstagramUser

root = Tk()
root.title("Instagram User Details")
root.geometry("600x250")

def submit():
    try:
        user = InstagramUser(userid.get())
        showresults.configure(text = f'''\nUsername\t=\t{user.fullname}\nFollowers\t=\t{user.number_of_followers}\nFollowing\t=\t{user.number_of_followings}\nPost\t\t=\t{user.number_of_posts}\nEmail\t\t=\t{user.email}\nPrivate\t\t=\t{user.is_private}''')
    except:
        showresults.configure(text = "Invalid input")

frametop = Frame(root, relief = RIDGE, bd = 5)
frametop.pack(fill = BOTH, side = TOP)

userid = StringVar()

topictxt = Entry(frametop,relief = RIDGE,font="lucida 14 bold" ,textvariable = userid,justify= CENTER, bd = 3)
topictxt.pack(fill = BOTH)

searchbtn = Button(frametop, text="search",command=submit, bg = "cadet blue",relief=RAISED, bd=2, font="arial 14 bold")
searchbtn.pack()

showresults = Label(root,font="lucida 12 bold", justify = LEFT)
showresults.pack()

root.mainloop()