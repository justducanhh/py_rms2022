
from tkinter import *
import tkinter as tk
from tkinter import Tk, StringVar,ttk

window = Tk()
window.title("Menu")
sg = ttk.Sizegrip(window)
sg.pack(side=tk.RIGHT, fill=tk.Y)

table = [Label(window, text="Table 1"), Label(window, text="Table 2"), Label(window, text="Table 3"), Label(window, text="Table 4"), Label(window, text="Table 5"), Label(window, text="Table 6"), Label(window, text="Table 7"), Label(window, text="Table 8"), Label(window, text="Table 9"), Label(window, text="Table 10")]

Label(window, text="Ỏder", font=('arial', 50, 'bold')).pack(fill = tk.X)

Seat = Frame(window, height=1000, width=1000, bd=12, relief='raise')
Seat.pack(side=LEFT)
Menu = Frame(window, bd=12, relief='raise')

Menu.pack(side=LEFT)

f1 = Frame(Menu, bd=1, relief='raise')#main
f1.pack(side=LEFT)
f2 = Frame(Menu , bd=1, relief='raise')#extra
f2.pack(side=LEFT)
f3 = Frame(Menu,   bd=1, relief='raise')#drink
f3.pack(side=LEFT)


f5 = Frame(Seat, bd = 12, relief='raise')
f5.pack(side=LEFT)

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
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()

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


tk.Label(f1, text="    Main Source", font=('arial', 32, 'bold')) .grid(row=0, column=0)
phoBo = Checkbutton(f1, text="Pho bo  $50", variable=var1, onvalue=1, offvalue=0, font=('arial', 16 )).grid(row=1, sticky=W)
txtphoBo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoBo, width=6, justify='right', state=DISABLED)
txtphoBo.grid(row=1, column=1)

phoGa = Checkbutton(f1, text="Pho ga   $50", variable=var2, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=3, sticky=W)
txtphoGa = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoGa, width=6, justify='right', state=DISABLED)
txtphoGa.grid(row=3, column=1)

phoXaobo = Checkbutton(f1, text="Pho xao bo   $50", variable=var3, onvalue=1, offvalue=0, font=('arial', 16 )).grid(row=5, sticky=W)
txtphoXaobo = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoXaobo, width=6, justify='right', state=DISABLED)
txtphoXaobo.grid(row=5, column=1)

phoTron = Checkbutton(f1, text="Pho tron   $50", variable=var4, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=7, sticky=W)
txtphoTron = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoTron, width=6, justify='right', state=DISABLED)
txtphoTron.grid(row=7, column=1)

phoCuon = Checkbutton(f1, text="Pho bo   $50", variable=var5, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=9, sticky=W)
txtphoCuon = Entry(f1, font=('arial', 16, 'bold'), textvariable=varphoCuon, width=6, justify='right', state=DISABLED)
txtphoCuon.grid(row=9, column=1)

comRang = Checkbutton(f1, text="Com rang   $50", variable=var6, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=11, sticky=W)
txtcomRang = Entry(f1, font=('arial', 16, 'bold'), textvariable=varcomRang, width=6, justify='right', state=DISABLED)
txtcomRang.grid(row=11, column=1)



tk.Label(f2, text="Topping", font=('arial', 32, 'bold')).grid(row=0, column=0)

Quay = Checkbutton(f2, text="Quay   $50", variable=var13, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=1, sticky=W)
txtQuay = Entry(f2, font=('arial', 16, 'bold'), textvariable=varQuay, width=6, justify='right', state=DISABLED)
txtQuay.grid(row=1, column=1)

trungTran = Checkbutton(f2, text="Trung tran   $50", variable=var14, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=3, sticky=W)
txttrungTran = Entry(f2, font=('arial', 16, 'bold'), textvariable=vartrungTran, width=6, justify='right', state=DISABLED)
txttrungTran.grid(row=3, column=1)

trungNon = Checkbutton(f2, text="Trung tran   $50", variable=var15, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=5, sticky=W)
txttrungNon = Entry(f2, font=('arial', 16, 'bold'), textvariable=vartrungNon, width=6, justify='right', state=DISABLED)
txttrungNon.grid(row=5, column=1)

Extra = Checkbutton(f2, text="Them bo/ga   $50", variable=var16, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=7, sticky=W)
txtExtra = Entry(f2, font=('arial', 16, 'bold'), textvariable=varExtra, width=6, justify='right', state=DISABLED)
txtExtra.grid(row=7, column=1)


tk.Label(f3, text="Drinks", font=('arial', 32, 'bold')) .grid(row=0, column=0)

traDa = Checkbutton(f3, text="Tra da   $50", variable=var7, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=1, sticky=W)
txttraDa = Entry(f3, font=('arial', 16, 'bold'), textvariable=vartraDa, width=6, justify='right', state=DISABLED)
txttraDa.grid(row=1, column=1)

suaDau = Checkbutton(f3, text="Sua dau   $50", variable=var8, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=3, sticky=W)
txtsuaDau = Entry(f3, font=('arial', 16, 'bold'), textvariable=varsuaDau, width=6, justify='right', state=DISABLED)
txtsuaDau.grid(row=3, column=1)

suaNgo = Checkbutton(f3, text="Sua ngo  $50", variable=var9, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=5, sticky=W)
txtsuaNgo = Entry(f3, font=('arial', 16, 'bold'), textvariable=varsuaNgo, width=6, justify='right', state=DISABLED)
txtsuaNgo.grid(row=5, column=1)

coCa = Checkbutton(f3, text="Coca cola   $50", variable=var10, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=7, sticky=W)
txtcoCa = Entry(f3, font=('arial', 16, 'bold'), textvariable=varcoCa, width=6, justify='right', state=DISABLED)
txtcoCa.grid(row=7, column=1)

pepSi = Checkbutton(f3, text="Pepsi   $50", variable=var11, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=9, sticky=W)
txtpepSi = Entry(f3, font=('arial', 16, 'bold'), textvariable=varpepSi, width=6, justify='right', state=DISABLED)
txtpepSi.grid(row=9, column=1)

nuocLoc = Checkbutton(f3, text="Nuoc loc   $50", variable=var12, onvalue=1, offvalue=0, font=('arial', 16)).grid(row=11, sticky=W)
txtnuocLoc = Entry(f3, font=('arial', 16, 'bold'), textvariable=varnuocLoc, width=6, justify='right', state=DISABLED)
txtnuocLoc.grid(row=11, column=1)



#lblspacer = Label(f2, text='\n\n\n\n\n\n\n\n')
#lblspacer.grid(row=9, column=0)

window.mainloop()