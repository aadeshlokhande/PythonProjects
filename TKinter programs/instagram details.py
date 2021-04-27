from  tkinter import *
import requests

root = Tk()
root.title("Instagram User Details")
root.geometry("400x300")

def search():
    u_name = user.get()
    url = f"www.instagram.com/{u_name}/_a=1"
    data = requests.get(url).json()
    print(data)
    def pic():
        import webbrowser
        d = data["graphql"]["user"]["profile_pic_url"]
        webbrowser.open(d)
    if details.get(1.0, END) != "":
        details.delete(1.0,END)
        details.insert(1.0, f'''\t username : {data["graphql"]["user"]["usernane"]}\nFollowers : {data["graphql"]["user"]["edge_followed_by"]["count"]} following = {data["graphql"]["user"]["edge_follow"]["count"]} \n Full name =  {data["graphql"]["user"]["full_name"]} Total Post = {data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]} Category = {data["graphql"]["user"]["category_enum"]} \n Email = {data["graphql"]["user"]["business_email"]} \n bio link = {data["graphql"]["user"]["external_url"]}\n private A/c = {data["graphql"]["user"]["is_private"]} \n Verified Account = {data["graphql"]["user"]["is_verified"]} Bussiness A/c = {data["graphql"]["user"]["is_business_account"]} \n\n See Profile Picture''')
        Button(innerframe1, text = "click to see", relief = RAISED, bd= 2, font = "verdana 8 bold", bg = "#248aa2", fg = "white", command = pic).place(x = 180, y = 145)

frame = Frame(root, width = 400, height = 300, relief = RIDGE, bd = 5, bg = "#248aa2")
frame.pack()

innerframe = LabelFrame(frame, width = 380, height = 50, relief = RIDGE, bd = 3, bg = "#248aa2", highlightbackground = "white", highlightcolor = "white", highlightthickness = 2)
innerframe.pack()

user = Entry(frame, width = 30, relief = RIDGE, bd = 3)
user.pack()

search = Button(frame, text = "search", relief = RAISED, bd = 2, font = "arial 8 bold", bg = "#248aa2", fg = "white", command = search)
search.pack()

innerframe = LabelFrame(frame, width = 380, height = 50, relief = RIDGE, bd = 3, bg = "#248aa2", highlightbackground = "white", highlightcolor = "white", highlightthickness = 2)
innerframe.pack()

innerframe1 = LabelFrame(innerframe,text = "user details", width = 380,font = "verdana 10 bold", highlightbackground = "white", highlightcolor = "white", highlightthickness = 2)
innerframe.pack()

details= Text(innerframe1,  width = 47, height = 12, relief = RIDGE, bd = 5, highlightbackground = "white", highlightcolor = "white")
details.pack()
root.mainloop()

