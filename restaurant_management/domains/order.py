from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import Tk, StringVar,ttk


# choose the quantity of a dish
#effect 
# if choose dish will delete "0" in entry field and change the state of the entry for the quantity
# if not  the entry will set to 0
# 
def choose_phobo(var1,txtphoBo,varphoBo):
    if var1.get() == 1:
        txtphoBo.configure(state="normal")
        txtphoBo.delete(0,END)
        txtphoBo.focus()
    elif var1.get() == 0:
        txtphoBo.configure(state="disabled")
        varphoBo.set('0')

def choose_phoga(var2,txtphoGa,varphoGa):
    if var2.get() == 1:
        txtphoGa.configure(state="normal")
        txtphoGa.delete(0,END)
        txtphoGa.focus()
    elif var2.get() == 0:
        txtphoGa.configure(state="disabled")
        varphoGa.set('0')

def choose_phoxaobo(var3,txtphoXaobo,varphoXaobo):
    if var3.get() == 1:
        txtphoXaobo.configure(state="normal")
        txtphoXaobo.delete(0,END)
        txtphoXaobo.focus()
    elif var3.get() == 0:
        txtphoXaobo.configure(state="disabled")
        varphoXaobo.set('0')

def choose_photron(var4,txtphoTron,varphoTron):
    if var4.get() == 1:
        txtphoTron.configure(state="normal")
        txtphoTron.delete(0,END)
        txtphoTron.focus()
    elif var4.get() == 0:
        txtphoTron.configure(state="disabled")
        varphoTron.set('0')

def choose_phocuon(var5,txtphoCuon,varphoCuon):
    if var5.get() == 1:
        txtphoCuon.configure(state="normal")
        txtphoCuon.delete(0,END)
        txtphoCuon.focus()
    elif var5.get() == 0:
        txtphoCuon.configure(state="disabled")
        varphoCuon.set('0')


def choose_comrang(var6,cr_e,varcomRang):
    if var6.get() == 1:
        cr_e.configure(state="normal")
        cr_e.delete(0,END)
        cr_e.focus()
    elif var6.get() == 0:
        cr_e.configure(state="disabled")
        varcomRang.set('0')

def choose_quay(var7,txtQuay,varQuay):
    if var7.get() == 1:
        txtQuay.configure(state="normal")
        txtQuay.delete(0,END)
        txtQuay.focus()
    elif var7.get() == 0:
        txtQuay.configure(state="disabled")
        varQuay.set('0')

def choose_trungtran(var8,txttrungTran,vartrungTran):
    if var8.get() == 1:
        txttrungTran.configure(state="normal")
        txttrungTran.delete(0,END)
        txttrungTran.focus()
    elif var8.get() == 0:
        txttrungTran.configure(state="disabled")
        vartrungTran.set('0')


def choose_trungnon(var9,txttrungNon,vartrungNon):
    if var9.get() == 1:
        txttrungNon.configure(state="normal")
        txttrungNon.delete(0,END)
        txttrungNon.focus()
    elif var9.get() == 0:
        txttrungNon.configure(state="disabled")
        vartrungNon.set('0')

def choose_extra(var10,txtExtra,varExtra):
    if var10.get() == 1:
        txtExtra.configure(state="normal")
        txtExtra.delete(0,END)
        txtExtra.focus()
    elif var10.get() == 0:
        txtExtra.configure(state="disabled")
        varExtra.set('0')


def choose_trada(var11,txttraDa,vartraDa):
    if var11.get() == 1:
        txttraDa.configure(state="normal")
        txttraDa.delete(0,END)
        txttraDa.focus()
    elif var11.get() == 0:
        txttraDa.configure(state="disabled")
        vartraDa.set('0')


def choose_suadau(var12,txtsuaDau,varsuaDau):
    if var12.get() == 1:
        txtsuaDau.configure(state="normal")
        txtsuaDau.delete(0,END)
        txtsuaDau.focus()
    elif var12.get() == 0:
        txtsuaDau.configure(state="disabled")
        varsuaDau.set('0')

def choose_suango(var13,txtsuaNgo,varsuaNgo):
    if var13.get() == 1:
        txtsuaNgo.configure(state="normal")
        txtsuaNgo.delete(0,END)
        txtsuaNgo.focus()
    elif var13.get() == 0:
        txtsuaNgo.configure(state="disabled")
        varsuaNgo.set('0')

def choose_coca(var14,txtcoCa,varcoCa):
    if var14.get() == 1:
        txtcoCa.configure(state="normal")
        txtcoCa.delete(0,END)
        txtcoCa.focus()
    elif var14.get() == 0:
        txtcoCa.configure(state="disabled")
        varcoCa.set('0')

def choose_pepsi(var15,txtpepSi,varpepSi):
    if var15.get() == 1:
        txtpepSi.configure(state="normal")
        txtpepSi.delete(0,END)
        txtpepSi.focus()
    elif var15.get() == 0:
        txtpepSi.configure(state="disabled")
        varpepSi.set('0')


def choose_nuocloc(var16,txtnuocLoc,varnuocLoc):
    if var16.get() == 1:
        txtnuocLoc.configure(state="normal")
        txtnuocLoc.delete(0,END)
        txtnuocLoc.focus()
    elif var16.get() == 0:
        txtnuocLoc.configure(state="disabled")
        varnuocLoc.set('0')

def switch_to_bill(container,frame):
    
    frame.destroy()
    bill_frame = Frame(container)
    bill_frame.pack()
    Label = tk.Label(bill_frame,text="Bill",font=("Arial",20,"bold"))
    Label.pack()

# main frame
def order_frame(container):
    container.title("Menu")
    sg = ttk.Sizegrip(container)
    sg.pack(side=tk.RIGHT, fill=tk.Y)

    table = [Label(container, text="Table 1"), Label(container, text="Table 2"), Label(container, text="Table 3"), Label(container, text="Table 4"), Label(container, text="Table 5"), Label(container, text="Table 6"), Label(container, text="Table 7"), Label(container, text="Table 8"), Label(container, text="Table 9"), Label(container, text="Table 10")]
    frame = ttk.Frame(container)
    frame.pack(side=LEFT, fill=BOTH, expand=True)
    topframe = ttk.Frame(frame, height=1000, width=1000)
    topframe.pack(side=TOP)
    Label(topframe, text="Ỏder", font=('arial', 50, 'bold')).pack(fill = tk.X)
    
    Menu = ttk.Frame(frame, height=1000, width=1000, relief=SUNKEN, borderwidth=5,)
    Menu.pack(side=RIGHT)

    f1 = ttk.Frame(Menu, height=1000, width=1000, relief=SUNKEN, borderwidth=5)
    f1.pack(side=RIGHT)

    separator = ttk.Separator(container, orient='vertical')
    separator.pack(fill='x')

    leftframe = ttk.Frame(frame, height=1000, width=1000, relief=SUNKEN, borderwidth=5)
    leftframe.pack(side=RIGHT,fill=Y)
    Seat = ttk.Frame(leftframe, height=1000, width=1000, relief=SUNKEN, borderwidth=5)
    Seat.pack(side=RIGHT,fill=Y)
    
    #init the variable
    var1 = IntVar() #phobo
    var2 = IntVar() #phoga
    var3 = IntVar() #phoxaobo
    var4 = IntVar() #photron
    var5 = IntVar() #phocuon
    var6 = IntVar() #comrang
    var7 = IntVar() #trada
    var8 = IntVar() #suaDau
    var9 = IntVar() #suaNgo
    var10 = IntVar() #coca
    var11 = IntVar() #pepsi 
    var12 = IntVar() #nuocloc
    var13 = IntVar() #quay
    var14 = IntVar() #trungtran
    var15 = IntVar() #trungnon
    var16 = IntVar() #extra
   
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

    #Main Menu
    varphoBo = StringVar()
    varphoGa = StringVar()
    varphoXaobo = StringVar()
    varphoTron = StringVar()
    varphoCuon = StringVar()
    varcomRang = StringVar()

    #Drinks
    vartraDa = StringVar()
    varsuaDau = StringVar()
    varsuaNgo = StringVar()
    varcoCa = StringVar()
    varpepSi = StringVar()
    varnuocLoc = StringVar()

    #Topping
    varQuay = StringVar()
    vartrungTran = StringVar()
    vartrungNon = StringVar()
    varExtra = StringVar()

    varphoBo.set("0")
    varphoGa.set("0")
    varphoXaobo.set("0")
    varphoTron.set("0")
    varphoCuon.set("0")
    varcomRang.set("0")
    vartraDa.set("0")
    varsuaDau.set("0")
    varsuaNgo.set("0")
    varcoCa.set("0")
    varpepSi.set("0")
    varnuocLoc.set("0")
    varQuay.set("0")
    vartrungTran.set("0")
    vartrungNon.set("0")
    varExtra.set("0")

    #entry fields
    tk.Label(f1, text="    Main Source", font=('arial', 32, 'bold')) .grid(row=0, column=0)
    phoBo = Checkbutton(f1, text="Pho bo  $50", variable=var1, onvalue=1, offvalue=0,command = lambda: choose_phobo(var1,txtphoBo,varphoBo), font=('arial', 16 )).grid(row=1, sticky=W)
    txtphoBo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoBo, width=6, justify='right', state=DISABLED)
    txtphoBo.grid(row=1, column=1)

    phoGa = Checkbutton(f1, text="Pho ga   $50", variable=var2, onvalue=1, offvalue=0,command = lambda:choose_phoga(var2,txtphoGa,varphoGa), font=('arial', 16)).grid(row=3, sticky=W)
    txtphoGa = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoGa, width=6, justify='right', state=DISABLED)
    txtphoGa.grid(row=3, column=1)

    phoXaobo = Checkbutton(f1, text="Pho xao bo   $50", variable=var3, onvalue=1, offvalue=0,command = lambda: choose_phoxaobo(var3,txtphoXaobo,varphoXaobo), font=('arial', 16 )).grid(row=5, sticky=W)
    txtphoXaobo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoXaobo, width=6, justify='right', state=DISABLED)
    txtphoXaobo.grid(row=5, column=1)

    phoTron = Checkbutton(f1, text="Pho tron   $50", variable=var4, onvalue=1, offvalue=0,command = lambda:choose_photron(var4,txtphoTron,varphoTron), font=('arial', 16)).grid(row=7, sticky=W)
    txtphoTron = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoTron, width=6, justify='right', state=DISABLED)
    txtphoTron.grid(row=7, column=1)

    phoCuon = Checkbutton(f1, text="Pho cuon   $50", variable=var5, onvalue=1, offvalue=0,command = lambda:choose_phocuon(var5,txtphoCuon,varphoCuon), font=('arial', 16)).grid(row=9, sticky=W)
    txtphoCuon = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoCuon, width=6, justify='right', state=DISABLED)
    txtphoCuon.grid(row=9, column=1)

    comRang = Checkbutton(f1, text="Com rang   $50", variable=var6, onvalue=1, offvalue=0,command = lambda:choose_comrang(var6,txtcomRang,varcomRang), font=('arial', 16)).grid(row=11, sticky=W)
    txtcomRang = Entry(f1, font=('arial', 16, 'bold'), textvariable=varcomRang, width=6, justify='right', state=DISABLED)
    txtcomRang.grid(row=11, column=1)

    tk.Label(f1, text="Topping", font=('arial', 32, 'bold')).grid(row=13, column=0)

    Quay = Checkbutton(f1, text="Quay   $50", variable=var7, onvalue=1, offvalue=0,command = lambda:choose_quay(var7,txtQuay,varQuay), font=('arial', 16)).grid(row=15, sticky=W)
    txtQuay = Entry(f1, font=('arial', 16, 'bold'), textvariable=varQuay, width=6, justify='right', state=DISABLED)
    txtQuay.grid(row=15, column=1)

    trungTran = Checkbutton(f1, text="Trung tran   $50", variable=var8, onvalue=1, offvalue=0,command = lambda:choose_trungtran(var8,txttrungTran,vartrungTran), font=('arial', 16)).grid(row=17, sticky=W)
    txttrungTran = Entry(f1, font=('arial', 16, 'bold'), textvariable=vartrungTran, width=6, justify='right', state=DISABLED)
    txttrungTran.grid(row=17, column=1)

    trungNon = Checkbutton(f1, text="Trung non   $50", variable=var9, onvalue=1, offvalue=0,command = lambda:choose_trungnon(var9,txttrungNon,vartrungNon), font=('arial', 16)).grid(row=19, sticky=W)
    txttrungNon = Entry(f1, font=('arial', 16, 'bold'), textvariable=vartrungNon, width=6, justify='right', state=DISABLED)
    txttrungNon.grid(row= 19, column=1)

    Extra = Checkbutton(f1, text="Them bo/ga   $50", variable=var10, onvalue=1, offvalue=0,command = lambda:choose_extra(var10,txtExtra,varExtra), font=('arial', 16)).grid(row=21, sticky=W)
    txtExtra = Entry(f1, font=('arial', 16, 'bold'), textvariable=varExtra, width=6, justify='right', state=DISABLED)
    txtExtra.grid(row=21, column=1)


    tk.Label(f1, text="Drinks", font=('arial', 32, 'bold')) .grid(row=23, column=0)

    traDa = Checkbutton(f1, text="Tra da   $50", variable=var11, onvalue=1, offvalue=0,command =lambda: choose_trada(var11,txttraDa,vartraDa), font=('arial', 16)).grid(row=25, sticky=W)
    txttraDa = Entry(f1, font=('arial', 16, 'bold'), textvariable=vartraDa, width=6, justify='right', state=DISABLED)
    txttraDa.grid(row=25, column=1)

    suaDau = Checkbutton(f1, text="Sua dau   $50", variable=var12, onvalue=1, offvalue=0,command = lambda:choose_suadau(var12,txtsuaDau,varsuaDau), font=('arial', 16)).grid(row=27, sticky=W)
    txtsuaDau = Entry(f1, font=('arial', 16, 'bold'), textvariable=varsuaDau, width=6, justify='right', state=DISABLED)
    txtsuaDau.grid(row=27, column=1)

    suaNgo = Checkbutton(f1, text="Sua ngo  $50", variable=var13, onvalue=1, offvalue=0,command = lambda:choose_suango(var13,txtsuaNgo,varsuaNgo), font=('arial', 16)).grid(row=29, sticky=W)
    txtsuaNgo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varsuaNgo, width=6, justify='right', state=DISABLED)
    txtsuaNgo.grid(row=29, column=1)

    coCa = Checkbutton(f1, text="Coca cola   $50", variable=var14, onvalue=1, offvalue=0,command = lambda:choose_coca(var14,txtcoCa,varcoCa), font=('arial', 16)).grid(row=31, sticky=W)
    txtcoCa = Entry(f1, font=('arial', 16, 'bold'), textvariable=varcoCa, width=6, justify='right', state=DISABLED)
    txtcoCa.grid(row=31, column=1)

    pepSi = Checkbutton(f1, text="Pepsi   $50", variable=var15, onvalue=1, offvalue=0,command = lambda:choose_pepsi(var15,txtpepSi,varpepSi), font=('arial', 16)).grid(row=33, sticky=W)
    txtpepSi = Entry(f1, font=('arial', 16, 'bold'), textvariable=varpepSi, width=6, justify='right', state=DISABLED)
    txtpepSi.grid(row=33, column=1)

    nuocLoc = Checkbutton(f1, text="Nuoc loc   $50", variable=var16, onvalue=1, offvalue=0,command = lambda:choose_nuocloc(var16,txtnuocLoc,varnuocLoc), font=('arial', 16)).grid(row=35, sticky=W)
    txtnuocLoc = Entry(f1, font=('arial', 16, 'bold'), textvariable=varnuocLoc, width=6, justify='right', state=DISABLED)
    txtnuocLoc.grid(row=35, column=1)

    tk.Label(f1, text="Total", font=('arial', 32, 'bold')).grid(row=37, column=0)

    seat_label = Label(Seat, text ="SEATS" ,font=('arial', 16, 'bold'),width=6, )
    seat_label.grid(row=0, column=0,sticky = W+E)
    for i in range(1, 6):
        for j in range(1, 6):
            seat_button = Button(Seat, text=str(i) + str(j) , width=6, height=2)
            seat_button.grid(row=i, column=j)
    
    to_bill_button = Button(Seat, text = "TO BILL", font=('arial', 16, 'bold'),command = lambda:switch_to_bill(container,frame))
    to_bill_button.grid(row=7, column=0,sticky = W+E)
    return frame


    
        

        
        
        
        
            

            




        
