from tkinter import *

def aadesh(event):
    print(f"you clicked at {event.x}, {event.y}")

def lokhande(event):
    quit()

def key_press(event):
    key = event.char
    print(key, 'is pressed')

def enter(event):
    print("Enter")

def exit_(event):
    print("exit")

root = Tk()
root.title("Event Handling")
root.geometry("333x333")

# Button
widget = Button(root, text="Click Me")
widget.pack()

# binding
widget.bind('<Button-1>', aadesh)
widget.bind('<Double-1>', lokhande)

# Label
Label(root, text="Press key ").pack()

# here we are binding keyboard
root.bind('<Key>', lambda a: key_press(a))

# mouse arrow enter/ exit
root.bind('<Enter>', enter)
root.bind('<Leave>', exit_)

root.mainloop()
