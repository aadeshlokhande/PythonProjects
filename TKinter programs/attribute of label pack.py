from tkinter import *


root = Tk()
root.title("Aadesh")              #title
root.geometry("700x400")            #geometry og window


# two ways for font
# font = "comicsansms 12 bold"
# font = ("comicsansms" , 12, "bold")

title_label = Label(text = '''Simple Present Tense is a type of sentence that has a function to express an activity or fact that \noccurs in the present, and structurally or its arrangement, simple present tense uses only one verb.Present Tense is one of the \nforms of verb tenses. It simply describes the actions, truths(facts), future and situations. It is very easy to form and uses \nbase form of the verb.It is a verb tense.  A ‘verb’ is an action word.  The ‘tense’ is the time of the action.  The ‘present’ \nis now. It shows how the past is connected to the present/now.''',
                    bg = "red",
                    fg = "white",
                    padx = 44,
                    pady = 94,
                    font = "comicsansms 12 bold",
                    borderwidth = 20,
                    relief = SUNKEN
                    )
# title_label.pack()

# anchor pack
# title_label.pack(anchor = "nw")
# title_label.pack(anchor = "ne")

# side = top , bottom, left , right
# title_label.pack(side = RIGHT)

# fill
# title_label.pack(side = BOTTOM, fill = X)
title_label.pack(side = LEFT, fill = Y)

# padding
title_label.pack(side = LEFT, fill = Y, padx = 32, pady = 44)



root.mainloop()