from tkinter import *
from tkinter import messagebox
import random
import time

theme = "cadet blue"
###### Functoins ########

######## Functions of Bottom Buttons ##########


def Receipt():
    global PriceOfFood, PriceOfCakes, PriceOfDrinks, receiptref, dateoforder
    textreceipt.delete(1.0, END)

    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 \
            or var8.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
            var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var1.get() != 0 or var17.get() != 0 or \
            var18.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
            var25.get() != 0 or var26.get() != 0 or var27.get() != 0:

        if costoffoodvar.get() != '' or costofdrinksvar.get() != '' or costofcakesvar.get() != '':

            x = random.randint(1000000, 100000000)
            dateoforder = time.strftime('%d/%m/%Y')

            receiptref = 'BILL ' + str(x)

            textreceipt.insert(END, 'Receipt Ref :\t\t' +
                               receiptref+'\t\t'+dateoforder+'\n')
            textreceipt.insert(
                END, '*********************************************************************\n')
            textreceipt.insert(END, 'Items:\t\t'+"  Cost Of Items(In Rs)\n")
            textreceipt.insert(
                END, '*********************************************************************\n')

            if e_roti.get() != '0':
                textreceipt.insert(
                    END, f'Roti:\t\t\t{ int(e_roti.get()) * 10 }\n')

            if e_daal.get() != '0':
                textreceipt.insert(
                    END, f'Daal:\t\t\t{  int(e_daal.get()) * 80}\n')

            if e_kolhapuri.get() != '0':
                textreceipt.insert(
                    END, f'Kolhapuri:\t\t\t{ int(e_kolhapuri.get()) * 120 }\n')

            if e_sabji.get() != '0':
                textreceipt.insert(
                    END, f'sabji:\t\t\t{  int(e_sabji.get()) * 90}\n')

            if e_masoor.get() != '0':
                textreceipt.insert(
                    END, f'Masoor:\t\t\t{ int(e_masoor.get()) * 140 }\n')

            if e_kaju.get() != '0':
                textreceipt.insert(
                    END, f'Kaju:\t\t\t{  int(e_kaju.get()) * 160}\n')

            if e_paneer.get() != '0':
                textreceipt.insert(
                    END, f'Paneer:\t\t\t{ int(e_paneer.get()) * 150 }\n')

            if e_mixveg.get() != '0':
                textreceipt.insert(
                    END, f'Mix-Veg:\t\t\t{  int(e_mixveg.get()) * 140}\n')

            if e_chawal.get() != '0':
                textreceipt.insert(
                    END, f'Chawal:\t\t\t{ int(e_chawal.get()) * 60 }\n')

            if e_lassi.get() != '0':
                textreceipt.insert(
                    END, f'Lassi:\t\t\t{  int(e_lassi.get()) * 20}\n')

            if e_coffee.get() != '0':
                textreceipt.insert(
                    END, f'Coffee:\t\t\t{ int(e_coffee.get()) * 15 }\n')

            if e_faluda.get() != '0':
                textreceipt.insert(
                    END, f'Faluda:\t\t\t{  int(e_faluda.get()) * 25}\n')

            if e_juice.get() != '0':
                textreceipt.insert(
                    END, f'Juice:\t\t\t{ int(e_juice.get()) * 20 }\n')

            if e_jaljira.get() != '0':
                textreceipt.insert(
                    END, f'Jaljira:\t\t\t{  int(e_jaljira.get()) * 12}\n')

            if e_tea.get() != '0':
                textreceipt.insert(
                    END, f'Tea:\t\t\t{ int(e_tea.get()) * 10 }\n')

            if e_badammilk.get() != '0':
                textreceipt.insert(
                    END, f'Badam Milk:\t\t\t{  int(e_badammilk.get()) * 25}\n')

            if e_coldrinks.get() != '0':
                textreceipt.insert(
                    END, f'Cold Drinks:\t\t\t{  int(e_coldrinks.get()) * 20}\n')

            if e_sarbat.get() != '0':
                textreceipt.insert(
                    END, f'Sarbat:\t\t\t{ int(e_sarbat.get()) * 15 }\n')

            if e_butterscotch.get() != '0':
                textreceipt.insert(
                    END, f'ButterScotch Cake:\t\t\t{  int(e_butterscotch.get()) * 450}\n')

            if e_apple.get() != '0':
                textreceipt.insert(
                    END, f'Apple Cake:\t\t\t{ int(e_apple.get()) * 500 }\n')

            if e_vanilla.get() != '0':
                textreceipt.insert(
                    END, f'Vanila Cake:\t\t\t{  int(e_vanilla.get()) * 600}\n')

            if e_blackforest.get() != '0':
                textreceipt.insert(
                    END, f'Black Forest Cake:\t\t\t{  int(e_blackforest.get()) * 650}\n')

            if e_banana.get() != '0':
                textreceipt.insert(
                    END, f'Banana Cake:\t\t\t{ int(e_banana.get()) * 500}\n')

            if e_brownie.get() != '0':
                textreceipt.insert(
                    END, f'Brownie Cake:\t\t\t{  int(e_brownie.get()) * 650}\n')

            if e_pineapple.get() != '0':
                textreceipt.insert(
                    END, f'PineApple Cake:\t\t\t{ int(e_pineapple.get()) * 600 }\n')

            if e_chocolate.get() != '0':
                textreceipt.insert(
                    END, f'Chocolate Cake:\t\t\t{  int(e_chocolate.get()) * 700}\n')

            if e_oreo.get() != '0':
                textreceipt.insert(
                    END, f'Oreao Cake:\t\t\t{  int(e_oreo.get()) * 845}\n')

            textreceipt.insert(
                END, '*********************************************************************\n')

            if PriceOfFood != 0:
                textreceipt.insert(
                    END, f"Cost Of Food:\t\t\t{PriceOfFood} Rs\n\n")
            if PriceOfDrinks != 0:
                textreceipt.insert(
                    END, f"Cost Of Drinks:\t\t\t{PriceOfDrinks} Rs\n\n")
            if PriceOfCakes != 0:
                textreceipt.insert(
                    END, f"Cost Of Cakes:\t\t\t{PriceOfCakes} Rs\n\n")

            textreceipt.insert(
                END, '*********************************************************************\n')

            textreceipt.insert(
                END, f"Sub Total:\t\t\t{PriceOfCakes+PriceOfDrinks+PriceOfFood} Rs\n")
            textreceipt.insert(END, f"Service Tax:\t\t\t50 Rs\n")
            textreceipt.insert(END, f"Total Bill:\t\t\t{total} Rs\n")

            textreceipt.insert(
                END, '*********************************************************************\n')

            textreceipt.insert(END, "Thanks For Visit ----->")

        else:
            messagebox.showerror('Error', "Please Click On Total")

    else:
        messagebox.showerror('Error', "Please Select Something Sir")

def Save():

    if textreceipt.get(1.0, END) != '\n':
        dateoforder = time.strftime("%d_%m_%Y-%H_%M_%S")
        file = open(f"data/{dateoforder}.txt",'a')
        bill_data = textreceipt.get(1.0, END)
        file.write(bill_data.replace("*","_"))
        file.close()
        messagebox.showinfo('Information', "Your Bill is Saved Successfully")


def Reset():

    global root2

    e_daal.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_kolhapuri.set('0')
    e_masoor.set('0')
    e_chawal.set('0')
    e_mixveg.set('0')
    e_kaju.set('0')
    e_paneer.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_juice.set('0')
    e_sarbat.set('0')
    e_jaljira.set('0')
    e_tea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_butterscotch.set('0')
    e_banana.set('0')
    e_pineapple.set('0')
    e_apple.set('0')
    e_chocolate.set('0')
    e_oreo.set('0')
    e_blackforest.set('0')
    e_brownie.set('0')
    e_vanilla.set('0')

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
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textkolhapuri.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textkaju.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textmix.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textmasoor.config(state=DISABLED)

    textcoffee.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textlfaluda.config(state=DISABLED)
    textjuice.config(state=DISABLED)
    textjaljira.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)
    textsarbat.config(state=DISABLED)

    textbuttorscotch.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textvanila.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrowni.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textoreo.config(state=DISABLED)

    costofdrinksvar.set('')
    costofcakesvar.set('')
    costoffoodvar.set('')
    subtotalvar.set('')
    totalcostvar.set('')
    servicechargevar.set('')

    textreceipt.delete(1.0, END)
    root2.destroy()

def CostOfItem():

    global PriceOfDrinks, PriceOfFood, PriceOfCakes, total

    if (e_roti.get() == '' or e_daal.get() == "" or e_kolhapuri.get() == '' or e_sabji.get() == "" or e_masoor.get() == '' or e_kaju.get() == "" or e_paneer.get() == '' or e_chawal.get() == ''
        or e_mixveg.get() == '' or e_lassi.get() == '' or e_coffee.get() == "" or e_faluda.get() == '' or e_juice.get() == "" or e_jaljira.get() == '' or e_tea.get() == "" or e_badammilk.get() == ''
        or e_coldrinks.get() == "" or e_sarbat.get() == '' or e_apple.get() == '' or e_blackforest.get() == "" or e_butterscotch.get() == '' or e_vanilla.get() == "" or e_brownie.get() == ''
            or e_pineapple.get() == "" or e_banana.get() == '' or e_chocolate.get() == "" or e_oreo.get() == ''):

        messagebox.showerror("Error", "PLease Enter the Quantity")

    else:

        if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 \
                or var8.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or \
                var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var1.get() != 0 or var17.get() != 0 or \
                var18.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or \
                var25.get() != 0 or var26.get() != 0 or var27.get() != 0:

            item1 = int(e_roti.get())
            item2 = int(e_daal.get())
            item3 = int(e_kolhapuri.get())
            item4 = int(e_sabji.get())
            item5 = int(e_masoor.get())
            item6 = int(e_kaju.get())
            item7 = int(e_paneer.get())
            item8 = int(e_mixveg.get())
            item9 = int(e_chawal.get())
            item10 = int(e_lassi.get())
            item11 = int(e_coffee.get())
            item12 = int(e_faluda.get())
            item13 = int(e_juice.get())
            item14 = int(e_jaljira.get())
            item15 = int(e_tea.get())
            item16 = int(e_badammilk.get())
            item17 = int(e_coldrinks.get())
            item18 = int(e_sarbat.get())
            item19 = int(e_butterscotch.get())
            item20 = int(e_apple.get())
            item21 = int(e_vanilla.get())
            item22 = int(e_blackforest.get())
            item23 = int(e_banana.get())
            item24 = int(e_brownie.get())
            item25 = int(e_pineapple.get())
            item26 = int(e_chocolate.get())
            item27 = int(e_oreo.get())

            PriceOfFood = (item1*10)+(item2*80)+(item3*120)+(item4*90) + \
                (item5*140)+(item6*160)+(item7*150)+(item8*140)+(item9*60)
            PriceOfDrinks = (item10*20)+(item11*15)+(item12*25)+(item13*20) + \
                (item14*12)+(item15*10)+(item16*25)+(item17*20)+(item18*15)
            PriceOfCakes = (item19*450)+(item20*500)+(item21*600)+(item22*650) + \
                (item23*500)+(item24*650)+(item25*600)+(item26*700)+(item27*845)

            costoffoodvar.set(str(PriceOfFood)+" Rs")
            costofdrinksvar.set(str(PriceOfDrinks)+" Rs")
            costofcakesvar.set(str(PriceOfCakes)+" Rs")

            subtotalofitems = PriceOfCakes + PriceOfDrinks + PriceOfFood

            subtotalvar.set(str(subtotalofitems)+" Rs")

            servicechargevar.set('50 Rs')

            total = subtotalofitems + 50

            totalcostvar.set(str(total)+" Rs")

        else:
            messagebox.showerror("Error", "No Item Selected")

######### Functions of Food Items #######

def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.focus()
        textroti.delete(0, END)
    elif var1.get() == 0:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.focus()
        textdaal.delete(0, END)
    elif var2.get() == 0:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def kolhapuri():
    if var3.get() == 1:
        textkolhapuri.config(state=NORMAL)
        textkolhapuri.focus()
        textkolhapuri.delete(0, END)
    elif var3.get() == 0:
        textkolhapuri.config(state=DISABLED)
        e_kolhapuri.set('0')

def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')

def masoor():
    if var5.get() == 1:
        textmasoor.config(state=NORMAL)
        textmasoor.focus()
        textmasoor.delete(0, END)
    elif var5.get() == 0:
        textmasoor.config(state=DISABLED)
        e_masoor.set('0')


def kaju():
    if var6.get() == 1:
        textkaju.config(state=NORMAL)
        textkaju.focus()
        textkaju.delete(0, END)
    elif var6.get() == 0:
        textkaju.config(state=DISABLED)
        e_kaju.set('0')


def paneer():
    if var7.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var7.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def mix():
    if var8.get() == 1:
        textmix.config(state=NORMAL)
        textmix.focus()
        textmix.delete(0, END)
    elif var8.get() == 0:
        textmix.config(state=DISABLED)
        e_mixveg.set('0')

def chawal():
    if var9.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var9.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')

def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def faluda():
    if var12.get() == 1:
        textlfaluda.config(state=NORMAL)
        textlfaluda.focus()
        textlfaluda.delete(0, END)
    elif var12.get() == 0:
        textlfaluda.config(state=DISABLED)
        e_faluda.set('0')

def juice():
    if var13.get() == 1:
        textjuice.config(state=NORMAL)
        textjuice.focus()
        textjuice.delete(0, END)
    elif var13.get() == 0:
        textjuice.config(state=DISABLED)
        e_juice.set('0')

def jaljira():
    if var14.get() == 1:
        textjaljira.config(state=NORMAL)
        textjaljira.focus()
        textjaljira.delete(0, END)
    elif var14.get() == 0:
        textjaljira.config(state=DISABLED)
        e_jaljira.set('0')

def tea():
    if var15.get() == 1:
        texttea.config(state=NORMAL)
        texttea.focus()
        texttea.delete(0, END)
    elif var15.get() == 0:
        texttea.config(state=DISABLED)
        e_tea.set('0')

def badamnilk():
    if var16.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var16.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')

def colddrinks():
    if var17.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var17.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')

def sarbat():
    if var18.get() == 1:
        textsarbat.config(state=NORMAL)
        textsarbat.focus()
        textsarbat.delete(0, END)
    elif var18.get() == 0:
        textsarbat.config(state=DISABLED)
        e_sarbat.set('0')

def butterscotchCake():
    if var19.get() == 1:
        textbuttorscotch.config(state=NORMAL)
        textbuttorscotch.focus()
        textbuttorscotch.delete(0, END)
    elif var19.get() == 0:
        textbuttorscotch.config(state=DISABLED)
        e_butterscotch.set('0')

def appleCake():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')

def vanilaCake():
    if var21.get() == 1:
        textvanila.config(state=NORMAL)
        textvanila.focus()
        textvanila.delete(0, END)
    elif var21.get() == 0:
        textvanila.config(state=DISABLED)
        e_vanilla.set('0')

def blackforestCake():
    if var22.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var22.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def bananaCake():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')

def brownieCake():
    if var24.get() == 1:
        textbrowni.config(state=NORMAL)
        textbrowni.focus()
        textbrowni.delete(0, END)
    elif var24.get() == 0:
        textbrowni.config(state=DISABLED)
        e_brownie.set('0')

def pineappleCake():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def chocolateCake():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')

def oreoCake():
    if var27.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var27.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


########### Texture ################
root = Tk()
root.geometry('1350x710+0+0')
root.resizable(0, 0)
root.title("Restaurant Management System")
# root.config(background='firebrick4')
root.config(background=theme)


######## Top Frame ##########

topframe = Frame(root, bd=10, bg=theme, relief=RIDGE)
topframe.pack(side=TOP)

labeltitle = Label(topframe, text='Hotel Billing System', font=(
    'arial', 30, "bold"), fg='yellow', width=54, bg=theme, bd=9)
labeltitle.grid(row=0, column=0)


####### Billing Frame ##############

receiptcal_frame = Frame(root, bd=15, relief=RIDGE, bg=theme)
receiptcal_frame.pack(side=RIGHT)

button_frame = Frame(receiptcal_frame, bg=theme, bd=3, relief=RIDGE)
button_frame.pack(side=BOTTOM)

calculator_frame = Frame(receiptcal_frame, bg=theme, relief=RIDGE, bd=1)
calculator_frame.pack(side=TOP)

receipt_frame = Frame(receiptcal_frame, bg=theme, bd=4, relief=RIDGE)
receipt_frame.pack(side=BOTTOM)

######### Menu Frame ###############

menu_frame = Frame(root, bg=theme, bd=10, relief=RIDGE)
menu_frame.pack(side=LEFT)

cost_frame = Frame(menu_frame, bd=4, bg=theme)
cost_frame.pack(side=BOTTOM)

food_frame = LabelFrame(menu_frame, text="FOOD", font=(
    'arial', 19, 'bold'), fg=theme, bg='white', bd=10, relief=RIDGE)
food_frame.pack(side=LEFT)

drinks_frame = LabelFrame(menu_frame, text="DRINKS", font=(
    'arial', 19, 'bold'), fg=theme, bg='white', bd=10, relief=RIDGE)
drinks_frame.pack(side=LEFT)

cake_frame = LabelFrame(menu_frame, text="CAKE", font=(
    'arial', 19, 'bold'), fg=theme, bg='white', bd=10, relief=RIDGE)
cake_frame.pack(side=RIGHT)

######## Variables  ##########

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
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti = StringVar()
e_daal = StringVar()
e_kolhapuri = StringVar()
e_sabji = StringVar()
e_masoor = StringVar()
e_kaju = StringVar()
e_paneer = StringVar()
e_mixveg = StringVar()
e_chawal = StringVar()

e_lassi = StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_juice = StringVar()
e_jaljira = StringVar()
e_tea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()
e_sarbat = StringVar()


e_butterscotch = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()
e_oreo = StringVar()

e_daal.set('0')
e_roti.set('0')
e_sabji.set('0')
e_kolhapuri.set('0')
e_masoor.set('0')
e_chawal.set('0')
e_mixveg.set('0')
e_kaju.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_juice.set('0')
e_sarbat.set('0')
e_jaljira.set('0')
e_tea.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_butterscotch.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')


costoffoodvar = StringVar()
subtotalvar = StringVar()
totalcostvar = StringVar()
costofcakesvar = StringVar()
costofdrinksvar = StringVar()
servicechargevar = StringVar()


########## FOOD #############

roti = Checkbutton(food_frame, text='Roti', variable=var1, onvalue=1,
                   offvalue=0, font=('arial', 18, 'bold'), bg='white', command=roti)
roti.grid(row=0, column=0, sticky=W)

daal = Checkbutton(food_frame, text='Daal', onvalue=1, variable=var2,
                   offvalue=0, font=('arial', 18, 'bold'), bg='white', command=daal)
daal.grid(row=1, column=0, sticky=W)

kolhapuri = Checkbutton(food_frame, text='Kolhapuri', onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var3, command=kolhapuri)
kolhapuri.grid(row=2, column=0, sticky=W)

sabji = Checkbutton(food_frame, text='Sabji', onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var4, command=sabji)
sabji.grid(row=3, column=0, sticky=W)

masoor = Checkbutton(food_frame, text='Masoor', onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var5, command=masoor)
masoor.grid(row=4, column=0, sticky=W)

kaju = Checkbutton(food_frame, text='Kaju', onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var6, command=kaju)
kaju.grid(row=5, column=0, sticky=W)

paneer = Checkbutton(food_frame, text='Paneer', onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var7, command=paneer)
paneer.grid(row=6, column=0, sticky=W)

mix = Checkbutton(food_frame, text='Mix-Veg', onvalue=1, offvalue=0,
                  font=('arial', 18, 'bold'), bg='white', variable=var8, command=mix)
mix.grid(row=7, column=0, sticky=W)

chawal = Checkbutton(food_frame, text='Chawal', onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var9, command=chawal)
chawal.grid(row=8, column=0, sticky=W)


#############  FOOD ENTRY  #########


textroti = Entry(food_frame, font=('arial', 18, 'bold'), bd=8,
                 width=6, state=DISABLED, textvariable=e_roti)
textroti.grid(row=0, column=1)

textdaal = Entry(food_frame, font=('arial', 18, 'bold'), bd=8,
                 width=6, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=1, column=1)

textkolhapuri = Entry(food_frame, font=('arial', 18, 'bold'),
                      bd=8, width=6, state=DISABLED, textvariable=e_kolhapuri)
textkolhapuri.grid(row=2, column=1)

textsabji = Entry(food_frame, font=('arial', 18, 'bold'), bd=8,
                  width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textmasoor = Entry(food_frame, font=('arial', 18, 'bold'),
                   bd=8, width=6, state=DISABLED, textvariable=e_masoor)
textmasoor.grid(row=4, column=1)

textkaju = Entry(food_frame, font=('arial', 18, 'bold'), bd=8,
                 width=6, state=DISABLED, textvariable=e_kaju)
textkaju.grid(row=5, column=1)

textpaneer = Entry(food_frame, font=('arial', 18, 'bold'),
                   bd=8, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=6, column=1)

textmix = Entry(food_frame, font=('arial', 18, 'bold'), bd=8,
                width=6, state=DISABLED, textvariable=e_mixveg)
textmix.grid(row=7, column=1)

textchawal = Entry(food_frame, font=('arial', 18, 'bold'),
                   bd=8, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=8, column=1)


########## DRINKS ###########


lassi = Checkbutton(drinks_frame, text="Lassi", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var10, command=lassi)
lassi.grid(row=0, column=0, sticky=W)

coffee = Checkbutton(drinks_frame, text="Coffee", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var11, command=coffee)
coffee.grid(row=1, column=0, sticky=W)

faluda = Checkbutton(drinks_frame, text="Faluda", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var12, command=faluda)
faluda.grid(row=2, column=0, sticky=W)

juice = Checkbutton(drinks_frame, text="Juice", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var13, command=juice)
juice.grid(row=3, column=0, sticky=W)

jaljira = Checkbutton(drinks_frame, text="Jaljira", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var14, command=jaljira)
jaljira.grid(row=4, column=0, sticky=W)

tea = Checkbutton(drinks_frame, text="Tea", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var15, command=tea)
tea.grid(row=5, column=0, sticky=W)

badamnilk = Checkbutton(drinks_frame, text="Badam Milk", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var16, command=badamnilk)
badamnilk.grid(row=6, column=0, sticky=W)

colddrinks = Checkbutton(drinks_frame, text="Cold-Drinks", onvalue=1, offvalue=0,
                         font=('arial', 18, 'bold'), bg='white', variable=var17, command=colddrinks)
colddrinks.grid(row=7, column=0, sticky=W)

sarbat = Checkbutton(drinks_frame, text="Sarbat", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var18, command=sarbat)
sarbat.grid(row=8, column=0, sticky=W)


######### Entry Fields for Drinks #########


textlassi = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                  state=DISABLED, bd=8, justify=LEFT, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                   state=DISABLED, bd=8, justify=LEFT, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textlfaluda = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                    state=DISABLED, bd=8, justify=LEFT, textvariable=e_faluda)
textlfaluda.grid(row=2, column=1)

textjuice = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                  state=DISABLED, bd=8, justify=LEFT, textvariable=e_juice)
textjuice.grid(row=3, column=1)

textjaljira = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                    state=DISABLED, bd=8, justify=LEFT, textvariable=e_jaljira)
textjaljira.grid(row=4, column=1)

texttea = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                state=DISABLED, bd=8, justify=LEFT, textvariable=e_tea)
texttea.grid(row=5, column=1)

textbadammilk = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                      state=DISABLED, bd=8, justify=LEFT, textvariable=e_badammilk)
textbadammilk.grid(row=6, column=1)

textcolddrinks = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                       state=DISABLED, bd=8, justify=LEFT, textvariable=e_coldrinks)
textcolddrinks.grid(row=7, column=1)

textsarbat = Entry(drinks_frame, font=('arial', 18, 'bold'), width=6,
                   state=DISABLED, bd=8, justify=LEFT, textvariable=e_sarbat)
textsarbat.grid(row=8, column=1)


######### Cakes #############

butterscotchCake = Checkbutton(cake_frame, text="ButterScotch", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var19, command=butterscotchCake)
butterscotchCake.grid(row=0, column=0, sticky=W)

appleCake = Checkbutton(cake_frame, text="Apple", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var20, command=appleCake)
appleCake.grid(row=1, column=0, sticky=W)

vanilaCake = Checkbutton(cake_frame, text="Vanilla", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var21, command=vanilaCake)
vanilaCake.grid(row=2, column=0, sticky=W)

blackforestCake = Checkbutton(cake_frame, text="Black Forest", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var22, command=blackforestCake)
blackforestCake.grid(row=3, column=0, sticky=W)

bananaCake = Checkbutton(cake_frame, text="Banana", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var23, command=bananaCake)
bananaCake.grid(row=4, column=0, sticky=W)

brownieCake = Checkbutton(cake_frame, text="Brownie", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var24, command=brownieCake)
brownieCake.grid(row=5, column=0, sticky=W)

pineappleCake = Checkbutton(cake_frame, text="Pineapple", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var25, command=pineappleCake)
pineappleCake.grid(row=6, column=0, sticky=W)

chocolateCake = Checkbutton(cake_frame, text="Chocolate", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var26, command=chocolateCake)
chocolateCake.grid(row=7, column=0, sticky=W)

oreoCake = Checkbutton(cake_frame, text="Oreo", onvalue=1, offvalue=0, font=(
    'arial', 18, 'bold'), bg='white', variable=var27, command=oreoCake)
oreoCake.grid(row=8, column=0, sticky=W)


######### Entry Box For Cakes #############

textbuttorscotch = Entry(cake_frame, font=('arial', 18, 'bold'), justify=LEFT,
                         width=6, state=DISABLED, bd=8, textvariable=e_butterscotch)
textbuttorscotch.grid(row=0, column=1)

textapple = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                  justify=LEFT, state=DISABLED, bd=8, textvariable=e_apple)
textapple.grid(row=1, column=1)

textvanila = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                   justify=LEFT, state=DISABLED, bd=8, textvariable=e_vanilla)
textvanila.grid(row=2, column=1)

textblackforest = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                        justify=LEFT, state=DISABLED, bd=8, textvariable=e_blackforest)
textblackforest.grid(row=3, column=1)

textbanana = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                   justify=LEFT, state=DISABLED, bd=8, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrowni = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                   state=DISABLED, justify=LEFT, bd=8, textvariable=e_brownie)
textbrowni.grid(row=5, column=1)

textpineapple = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                      justify=LEFT, state=DISABLED, bd=8, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                      justify=LEFT, state=DISABLED, bd=8, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textoreo = Entry(cake_frame, font=('arial', 18, 'bold'), width=6,
                 justify=LEFT, state=DISABLED, bd=8, textvariable=e_oreo)
textoreo.grid(row=8, column=1)

######### Cost Labels ##############

labelcostofdrinks = Label(cost_frame, font=('arial', 16, 'bold'),
                          text="Cost Of Drinks\t", bg=theme, fg='cornsilk', justify=CENTER)
labelcostofdrinks.grid(row=0, column=0, sticky=W)

textcostofdrinks = Entry(cost_frame, font=('arial', 16, 'bold'), bd=7, bg='white',
                         width=14, justify=RIGHT, state='readonly', textvariable=costofdrinksvar)
textcostofdrinks.grid(row=0, column=1)

labelcostofcakes = Label(cost_frame, font=('arial', 16, 'bold'),
                         text="Cost Of Cakes\t", bg=theme, fg='cornsilk', justify=CENTER)
labelcostofcakes.grid(row=1, column=0, sticky=W)

textcostofcakes = Entry(cost_frame, font=('arial', 16, 'bold'), bd=7, bg='white',
                        width=14, justify=RIGHT, state='readonly', textvariable=costofcakesvar)
textcostofcakes.grid(row=1, column=1)

labelcostoffood = Label(cost_frame, font=('arial', 16, 'bold'),
                        text="Cost Of Food\t", bg=theme, fg='cornsilk', justify=CENTER)
labelcostoffood.grid(row=2, column=0, sticky=W)

textcostoffood = Entry(cost_frame, font=('arial', 16, 'bold'), bd=7, bg='white',
                       width=14, justify=RIGHT, state='readonly', textvariable=costoffoodvar)
textcostoffood.grid(row=2, column=1)

labelsubtotal = Label(cost_frame, font=('arial', 16, 'bold'),
                      text="   Sub Total\t", bg=theme, fg='cornsilk', justify=CENTER)
labelsubtotal.grid(row=0, column=2, sticky=W)

textsubtotal = Entry(cost_frame, font=('arial', 16, 'bold'), bd=7, bg='white',
                     width=14, justify=RIGHT, state='readonly', textvariable=subtotalvar)
textsubtotal.grid(row=0, column=3)

labelservicecharge = Label(cost_frame, font=(
    'arial', 16, 'bold'), text="   Service Charge\t", bg=theme, fg='cornsilk', justify=CENTER)
labelservicecharge.grid(row=1, column=2, sticky=W)

textservicecharge = Entry(cost_frame, font=('arial', 16, 'bold'), bd=7, bg='white',
                          width=14, justify=RIGHT, state='readonly', textvariable=servicechargevar)
textservicecharge.grid(row=1, column=3)

labeltotalcharge = Label(cost_frame, font=('arial', 16, 'bold'),
                         text="   Total Cost\t", bg=theme, fg='cornsilk', justify=CENTER)
labeltotalcharge.grid(row=2, column=2, sticky=W)

texttotalcharge = Entry(cost_frame, font=('arial', 16, 'bold'), bd=7, bg='white',
                        width=14, justify=RIGHT, state='readonly', textvariable=totalcostvar)
texttotalcharge.grid(row=2, column=3)


############ Button Frame ##########


buttonTotal = Button(button_frame, text='Total', font=('arial', 14, 'bold'),
                     fg='white', bg=theme, padx=16, pady=1, bd=4, width=4, command=CostOfItem)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(button_frame, text='Receipt', font=(
    'arial', 14, 'bold'), fg='white', bg=theme, padx=16, pady=1, bd=4, width=4, command=Receipt)
buttonReceipt.grid(row=0, column=1)

buttonsave = Button(button_frame, text='Save', font=('arial', 14, 'bold'),
                    fg='white', bg=theme, padx=16, pady=1, bd=4, width=4, command=Save)
buttonsave.grid(row=0, column=2)


buttonreset = Button(button_frame, text='Reset', font=('arial', 14, 'bold'),
                     fg='white', bg=theme, padx=16, pady=1, bd=4, width=4, command=Reset)
buttonreset.grid(row=0, column=4)

####### TEXT  AREA for Receipt #########

textreceipt = Text(receipt_frame, font=('arial', 12, 'bold'), bd=4, width=46, height=14)
textreceipt.grid(row=0, column=0)

##### Functionality Of Calculater ##############

operator = ""

def btnClick(number):
    global operator
    operator += str(number)
    textDisplay.delete(0, END)
    textDisplay.insert(END, operator)

def btnClear():
    global operator
    operator = ""
    textDisplay.delete(0, END)

def btnAns():

    try:
        global operator
        sumup = str(eval(operator))
        textDisplay.delete(0, END)
        textDisplay.insert(0, sumup)
        operator = str(sumup)
    except:
        pass

############# GUI for  Calculater ############

textDisplay = Entry(calculator_frame, font=(
    'arial', 16, 'bold'), width=35, bg='white', justify=RIGHT, bd=4)
textDisplay.grid(row=0, column=0, columnspan=4, pady=1)
textDisplay.insert(0, '0')

button7 = Button(calculator_frame, text='7', fg='yellow', bg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(7))
button7.grid(row=1, column=0)

button8 = Button(calculator_frame, text='8', fg='yellow', bg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(8))
button8.grid(row=1, column=1)

button9 = Button(calculator_frame, text='9', fg='yellow', bg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(9))
button9.grid(row=1, column=2)

buttonadd = Button(calculator_frame, text='+', fg='yellow', bg=theme, bd=7, padx=16,
                   pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick("+"))
buttonadd.grid(row=1, column=3)

button4 = Button(calculator_frame, text='4', fg='yellow', bg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(4))
button4.grid(row=2, column=0)

button5 = Button(calculator_frame, text='5', bg='white', fg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(5))
button5.grid(row=2, column=1)

button6 = Button(calculator_frame, text='6', bg='white', fg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(6))
button6.grid(row=2, column=2)

buttonsubtract = Button(calculator_frame, text='-', fg='yellow', bg=theme, bd=7,
                        padx=16, pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick('-'))
buttonsubtract.grid(row=2, column=3)

button1 = Button(calculator_frame, text='1', fg='yellow', bg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(1))
button1.grid(row=3, column=0)

button2 = Button(calculator_frame, text='2', bg='white', fg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(2))
button2.grid(row=3, column=1)

button3 = Button(calculator_frame, text='3', bg='white', fg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(3))
button3.grid(row=3, column=2)

buttonmultiply = Button(calculator_frame, text='*', fg='yellow', bg=theme, bd=7,
                        padx=16, pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick('*'))
buttonmultiply.grid(row=3, column=3)

buttonans = Button(calculator_frame, text='Ans', fg='yellow', bg=theme,
                   bd=7, padx=16, pady=1, font=('arial', 16, 'bold'), width=4, command=btnAns)
buttonans.grid(row=4, column=0)

buttonclr = Button(calculator_frame, text='Clear', fg='yellow', bg=theme,
                   bd=7, padx=16, pady=1, font=('arial', 16, 'bold'), width=4, command=btnClear)
buttonclr.grid(row=4, column=1)

button0 = Button(calculator_frame, text='0', fg='yellow', bg=theme, bd=7, padx=16,
                 pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick(0))
button0.grid(row=4, column=2)

buttondiv = Button(calculator_frame, text='/', fg='yellow', bg=theme, bd=7, padx=16,
                   pady=1, font=('arial', 16, 'bold'), width=4, command=lambda: btnClick('/'))
buttondiv.grid(row=4, column=3)

root.mainloop()