from cmath import phase
from tkinter import *
import tkinter.ttk as ttk


class Order:
    # them id
    def __init__(self, dish):
        self.__dish = []  # Inputting tuples as elements
        self.__dish = dish


root = Tk()
root.resizable(False, False)
root.title("Order")

display_text = StringVar()
e1 = Label(root, textvariable=display_text)
e1.grid(row=0, column=0)


# Get the values from the table to put into the order
def get_order_values():
    list_of_entries = table.get_children()
    ordered = []
    for each in list_of_entries:
        name = table.item(each)['values'][0]
        quan = table.item(each)['values'][1]
        dish = (name, quan)
        ordered.append(dish)
    return ordered


def submit_order():
    new_order = Order(get_order_values())


def submit_edition(eff, e: Entry, t: Toplevel):
    cur_item = table.focus()
    or_name = table.item(cur_item)['values'][0]
    edited_data = [or_name, e.get()]
    selected_item = table.selection()[0]
    table.item(selected_item, text="blub", values=edited_data)
    t.destroy()


def edit_order(event):
    pop = Toplevel()
    pop.resizable(False, False)
    pop.title("Edit quantity")

    edit_text = Label(pop, text="Edit quantity:", font=("Arial", 10))
    edit_text.grid(column=0, row=0, padx=10, pady=10)

    edit_entry = Entry(pop, font=("Arial", 10))
    edit_entry.grid(column=1, row=0, padx=10, pady=10)
    edit_entry.bind('<Return>', lambda eff: submit_edition(eff, edit_entry, pop))


name_data = ""
quantity_data = ""

columns = ('name', 'quantity')
table = ttk.Treeview(root, columns=columns, show='headings', height=5)
table.heading('name', text="Name")
table.heading('quantity', text="Quantity")
table.bind('<Double-1>', edit_order)  # execute edit_order() on 'double click'

table.grid(column=1, row=0, padx=10)


def add(event):
    # Extract quantity data from entry set
    global quantity_data
    global name_data
    quantity_data = quantity.get()

    new_data = [name_data, quantity_data]
    table.insert('', END, values=new_data)


def option_menu_select(val):
    display_text.set(val)
    choice = var.get()
    for i in range(len(choices)):
        if choices[i] == choice:
            # Extract name of the selected option
            global name_data
            name_data = Menu[i][0]
            return


Menu = [("Pho bo", "$3.50"), ("Chao ga", "$3.99"), ("pho xao", "$4.10"), ("Com rang", "$3.80")]
choices = [Menu[i][0] + "  " + Menu[i][1] for i in range(len(Menu))]

var = StringVar()
var.set(choices[0])
selected = var.get()
for i in range(len(choices)):
    if choices[i] == selected:
        # Extract name of the selected option
        name_data = Menu[i][0]
display_text.set(choices[0])
popupMenu = OptionMenu(root, var, *choices, command=option_menu_select)
popupMenu.grid(row=1, column=0)


quantity = Entry(root)
quantity.grid(row=1, column=1, sticky=W)
quantity.bind("<Return>", add)  # execute say_hello() on Enter

# Submit button
submit = Button(root, text="Submit", padx=30, pady=5, command=submit_order)
submit.grid(columnspan=2, row=2, column=0)

root.mainloop()