from tkinter import *
import random
import tkinter.messagebox as mb
import time

root = Tk()
# root.geometry("1140x700")
# root.minsize(1150, 700)
# root.maxsize(1150, 700)
root.title("Restaurant Management Systems by Aadesh Lokhande")
root.configure(bg="Cadet blue")

# buttons Functions

def iExit():
    iExit = mb.askyesno("Exit Restaurant System",
                        "Confirm If You Want To Exit")
    if iExit == 1:
        root.destroy()

def Reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofNonveg.set("")
    CostofVeg.set("")
    ServiceCharge.set("")
    Cus_Name.set("")
    txtReceipt.delete("1.0", END)

    E_Chi_Lollipop.set("0")
    E_Chi_Hotdog.set("0")
    E_Chi_Burger.set("0")
    E_Chi_Roll.set("0")
    E_Chi_65.set("0")
    E_Chi_Crispy.set("0")
    E_Chi_Chilli.set("0")
    E_Chi_Samosa.set("0")

    E_Veg_Puff.set("0")
    E_Veg_Hotdog.set("0")
    E_Veg_Burger.set("0")
    E_Veg_Roll.set("0")
    E_Veg_Manchurian.set("0")
    E_Veg_Crispy.set("0")
    E_Veg_noodles.set("0")
    E_Veg_samosa.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    Chi_Lollipoptxt.configure(state=DISABLED)
    Chi_Hotdogtxt.configure(state=DISABLED)
    Chi_Burgertxt.configure(state=DISABLED)
    Chi_Rolltxt.configure(state=DISABLED)
    Chi_65txt.configure(state=DISABLED)
    Chi_Crispytxt.configure(state=DISABLED)
    Chi_Chillitxt.configure(state=DISABLED)
    Chi_Samosatxt.configure(state=DISABLED)

    Veg_Pufftxt.configure(state=DISABLED)
    Veg_Hotdogtxt.configure(state=DISABLED)
    Veg_Burgertxt.configure(state=DISABLED)
    Veg_Rolltxt.configure(state=DISABLED)
    Veg_Manchuriantxt.configure(state=DISABLED)
    Veg_Crispytxt.configure(state=DISABLED)
    Veg_noodlestxt.configure(state=DISABLED)
    Veg_samosatxt.configure(state=DISABLED)

def CostosItem():
    item1 = float(E_Chi_Lollipop.get())
    item2 = float(E_Chi_Hotdog.get())
    item3 = float(E_Chi_Burger.get())
    item4 = float(E_Chi_Roll.get())
    item5 = float(E_Chi_65.get())
    item6 = float(E_Chi_Crispy.get())
    item7 = float(E_Chi_Chilli.get())
    item8 = float(E_Chi_Samosa.get())

    item9 = float(E_Veg_Puff.get())
    item10 = float(E_Veg_Hotdog.get())
    item11 = float(E_Veg_Burger.get())
    item12 = float(E_Veg_Roll.get())
    item13 = float(E_Veg_Manchurian.get())
    item14 = float(E_Veg_Crispy.get())
    item15 = float(E_Veg_noodles.get())
    item16 = float(E_Veg_samosa.get())

    PriceofNonveg = (item1 * 120) + (item2 * 40) + (item3 * 40) + (item4 * 45) + \
        (item5 * 120) + (item6 * 120) + (item7 * 120) + (item8 * 35)
    PriceofVeg = (item9 * 15) + (item10 * 45) + (item11 * 45) + (item12 * 35) + \
        (item13 * 60) + (item14 * 60) + (item15 * 80) + (item16 * 20)

    NonvegPrice = f"{PriceofNonveg} Rs"
    VegPrice = f"{PriceofVeg} Rs"

    CostofNonveg.set(NonvegPrice)
    CostofVeg.set(VegPrice)

    ServiceCharge.set(f"{12} Rs")

    SubTotalItems = f"{PriceofNonveg+PriceofVeg+12} Rs"
    SubTotal.set(SubTotalItems)

    Tax = f"{(PriceofNonveg + PriceofVeg + 12)*0.15} Rs"
    PaidTax.set(Tax)

    TT = (PriceofNonveg + PriceofVeg + 12)*0.15
    TC = f"{PriceofNonveg + PriceofVeg + 2 + TT} Rs"
    TotalCost.set(TC)

def Receipt():
    item1 = float(E_Chi_Lollipop.get())
    item2 = float(E_Chi_Hotdog.get())
    item3 = float(E_Chi_Burger.get())
    item4 = float(E_Chi_Roll.get())
    item5 = float(E_Chi_65.get())
    item6 = float(E_Chi_Crispy.get())
    item7 = float(E_Chi_Chilli.get())
    item8 = float(E_Chi_Samosa.get())

    item9 = float(E_Veg_Puff.get())
    item10 = float(E_Veg_Hotdog.get())
    item11 = float(E_Veg_Burger.get())
    item12 = float(E_Veg_Roll.get())
    item13 = float(E_Veg_Manchurian.get())
    item14 = float(E_Veg_Crispy.get())
    item15 = float(E_Veg_noodles.get())
    item16 = float(E_Veg_samosa.get())

    Chi_Lollipop_Price = str(item1 * 120)
    Chi_Hotdog_Price = str(item2 * 40)
    Chi_Burger_Price = str(item3 * 40)
    Chi_Roll_Price = str(item4 * 45)
    Chi_65_Price = str(item5 * 120)
    Chi_Crispy_Price = str(item6 * 120)
    Chi_Chilli_Price = str(item7 * 120)
    Chi_Samosa_Price = str(item8 * 35)

    Veg_Puff_Price = str(item9 * 15)
    Veg_Hotdog_Price = str(item10 * 45)
    Veg_Burger_Price = str(item11 * 45)
    Veg_Roll_Price = str(item12 * 35)
    Veg_Manchurian_Price = str(item13 * 60)
    Veg_Crispy_Price = str(item14 * 60)
    Veg_noodles_Price = str(item15 * 80)
    Veg_samosa_Price = str(item16 * 20)

    txtReceipt.delete("1.0", END)
    x = random.randint(1000000, 100000000)
    randomRef = str(x)
    Receipt_Ref.set("BILL - " + randomRef)
    CusName = Cus_Name.get().upper()
    txtReceipt.insert(END, "Receipt Ref : " +
                      Receipt_Ref.get()+"\t\t" + DateofOrder.get() + "\n")
    txtReceipt.insert(END, "Customer Name\t:\t" + CusName + "\n\n")
    txtReceipt.insert(END, "Items\t\t\t" + "Cost of Items\n")

    txtReceipt.insert(END, "Chicken Lollipop\t\t\t\t" +Chi_Lollipop_Price + "\n")
    txtReceipt.insert(END, "Chicken Hotdog\t\t\t\t" + Chi_Hotdog_Price+"\n")
    txtReceipt.insert(END, "Chicken Burger\t\t\t\t" + Chi_Burger_Price + "\n")
    txtReceipt.insert(END, "Chicken Roll\t\t\t\t" + Chi_Roll_Price+"\n")
    txtReceipt.insert(END, "Chicken 65\t\t\t\t" + Chi_65_Price+"\n")
    txtReceipt.insert(END, "Chicken Crispy\t\t\t\t" + Chi_Crispy_Price + "\n")
    txtReceipt.insert(END, "Chicken Chilli\t\t\t\t" + Chi_Chilli_Price + "\n")
    txtReceipt.insert(END, "Chicken Samosa\t\t\t\t" + Chi_Samosa_Price + "\n")

    txtReceipt.insert(END, "Veg Puff\t\t\t\t" + Veg_Puff_Price + "\n")
    txtReceipt.insert(END, "Veg Hotdog\t\t\t\t" + Veg_Hotdog_Price + "\n")
    txtReceipt.insert(END, "Veg Burger\t\t\t\t" + Veg_Burger_Price + "\n")
    txtReceipt.insert(END, "Veg Roll\t\t\t\t" + Veg_Roll_Price + "\n")
    txtReceipt.insert(END, "Veg Manchurian\t\t\t\t" + Veg_Manchurian_Price + "\n")
    txtReceipt.insert(END, "Veg Crispy\t\t\t\t" + Veg_Crispy_Price + "\n")
    txtReceipt.insert(END, "Veg Noodles\t\t\t\t" + Veg_noodles_Price + "\n")
    txtReceipt.insert(END, "Veg Samosa\t\t\t\t" + Veg_samosa_Price + "\n")

    txtReceipt.insert(END, "Paid Tax\t\t\t\t" + PaidTax.get() + "\n")
    txtReceipt.insert(END, "Service Charge\t\t\t\t" +
                      ServiceCharge.get() + "\n")
    txtReceipt.insert(END, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    txtReceipt.insert(END, "Total Cost\t\t\t\t" + TotalCost.get() + "\n")

    file = open("Bill.txt", "w")
    file.write(
        # "BILL - "+ randomRef+
        "Receipt Ref : " + Receipt_Ref.get()+"\t\t" + DateofOrder.get() + "\n" +
        "Customer Name\t:\t"+CusName+"\n" +
        "Items\t\t\t\t" + "Cost of Items\n" +

        "Chicken Lollipop\t\t\t" + Chi_Lollipop_Price + "\n" +
        "Chicken Hotdog\t\t\t\t" + Chi_Hotdog_Price + "\n" +
        "Chicken Burger\t\t\t\t" + Chi_Burger_Price + "\n" +
        "Chicken Roll\t\t\t\t" + Chi_Roll_Price + "\n" +
        "Chicken 65\t\t\t\t\t" + Chi_65_Price + "\n" +
        "Chicken Crispy\t\t\t\t" + Chi_Crispy_Price + "\n" +
        "Chicken Chilli\t\t\t\t" + Chi_Chilli_Price + "\n" +
        "Chicken Samosa\t\t\t\t" + Chi_Samosa_Price + "\n" +

        "Veg Puff\t\t\t\t\t" + Veg_Puff_Price + "\n" +
        "Veg Hotdog\t\t\t\t\t" + Veg_Hotdog_Price + "\n" +
        "Veg Burger\t\t\t\t\t" + Veg_Burger_Price + "\n" +
        "Veg Roll\t\t\t\t\t" + Veg_Roll_Price + "\n" +
        "Veg Manchurian\t\t\t\t" + Veg_Manchurian_Price + "\n" +
        "Veg Crispy\t\t\t\t\t" + Veg_Crispy_Price + "\n" +
        "Veg Noodles\t\t\t\t\t" + Veg_noodles_Price + "\n" +
        "Veg Samosa\t\t\t\t\t" + Veg_samosa_Price + "\n" +

        "Paid Tax\t\t\t\t" + PaidTax.get() + "\n" +
        "Service Charge\t\t\t\t" + ServiceCharge.get() + "\n" +
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        "Total Cost\t\t\t\t" + TotalCost.get() + "\n"
    )
    file.close()

# Check box  checked or not

def ckChi_Lollipop():
    if(var1.get() == 1):
        Chi_Lollipoptxt.configure(state=NORMAL)
        Chi_Lollipoptxt.focus()
        Chi_Lollipoptxt.delete("0", END)
        E_Chi_Lollipop.set("")
    elif(var1.get() == 0):
        Chi_Lollipoptxt.configure(state=DISABLED)
        E_Chi_Lollipop.set("0")

def ckChi_Hotdog():
    if(var2.get() == 1):
        Chi_Hotdogtxt.configure(state=NORMAL)
        Chi_Hotdogtxt.focus()
        Chi_Hotdogtxt.delete("0", END)
        E_Chi_Hotdog.set("")
    elif(var2.get() == 0):
        Chi_Hotdogtxt.configure(state=DISABLED)
        E_Chi_Hotdog.set("0")

def ckChi_Burger():
    if(var3.get() == 1):
        Chi_Burgertxt.configure(state=NORMAL)
        Chi_Burgertxt.focus()
        Chi_Burgertxt.delete("0", END)
        E_Chi_Burger.set("")
    elif(var3.get() == 0):
        Chi_Burgertxt.configure(state=DISABLED)
        E_Chi_Burger.set("0")

def ckChi_Roll():
    if(var4.get() == 1):
        Chi_Rolltxt.configure(state=NORMAL)
        Chi_Rolltxt.focus()
        Chi_Rolltxt.delete("0", END)
        E_Chi_Roll.set("")
    elif(var4.get() == 0):
        Chi_Rolltxt.configure(state=DISABLED)
        E_Chi_Roll.set("0")

def ckChi_65():
    if(var5.get() == 1):
        Chi_65txt.configure(state=NORMAL)
        Chi_65txt.focus()
        Chi_65txt.delete("0", END)
        E_Chi_65.set("")
    elif(var5.get() == 0):
        Chi_65txt.configure(state=DISABLED)
        E_Chi_65.set("0")

def ckChi_Crispy():
    if(var6.get() == 1):
        Chi_Crispytxt.configure(state=NORMAL)
        Chi_Crispytxt.focus()
        Chi_Crispytxt.delete("0", END)
        E_Chi_Crispy.set("")
    elif(var6.get() == 0):
        Chi_Crispytxt.configure(state=DISABLED)
        E_Chi_Crispy.set("0")

def ckChi_Chilli():
    if(var7.get() == 1):
        Chi_Chillitxt.configure(state=NORMAL)
        Chi_Chillitxt.focus()
        Chi_Chillitxt.delete("0", END)
        E_Chi_Chilli.set("")
    elif(var7.get() == 0):
        Chi_Chillitxt.configure(state=DISABLED)
        E_Chi_Chilli.set("0")

def ckChi_Samosa():
    if(var8.get() == 1):
        Chi_Samosatxt.configure(state=NORMAL)
        Chi_Samosatxt.focus()
        Chi_Samosatxt.delete("0", END)
        E_Chi_Samosa.set("")
    elif(var8.get() == 0):
        Chi_Samosatxt.configure(state=DISABLED)
        E_Chi_Samosa.set("0")

def ckVeg_Puff():
    if(var9.get() == 1):
        Veg_Pufftxt.configure(state=NORMAL)
        Veg_Pufftxt.focus()
        Veg_Pufftxt.delete("0", END)
        E_Veg_Puff.set("")
    elif(var9.get() == 0):
        Veg_Pufftxt.configure(state=DISABLED)
        E_Veg_Puff.set("0")

def ckVeg_Hotdog():
    if(var10.get() == 1):
        Veg_Hotdogtxt.configure(state=NORMAL)
        Veg_Hotdogtxt.focus()
        Veg_Hotdogtxt.delete("0", END)
        E_Veg_Hotdog.set("")
    elif(var10.get() == 0):
        Veg_Hotdogtxt.configure(state=DISABLED)
        E_Veg_Hotdog.set("0")

def ckVeg_Burger():
    if(var11.get() == 1):
        Veg_Burgertxt.configure(state=NORMAL)
        Veg_Burgertxt.focus()
        Veg_Burgertxt.delete("0", END)
        E_Veg_Burger.set("")
    elif(var11.get() == 0):
        Veg_Burgertxt.configure(state=DISABLED)
        E_Veg_Burger.set("0")

def ckVeg_Roll():
    if(var12.get() == 1):
        Veg_Rolltxt.configure(state=NORMAL)
        Veg_Rolltxt.focus()
        Veg_Rolltxt.delete("0", END)
        E_Veg_Roll.set("")
    elif(var12.get() == 0):
        Veg_Rolltxt.configure(state=DISABLED)
        E_Veg_Roll.set("0")

def ckVeg_Manchurian():
    if(var13.get() == 1):
        Veg_Manchuriantxt.configure(state=NORMAL)
        Veg_Manchuriantxt.focus()
        Veg_Manchuriantxt.delete("0", END)
        E_Veg_Manchurian.set("")
    elif(var13.get() == 0):
        Veg_Manchuriantxt.configure(state=DISABLED)
        E_Veg_Manchurian.set("0")

def ckVeg_Crispy():
    if(var14.get() == 1):
        Veg_Crispytxt.configure(state=NORMAL)
        Veg_Crispytxt.focus()
        Veg_Crispytxt.delete("0", END)
        E_Veg_Crispy.set("")
    elif(var14.get() == 0):
        Veg_Crispytxt.configure(state=DISABLED)
        E_Veg_Crispy.set("0")

def ckVeg_noodles():
    if(var15.get() == 1):
        Veg_noodlestxt.configure(state=NORMAL)
        Veg_noodlestxt.focus()
        Veg_noodlestxt.delete("0", END)
        E_Veg_noodles.set("")
    elif(var15.get() == 0):
        Veg_noodlestxt.configure(state=DISABLED)
        E_Veg_noodles.set("0")

def ckVeg_samosa():
    if(var16.get() == 1):
        Veg_samosatxt.configure(state=NORMAL)
        Veg_samosatxt.focus()
        Veg_samosatxt.delete("0", END)
        E_Veg_samosa.set("")
    elif(var16.get() == 0):
        Veg_samosatxt.configure(state=DISABLED)
        E_Veg_samosa.set("0")


# Top frame START
Tops = Frame(root, bg="Cadet blue", bd=20, pady=2, relief=RIDGE)
lblTitle = Label(Tops, font="arial 50 bold", text="Restaurant Management Systems",
                 bd=10, bg="Cadet blue", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)
lblname = Label(Tops, font="arial 15 bold",
                text="By Aadesh Lokhande", bg="Cadet blue", fg="Cornsilk")
lblname.grid(row=1, column=0)
Tops.pack(side=TOP, fill=BOTH)
# Top frame END

# Receipt frame START
ReceiptCal_f = Frame(root, bg="Powder blue", bd=10, relief=RIDGE)

Buttons_F = Frame(ReceiptCal_f, bg="Powder blue", bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM, fill=BOTH)

Cal_F = Frame(ReceiptCal_f, bg="Powder blue", bd=3, relief=RIDGE)
Cal_F.pack(side=TOP, fill=BOTH)

Receipt_F = Frame(ReceiptCal_f, bg="Powder blue", bd=3, relief=RIDGE)
Receipt_F.pack(side=BOTTOM, fill=BOTH)

ReceiptCal_f.pack(side=RIGHT, fill=BOTH)
# Receipt frame END

# Menu frame START
MenuFrame = Frame(root, bg="Cadet blue", bd=10, relief=RIDGE)

MenuFrame.pack(side=LEFT, fill= BOTH)

Cost_F = Frame(MenuFrame, bg="Powder Blue", bd=4)
Cost_F.pack(side=BOTTOM, fill=BOTH)

Drinks_F = Frame(MenuFrame, bg="Cadet Blue", bd=10)
Drinks_F.pack(side=TOP, fill=BOTH)

# declare Variable
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofNonveg = StringVar()
CostofVeg = StringVar()
ServiceCharge = StringVar()

Cus_Name = StringVar()

text_input = StringVar()
operator = ""

E_Chi_Lollipop = StringVar()
E_Chi_Hotdog = StringVar()
E_Chi_Burger = StringVar()
E_Chi_Roll = StringVar()
E_Chi_65 = StringVar()
E_Chi_Crispy = StringVar()
E_Chi_Chilli = StringVar()
E_Chi_Samosa = StringVar()

E_Veg_Puff = StringVar()
E_Veg_Hotdog = StringVar()
E_Veg_Burger = StringVar()
E_Veg_Roll = StringVar()
E_Veg_Manchurian = StringVar()
E_Veg_Crispy = StringVar()
E_Veg_noodles = StringVar()
E_Veg_samosa = StringVar()

E_Chi_Lollipop.set("0")
E_Chi_Hotdog.set("0")
E_Chi_Burger.set("0")
E_Chi_Roll.set("0")
E_Chi_65.set("0")
E_Chi_Crispy.set("0")
E_Chi_Chilli.set("0")
E_Chi_Samosa.set("0")

E_Veg_Puff.set("0")
E_Veg_Hotdog.set("0")
E_Veg_Burger.set("0")
E_Veg_Roll.set("0")
E_Veg_Manchurian.set("0")
E_Veg_Crispy.set("0")
E_Veg_noodles.set("0")
E_Veg_samosa.set("0")

DateofOrder.set(time.strftime(" %d/%m/20%y"))

# nonveg Frame START
Nonveg_F = Frame(MenuFrame, bg="Powder Blue", bd=10, relief=RIDGE)
# Nonveg Checkboxes
Chi_Lollipop = Checkbutton(Nonveg_F, text="Chicken Lollipop\t  ", command=ckChi_Lollipop,
                           variable=var1, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Lollipop.grid(row=0, sticky=W)
# Chi_Lollipop.bind("<>", ckChi_Lollipop)
Chi_Hotdog = Checkbutton(Nonveg_F, text="Chicken Hotdog\t  ", command=ckChi_Hotdog,
                         variable=var2, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Hotdog.grid(row=1, sticky=W)
Chi_Burger = Checkbutton(Nonveg_F, text="Chicken Burger\t  ", command=ckChi_Burger,
                         variable=var3, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Burger.grid(row=2, sticky=W)
Chi_Roll = Checkbutton(Nonveg_F, text="Chicken Roll\t  ", command=ckChi_Roll,
                       variable=var4, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Roll.grid(row=3, sticky=W)
Chi_65 = Checkbutton(Nonveg_F, text="Chicken 65\t  ", command=ckChi_65,
                     variable=var5, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_65.grid(row=4, sticky=W)
Chi_Crispy = Checkbutton(Nonveg_F, text="Chicken Crispy\t  ", command=ckChi_Crispy,
                         variable=var6, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Crispy.grid(row=5, sticky=W)
Chi_Chilli = Checkbutton(Nonveg_F, text="Chicken Chilli\t  ", command=ckChi_Chilli,
                         variable=var7, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Chilli.grid(row=6, sticky=W)
Chi_Samosa = Checkbutton(Nonveg_F, text="Chicken Samosa\t  ", command=ckChi_Samosa,
                         variable=var8, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Chi_Samosa.grid(row=7, sticky=W)

# Nonveg Entries
Chi_Lollipoptxt = Entry(Nonveg_F, font="arial 16 bold",
                        textvariable=E_Chi_Lollipop, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Lollipoptxt.grid(row=0, column=1)
Chi_Hotdogtxt = Entry(Nonveg_F, font="arial 16 bold",
                      textvariable=E_Chi_Hotdog, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Hotdogtxt.grid(row=1, column=1)
Chi_Burgertxt = Entry(Nonveg_F, font="arial 16 bold",
                      textvariable=E_Chi_Burger, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Burgertxt.grid(row=2, column=1)
Chi_Rolltxt = Entry(Nonveg_F, font="arial 16 bold",
                    textvariable=E_Chi_Roll, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Rolltxt.grid(row=3, column=1)
Chi_65txt = Entry(Nonveg_F, font="arial 16 bold", textvariable=E_Chi_65,
                  bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_65txt.grid(row=4, column=1)
Chi_Crispytxt = Entry(Nonveg_F, font="arial 16 bold",
                      textvariable=E_Chi_Crispy, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Crispytxt.grid(row=5, column=1)
Chi_Chillitxt = Entry(Nonveg_F, font="arial 16 bold",
                      textvariable=E_Chi_Chilli, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Chillitxt.grid(row=6, column=1)
Chi_Samosatxt = Entry(Nonveg_F, font="arial 16 bold",
                      textvariable=E_Chi_Samosa, bd=8, width=5, justify=LEFT, state=DISABLED)
Chi_Samosatxt.grid(row=7, column=1)


Nonveg_F.pack(side=LEFT, fill=BOTH)
# nonveg frame END


# veg frame START
Veg_F = Frame(MenuFrame, bg="Powder Blue", bd=10, relief=RIDGE)
# Veg Checkboxes
Veg_Puff = Checkbutton(Veg_F, text="Veg Puff\t\t", command=ckVeg_Puff,
                       variable=var9, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_Puff.grid(row=0, sticky=W)
Veg_Hotdog = Checkbutton(Veg_F, text="Veg Hotdog\t", command=ckVeg_Hotdog,
                         variable=var10, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_Hotdog.grid(row=1, sticky=W)
Veg_Burger = Checkbutton(Veg_F, text="Veg Burger\t", command=ckVeg_Burger,
                         variable=var11, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_Burger.grid(row=2, sticky=W)
Veg_Roll = Checkbutton(Veg_F, text="Paneer Roll\t", command=ckVeg_Roll,
                       variable=var12, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_Roll.grid(row=3, sticky=W)
Veg_Manchurian = Checkbutton(Veg_F, text="Veg Manchurian\t", command=ckVeg_Manchurian,
                             variable=var13, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_Manchurian.grid(row=4, sticky=W)
Veg_Crispy = Checkbutton(Veg_F, text="Veg Crispy\t", command=ckVeg_Crispy,
                         variable=var14, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_Crispy.grid(row=5, sticky=W)
Veg_noodles = Checkbutton(Veg_F, text="Veg Noodles\t", command=ckVeg_noodles,
                          variable=var15, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_noodles.grid(row=6, sticky=W)
Veg_samosa = Checkbutton(Veg_F, text="Samosa\t\t", command=ckVeg_samosa,
                         variable=var16, onvalue=1, offvalue=0, font="arial 16 bold", bg="powder blue")
Veg_samosa.grid(row=7, sticky=W)

# Veg Entries
Veg_Pufftxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_Puff,
                    bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_Pufftxt.grid(row=0, column=1)
Veg_Hotdogtxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_Hotdog,
                      bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_Hotdogtxt.grid(row=1, column=1)
Veg_Burgertxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_Burger,
                      bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_Burgertxt.grid(row=2, column=1)
Veg_Rolltxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_Roll,
                    bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_Rolltxt.grid(row=3, column=1)
Veg_Manchuriantxt = Entry(Veg_F, font="arial 16 bold", bd=8,
                          textvariable=E_Veg_Manchurian, width=5, justify=LEFT, state=DISABLED)
Veg_Manchuriantxt.grid(row=4, column=1)
Veg_Crispytxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_Crispy,
                      bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_Crispytxt.grid(row=5, column=1)
Veg_noodlestxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_noodles,
                       bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_noodlestxt.grid(row=6, column=1)
Veg_samosatxt = Entry(Veg_F, font="arial 16 bold", textvariable=E_Veg_samosa,
                      bd=8, width=5, justify=LEFT, state=DISABLED)
Veg_samosatxt.grid(row=7, column=1)
Veg_F.pack(side=RIGHT, fill=BOTH)
# Veg frame END



# Menu Frame END

# Total Cost
lblCostofNonveg = Label(Cost_F, font="arial 14 bold",
                        text="Cost of Nonveg", bg="powder blue", fg="black")
lblCostofNonveg.grid(row=0, column=0, sticky=W)
txtCostofNonveg = Entry(Cost_F, font="arial 12 bold", bg="white",
                        textvariable=CostofNonveg, bd=4, insertwidth=2, justify=RIGHT)
txtCostofNonveg.grid(row=0, column=1)

lblCostofVeg = Label(Cost_F, font="arial 14 bold",
                     text="Cost of Veg", bg="powder blue", fg="black")
lblCostofVeg.grid(row=1, column=0, sticky=W)
txtCostofVeg = Entry(Cost_F, font="arial 12 bold", bg="white",
                     textvariable=CostofVeg, bd=4, insertwidth=2, justify=RIGHT)
txtCostofVeg.grid(row=1, column=1)

lblServiceCharge = Label(Cost_F, font="arial 14 bold",
                         text="Service Charge", bg="powder blue", fg="black")
lblServiceCharge.grid(row=2, column=0, sticky=W)
txtServiceCharge = Entry(Cost_F, font="arial 12 bold", bg="white",
                         textvariable=ServiceCharge, bd=4, insertwidth=2, justify=RIGHT)
txtServiceCharge.grid(row=2, column=1)

lblPaidTax = Label(Cost_F, font="arial 14 bold", bd=7,
                   text="Paid Tax", bg="powder blue", fg="black")
lblPaidTax.grid(row=0, column=2, sticky=W)
txtPaidTax = Entry(Cost_F, font="arial 12 bold", bg="white",
                   textvariable=PaidTax, bd=7, insertwidth=2, justify=RIGHT)
txtPaidTax.grid(row=0, column=3)

lblSubTotal = Label(Cost_F, font="arial 14 bold",
                    text="Subtotal", bg="powder blue", fg="black")
lblSubTotal.grid(row=1, column=2, sticky=W)
txtSubTotal = Entry(Cost_F, font="arial 12 bold", textvariable=SubTotal,
                    bg="white", bd=7, insertwidth=2, justify=RIGHT)
txtSubTotal.grid(row=1, column=3)

lblTotalCost = Label(Cost_F, font="arial 14 bold",
                     text="Total Cost", bd=7, bg="powder blue", fg="black")
lblTotalCost.grid(row=2, column=2, sticky=W)
txtTotalCost = Entry(Cost_F, font="arial 12 bold", bd=7,
                     textvariable=TotalCost, bg="white", insertwidth=2, justify=RIGHT)
txtTotalCost.grid(row=2, column=3)

# Receipt
txtReceipt = Text(Receipt_F, width=47, height=9,
                  bg="white", bd=4, font="arial 12 bold")
txtReceipt.grid(row=0, column=0)

nameF = Frame(Receipt_F, width=47, height=2)
namelbl = Label(nameF, font="arial 14 bold", text="Customer Name :", bd=5, bg="powder blue", fg="black")
namelbl.grid(row=0, column=0)
nametxt = Entry(nameF, font="arial 14 bold", width=25, bd=5,
                textvariable=Cus_Name, bg="white", insertwidth=2, justify=RIGHT)
nametxt.grid(row=0, column=1)
nameF.grid(row=1, column=0)

# Main Buttons
btnTotal = Button(Buttons_F, padx=16, pady=1, bd=7, command=CostosItem,
                  fg="black", font="arial 16 bold", width=5, text="Total", bg="powder blue")
btnTotal.grid(row=0, column=0)

btnReceipt = Button(Buttons_F, padx=16, pady=1, bd=7, command=Receipt,
                    fg="black", font="arial 16 bold", width=5, text="Receipt", bg="powder blue")
btnReceipt.grid(row=0, column=1)

btnReset = Button(Buttons_F, padx=16, pady=1, bd=7, command=Reset, fg="black",
                  font="arial 16 bold", width=5, text="Reset", bg="powder blue")
btnReset.grid(row=0, column=2)
btnReset.bind("R", Reset)

btnExit = Button(Buttons_F, padx=16, pady=1, bd=7, command=iExit, fg="white",
                 font="arial 16 bold", width=4, text="Exit", bg="red2")
btnExit.grid(row=0, column=3)

# Calculator
# Calculator functions


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClear():
    global operator
    operator = ""
    text_input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""
    print(sumup)


# calc Display
txtDisplay = Entry(Cal_F, width=45, bg="white", bd=4,
                   textvariable=text_input, justify=RIGHT, font="arial 12 bold")
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

# calc Buttons
btn7 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(7), bd=7, fg="white",
              font="arial 16 bold", width=4, text="7", bg="orchid1")
btn7.grid(row=1, column=0)
btn8 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(8), bd=7, fg="white",
              font="arial 16 bold", width=4, text="8", bg="orchid1")
btn8.grid(row=1, column=1)
btn9 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(9), bd=7, fg="white",
              font="arial 16 bold", width=4, text="9", bg="orchid1")
btn9.grid(row=1, column=2)
btnAdd = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick("+"), bd=7, fg="white",
                font="arial 16 bold", width=4, text="+", bg="blue2")
btnAdd.grid(row=1, column=3)

btn4 = Button(Cal_F, padx=16, command=lambda: btnClick(4), pady=1, bd=7, fg="white",
              font="arial 16 bold", width=4, text="4", bg="orchid1")
btn4.grid(row=2, column=0)
btn5 = Button(Cal_F, padx=16, command=lambda: btnClick(5), pady=1, bd=7, fg="white",
              font="arial 16 bold", width=4, text="5", bg="orchid1")
btn5.grid(row=2, column=1)
btn6 = Button(Cal_F, padx=16, command=lambda: btnClick(6), pady=1, bd=7, fg="white",
              font="arial 16 bold", width=4, text="6", bg="orchid1")
btn6.grid(row=2, column=2)
btnSub = Button(Cal_F, padx=16, command=lambda: btnClick("-"), pady=1, bd=7, fg="white",
                font="arial 16 bold", width=4, text="-", bg="blue2")
btnSub.grid(row=2, column=3)

btn1 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(1), bd=7, fg="white",
              font="arial 16 bold", width=4, text="1", bg="orchid1")
btn1.grid(row=3, column=0)
btn2 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(2), bd=7, fg="white",
              font="arial 16 bold", width=4, text="2", bg="orchid1")
btn2.grid(row=3, column=1)
btn3 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(3), bd=7, fg="white",
              font="arial 16 bold", width=4, text="3", bg="orchid1")
btn3.grid(row=3, column=2)

btnMult = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick("*"), bd=7, fg="white",
                 font="arial 16 bold", width=4, text="*", bg="blue2")
btnMult.grid(row=3, column=3)

btnClear = Button(Cal_F, padx=16, pady=1, command=btnClear, bd=7, fg="white",
                  font="arial 16 bold", width=4, text="C", bg="red2")
btnClear.grid(row=4, column=0)
btn0 = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick(0), bd=7, fg="white",
              font="arial 16 bold", width=4, text="0", bg="orchid1")
btn0.grid(row=4, column=1)
btnEqual = Button(Cal_F, padx=16, pady=1, command=btnEquals, bd=7, fg="white",
                  font="arial 16 bold", width=4, text="=", bg="blue2")
btnEqual.grid(row=4, column=2)
btnDiv = Button(Cal_F, padx=16, pady=1, command=lambda: btnClick("/"), bd=7, fg="white",
                font="arial 16 bold", width=4, text="/", bg="blue2")
btnDiv.grid(row=4, column=3)

root.mainloop()