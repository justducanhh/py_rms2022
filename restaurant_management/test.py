from cmath import phase
from tkinter import *
from unicodedata import name
root = Tk()

display_text=StringVar()


def put1_in_textbox(val):
    val = display_text.get()

   




Menu = {"Pho bo":"$3.50", "Chao ga":"$3.99", "pho xao":"$4.10", "Com rang":"$3.80"}
choices = [m + "  " + Menu[m] for m in Menu]

var=StringVar()
var.set(choices[0])
display_text.set(choices[0]) 
popupMenu = OptionMenu(root, var, *choices, command = put1_in_textbox)
popupMenu.grid(row=1, column=1)

root.mainloop()

class Order():
#them id
    def init(self,dish,quantity):
        self.dish.append(dish)
        self.quantity.append(quantity)

    def total_price(self):
        total=0
        for i in range(len(self.dish)):
            total+=self.dish[i].getPrice() * self.__quantity[i]
        return total
    
    
class Dish():
    def init(self,name,price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

if __name__ == "__main__":
    order = Order()
    pho = Dish()
    

