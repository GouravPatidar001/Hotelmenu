#14.00
from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
#functions

def reset():
    textReceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_bati.set('0')
    e_sabji.set('0')
    e_bhindi.set('0')
    e_chawal.set('0')
    e_paneer.set('0')
    e_kajukadi.set('0')
    e_maggi.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_chai.set('0')
    e_faluda.set('0')
    e_mangoshake.set('0')
    e_coldcoffee.set('0')
    e_badammilk.set('0')
    e_jaljira.set('0')
    e_roohafza.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownle.set('0')
    e_pineapple.set('0')
    e_chocalate.set('0')
    e_blackforest.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textbati.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textbhindi.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textkajukadi.config(state=DISABLED)
    textmaggi.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textchai.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textmangoshake.config(state=DISABLED)
    textcoldcoffee.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textjaljira.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownle.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocalate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

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

    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def send():
    def send_msg():
        message=textarea.get(1.0,END)
        number=numberfield.get()
        auth='6YS4avMfhL2z3Pb7VqpEBWd5NAJ8U9XQODgmlIoiZwGFsyxKer72OnAa3eDlBmZTW4KCpjN5dsUQSoiF'
        url='https://www.fast2sms.com/dev/bulk'

        params={
            'authorization':auth,
            'message':message,
            'number':number,
            'sender-id':'FSTSMS',
            'route':'p',
            'language':'english'
        }
        response=requests.get(url,params=params)
        dic=response.json()
        result=dic.get('return')
        if result==True:
            messagebox.showinfo('Send Successfully','Message sent Succesfully')

        else:
            messagebox.showerror('Error','Something went wrong')


    root2=Toplevel()
    root2.title("SEND BILL")
    root2.config(bg='red4')
    root2.geometry('485x620+50+50')

    logoImage=PhotoImage(file='logo.png.png')
    label=Label(root2,image=logoImage,bg='red4')
    label.pack(pady=5)

    numberLabel=Label(root2,text='Mobile Number',font=('arial',18,'bold underline'),bg='red4',fg='white')
    numberLabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
    billLabel.pack(pady=5)

    textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
    textarea.pack(pady=5)
    textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

    if costoffoodvar.get()!='0 Rs':
        textarea.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n')

    if costofdrinksvar.get() != '0 Rs':
        textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')

    if costofcakesvar.get() != '0 Rs':
        textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

    textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
    textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
    textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n')

    sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='black',bd=7,relief=GROOVE,
                      command=send_msg)
    sendButton.pack(pady=5)

    root2.mainloop()

def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')

    bill_data=textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your Bill is Successfully Saved')
def receipt():
    global billnumber,date
    textReceipt.delete(1.0,END)
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%y')
    textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date)
    textReceipt.insert(END,'\n---------------------------------------------------------------------------\n')
    textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)')
    textReceipt.insert(END, '\n---------------------------------------------------------------------------\n')


    if e_roti.get()!='0':
        textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*6}\n\n')

    if e_daal.get()!='0':
        textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')

    if e_bati.get()!='0':
        textReceipt.insert(END,f'Bati\t\t\t{int(e_bati.get())*20}\n\n')

    if e_sabji.get()!='0':
        textReceipt.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*90}\n\n')

    if e_bhindi.get()!='0':
        textReceipt.insert(END,f'Bhindi\t\t\t{int(e_bhindi.get())*70}\n\n')

    if e_chawal.get()!='0':
        textReceipt.insert(END,f'Chawal\t\t\t{int(e_chawal.get())*50}\n\n')

    if e_paneer.get()!='0':
        textReceipt.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*120}\n\n')

    if e_kajukadi.get()!='0':
        textReceipt.insert(END,f'Kajukadi\t\t\t{int(e_kajukadi.get())*130}\n\n')

    if e_maggi.get()!='0':
        textReceipt.insert(END,f'Maggi\t\t\t{int(e_maggi.get())*40}\n\n')

    if e_lassi.get()!='0':
        textReceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*30}\n\n')

    if e_coffee.get()!='0':
        textReceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*30}\n\n')

    if e_chai.get()!='0':
        textReceipt.insert(END,f'Chai\t\t\t{int(e_chai.get())*20}\n\n')

    if e_faluda.get()!='0':
        textReceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*70}\n\n')

    if e_mangoshake.get()!='0':
        textReceipt.insert(END,f'Mangoshake\t\t\t{int(e_mangoshake.get())*80}\n\n')

    if e_coldcoffee.get()!='0':
        textReceipt.insert(END,f'Coldcoffee\t\t\t{int(e_coldcoffee.get())*40}\n\n')

    if e_badammilk.get()!='0':
        textReceipt.insert(END,f'Badammilk\t\t\t{int(e_badammilk.get())*60}\n\n')

    if e_jaljira.get()!='0':
        textReceipt.insert(END,f'Jaljira\t\t\t{int(e_jaljira.get())*30}\n\n')

    if e_roohafza.get()!='0':
        textReceipt.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*65}\n\n')

    if e_oreo.get()!='0':
        textReceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*400}\n\n')

    if e_apple.get()!='0':
        textReceipt.insert(END,f'Apple\t\t\t{int(e_apple.get())*500}\n\n')

    if e_kitkat.get()!='0':
        textReceipt.insert(END,f'Kitkat\t\t\t{int(e_kitkat.get())*540}\n\n')

    if e_vanilla.get()!='0':
        textReceipt.insert(END,f'Vanilla\t\t\t{int(e_vanilla.get())*425}\n\n')

    if e_banana.get()!='0':
        textReceipt.insert(END,f'Banana\t\t\t{int(e_banana.get())*320}\n\n')

    if e_brownle.get()!='0':
        textReceipt.insert(END,f'Brownle\t\t\t{int(e_brownle.get())*530}\n\n')

    if e_pineapple.get()!='0':
        textReceipt.insert(END,f'Pineapple\t\t\t{int(e_pineapple.get())*650}\n\n')

    if e_chocalate.get()!='0':
        textReceipt.insert(END,f'Chocalate\t\t\t{int(e_chocalate.get())*550}\n\n')

    if e_blackforest.get()!='0':
        textReceipt.insert(END,f'Blackforest\t\t\t{int(e_blackforest.get())*750}\n\n')

    textReceipt.insert(END,'---------------------------------------------------------------------------\n')
    if costoffoodvar.get()!='0 Rs':
        textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')

    if costoffoodvar.get() != '0 Rs':
        textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')

    if costoffoodvar.get() != '0 Rs':
        textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

    textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
    textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
    textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
    textReceipt.insert(END, '---------------------------------------------------------------------------\n')

def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    item1=int(e_roti.get())
    item2=int(e_daal.get())
    item3 = int(e_bati.get())
    item4 = int(e_sabji.get())
    item5 = int(e_bhindi.get())
    item6 = int(e_chawal.get())
    item7 = int(e_paneer.get())
    item8 = int(e_kajukadi.get())
    item9 = int(e_maggi.get())

    item10 = int(e_lassi.get())
    item11 = int(e_coffee.get())
    item12 = int(e_chai.get())
    item13 = int(e_faluda.get())
    item14 = int(e_mangoshake.get())
    item15 = int(e_coldcoffee.get())
    item16 = int(e_badammilk.get())
    item17 = int(e_jaljira.get())
    item18 = int(e_roohafza.get())

    item19 = int(e_oreo.get())
    item20 = int(e_apple.get())
    item21 = int(e_kitkat.get())
    item22 = int(e_vanilla.get())
    item23 = int(e_banana.get())
    item24 = int(e_brownle.get())
    item25 = int(e_pineapple.get())
    item26 = int(e_chocalate.get())
    item27 = int(e_blackforest.get())

    priceofFood=(item1*6)+(item2*60)+(item3*20)+(item4*90)+(item5*70)+(item6*50)+(item7*120)+(item8*130)+(item9*40)

    priceofDrinks=(item10*30)+(item11*30)+(item12*20)+(item13*70)+(item14*80)+(item15*40)+(item16*60)+(item17*30)+(item18*65)

    priceofCakes=(item19*400)+(item20*500)+(item21*540)+(item22*425)+(item23*320)+(item24*530)+(item25*650)+(item26*550)+(item27*750)

    costoffoodvar.set(str(priceofFood)+' Rs')
    costofdrinksvar.set(str(priceofDrinks)+' Rs')
    costofcakesvar.set(str(priceofCakes)+' Rs')

    subtotalofItems=priceofFood+priceofDrinks+priceofCakes
    subtotalvar.set(str(subtotalofItems)+' Rs')

    servicetaxvar.set(' 50 Rs')

    totalcost=subtotalofItems+50
    totalcostvar.set(str(totalcost)+' Rs')
def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()

    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')


def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0, END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def bati():
    if var3.get() == 1:
        textbati.config(state=NORMAL)
        textbati.delete(0, END)
        textbati.focus()

    else:
        textbati.config(state=DISABLED)
        e_bati.set('0')

def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.delete(0, END)
        textsabji.focus()

    else:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')

def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.delete(0, END)
        textchawal.focus()

    else:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')

def bhindi():
    if var5.get() == 1:
        textbhindi.config(state=NORMAL)
        textbhindi.delete(0, END)
        textbhindi.focus()

    else:
        textbhindi.config(state=DISABLED)
        e_bhindi.set('0')

def paneer():
    if var7.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0, END)
        textpaneer.focus()

    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def maggi():
    if var9.get() == 1:
        textmaggi.config(state=NORMAL)
        textmaggi.delete(0, END)
        textmaggi.focus()

    else:
        textmaggi.config(state=DISABLED)
        e_maggi.set('0')

def kajukadi():
    if var8.get() == 1:
        textkajukadi.config(state=NORMAL)
        textkajukadi.delete(0, END)
        textkajukadi.focus()

    else:
        textkajukadi.config(state=DISABLED)
        e_kajukadi.set('0')

def lassi():
    if var10.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()

    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def chai():
    if var12.get()==1:
        textchai.config(state=NORMAL)
        textchai.delete(0,END)
        textchai.focus()

    else:
        textchai.config(state=DISABLED)
        e_chai.set('0')

def faluda():
    if var13.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()

    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')

def mangoshake():
    if var14.get()==1:
        textmangoshake.config(state=NORMAL)
        textmangoshake.delete(0,END)
        textmangoshake.focus()

    else:
        textmangoshake.config(state=DISABLED)
        e_mangoshake.set('0')

def badammilk():
    if var16.get()==1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()

    else:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')

def roohafza():
    if var17.get()==1:
        textroohafza.config(state=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()

    else:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')

def coffee():
    if var12.get()==1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()

    else:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')

def coldcoffee():
    if var15.get()==1:
        textcoldcoffee.config(state=NORMAL)
        textcoldcoffee.delete(0,END)
        textcoldcoffee.focus()

    else:
        textcoldcoffee.config(state=DISABLED)
        e_coldcoffee.set('0')

def jaljira():
    if var12.get()==1:
        textjaljira.config(state=NORMAL)
        textjaljira.delete(0,END)
        textjaljira.focus()

    else:
        textjaljira.config(state=DISABLED)
        e_jaljira.set('0')

def oreo():
    if var19.get()==1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()

    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')

def apple():
    if var20.get()==1:
        textapple.config(state=NORMAL)
        textapple.delete(0,END)
        textapple.focus()

    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')

def kitkat():
    if var21.get()==1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()

    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')

def vanilla():
    if var22.get()==1:
        textvanilla.config(state=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()

    else:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')

def banana():
    if var23.get()==1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()

    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')

def brownle():
    if var24.get()==1:
        textbrownle.config(state=NORMAL)
        textbrownle.delete(0,END)
        textbrownle.focus()

    else:
        textbrownle.config(state=DISABLED)
        e_brownle.set('0')

def pineapple():
    if var25.get()==1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()

    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')

def chocalate():
    if var26.get()==1:
        textchocalate.config(state=NORMAL)
        textchocalate.delete(0,END)
        textchocalate.focus()

    else:
        textchocalate.config(state=DISABLED)
        e_chocalate.set('0')

def blackforest():
    if var27.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()

    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

root=Tk()
root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title("Restaurent Management by Gourav")
root.config(bg='firebrick4')
topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Restaurent Management System',font=('arial',30,'bold'),fg='yellow',bd=9,bg='red4',width=51)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drink',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cake',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

##Variable

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_bati=StringVar()
e_sabji=StringVar()
e_bhindi=StringVar()
e_chawal=StringVar()
e_paneer=StringVar()
e_kajukadi=StringVar()
e_maggi=StringVar()

e_lassi=StringVar()
e_coffee=StringVar()
e_chai=StringVar()
e_faluda=StringVar()
e_mangoshake=StringVar()
e_coldcoffee=StringVar()
e_badammilk=StringVar()
e_jaljira=StringVar()
e_roohafza=StringVar()

e_oreo=StringVar()
e_apple=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_banana=StringVar()
e_brownle=StringVar()
e_pineapple=StringVar()
e_chocalate=StringVar()
e_blackforest=StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_bati.set('0')
e_sabji.set('0')
e_bhindi.set('0')
e_chawal.set('0')
e_paneer.set('0')
e_kajukadi.set('0')
e_maggi.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_chai.set('0')
e_faluda.set('0')
e_mangoshake.set('0')
e_coldcoffee.set('0')
e_badammilk.set('0')
e_jaljira.set('0')
e_roohafza.set('0')

e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_banana.set('0')
e_brownle.set('0')
e_pineapple.set('0')
e_chocalate.set('0')
e_blackforest.set('0')

##FOOD

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,
                 command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,
                 command=daal)
daal.grid(row=1,column=0,sticky=W)

bati=Checkbutton(foodFrame,text='Bati',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,
                 command=bati)
bati.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,
                  command=sabji)
sabji.grid(row=3,column=0,sticky=W)

bhindi=Checkbutton(foodFrame,text='Bhindi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,
                   command=bhindi)
bhindi.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodFrame,text='Chawal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,
                   command=chawal)
chawal.grid(row=5,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=paneer)
paneer.grid(row=6,column=0,sticky=W)

kajukadi=Checkbutton(foodFrame,text='KajuKadi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,
                     command=kajukadi)
kajukadi.grid(row=7,column=0,sticky=W)

maggi=Checkbutton(foodFrame,text='Maggi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,
                  command=maggi)
maggi.grid(row=8,column=0,sticky=W)

#Entry Field for Food Items

textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textbati=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bati)
textbati.grid(row=2,column=1)

textsabji=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=3,column=1)

textbhindi=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bhindi)
textbhindi.grid(row=4,column=1)

textchawal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chawal)
textchawal.grid(row=5,column=1)

textpaneer=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=6,column=1)

textkajukadi=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kajukadi)
textkajukadi.grid(row=7,column=1)

textmaggi=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_maggi)
textmaggi.grid(row=8,column=1)

#Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

chai=Checkbutton(drinksFrame,text='Chai',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=chai)
chai.grid(row=2,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=faluda)
faluda.grid(row=3,column=0,sticky=W)

mangoshake=Checkbutton(drinksFrame,text='Mango-Shake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=mangoshake)
mangoshake.grid(row=4,column=0,sticky=W)

coldcoffee=Checkbutton(drinksFrame,text='ColdCoffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=coldcoffee)
coldcoffee.grid(row=5,column=0,sticky=W)

badammilk=Checkbutton(drinksFrame,text='Badam-Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=badammilk)
badammilk.grid(row=6,column=0,sticky=W)

jaljira=Checkbutton(drinksFrame,text='Jal-Jira',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=jaljira)
jaljira.grid(row=7,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Rooh-Afza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=roohafza)
roohafza.grid(row=8,column=0,sticky=W)

#Entry Field for drink items

textlassi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textchai=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chai)
textchai.grid(row=2,column=1)

textfaluda=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=3,column=1)

textmangoshake=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mangoshake)
textmangoshake.grid(row=4,column=1)

textcoldcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coldcoffee)
textcoldcoffee.grid(row=5,column=1)

textbadammilk=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=6,column=1)

textjaljira=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jaljira)
textjaljira.grid(row=7,column=1)

textroohafza=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=8,column=1)

#cakes
oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,
                     command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,
                       command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,
                        command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,
                       command=banana)
bananacake.grid(row=4,column=0,sticky=W)

brownlecake=Checkbutton(cakesFrame,text='Brownle',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,
                        command=brownle)
brownlecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,
                          command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocalatecake=Checkbutton(cakesFrame,text='Chocalate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,
                          command=chocalate)
chocalatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='Blackforest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,
                            command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#Entry Field for Cake Items

textoreo=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textkitkat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)

textvanilla=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)

textbanana=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)

textbrownle=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownle)
textbrownle.grid(row=5,column=1)

textpineapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)

textchocalate=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocalate)
textchocalate.grid(row=7,column=1)

textblackforest=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)

#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='red4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='red4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='red4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='red4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='red4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='red4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#BUTTONS
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=4,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=4,
                     command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=4,
                  command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=4,
                  command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=3,
                   command=reset)
buttonReset.grid(row=0,column=4)

#text area for receipt
textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                  command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                   command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonstar=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                  command=lambda:buttonClick('*'))
buttonstar.grid(row=3,column=3)

buttonans=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                   command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttondivide=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                    command=lambda:buttonClick('/'))
buttondivide.grid(row=4,column=3)

root.mainloop()