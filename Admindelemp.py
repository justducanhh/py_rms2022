#add/edit/delete employee
from tkinter import *
import tkinter.ttk as ttk


class Admin:
    def __init__(self):
        self.__employee = []

    def add_employee(self, name, id):
        new_employee = (name, id)
        self.__employee.append(new_employee)

        for e in self.__employee:
            print(e)

    def edit_employee(self, edited_name, edited_id, or_name):
        if edited_name == or_name:
            return
        else:
            for d in self.__employee:
                if d[0] == or_name:
                    self.delete_employee(or_name)
                    new_employee = (edited_name, edited_id)
                    self.__employee.append(new_employee)
                    break

        for d in self.__employee:
            print(d)

    def delete_employee(self, name):
        for d in self.__employee:
            if d[0] == name:
                self.__employee.remove(d)
                break

        for d in self.__employee:
            print(d)


win = Tk()
win.title("Admin")
win.resizable(False, False)

# employee listbox
lbx = Listbox(win, width=40)
#lbx.grid(columnspan=3, column=0, row=0)

# Treeview(table)
columns = ('name', 'id')
table = ttk.Treeview(win, columns=columns, show='headings')
table.heading('name', text="Name")
table.heading('id', text="id")

table.grid(columnspan=3, column=0, row=0)

# Scrollbar
scrollbar = Scrollbar(win)
#scrollbar.grid(column=)

added_stuff = ""
employee_amount = 0

# Create new admin instance
new_admin = Admin()


def submit_addition(employee: Entry, id: Entry, p: Toplevel):
    data = [employee.get(), id.get()]
    table.insert('', END, values=data)

    new_admin.add_employee(employee.get(), id.get())

    p.destroy()


def submit_edition(employee: Entry, id: Entry, p: Toplevel):
    selected_item = table.selection()[0]  # Get selected item

    cur_item = table.focus()
    or_name = table.item(cur_item)['values'][0]
    edited_data = [employee.get(), id.get()]
    edited_name = employee.get()
    edited_id = id.get()

    new_admin.edit_employee(edited_name, edited_id, or_name)

    table.item(selected_item, text="blub", values=edited_data)
    p.destroy()


def add():
    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Adding new employee")

    # Add employee name
    add_text = Label(pop, text='Add name:')
    add_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    stuff_entry = Entry(pop)
    stuff_entry.grid(column=1, row=0, padx=10)

    # Add employee id
    add_id_text = Label(pop, text='ID:')
    add_id_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    id_entry = Entry(pop)
    id_entry.grid(column=1, row=1, padx=10)

    # Submit addition
    submit_add = Button(pop, text='Enter', command=lambda: submit_addition(stuff_entry, id_entry, pop))
    submit_add.grid(columnspan=2, column=0, row=2, padx=10, pady=10)


def edit():
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the employee to edit!", font=("Arial", 50))
        message.pack()
        return

    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Adding new employee")

    # Add employee name
    edit_text = Label(pop, text='Edit employee:')
    edit_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    edit_entry = Entry(pop)
    edit_entry.grid(column=1, row=0, padx=10)

    # Add employee id
    edit_id_text = Label(pop, text='Edit id:')
    edit_id_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    id_entry = Entry(pop)
    id_entry.grid(column=1, row=1, padx=10)

    # Submit addition
    submit_edit = Button(pop, text='Enter', command=lambda: submit_edition(edit_entry, id_entry, pop))
    submit_edit.grid(columnspan=2, column=0, row=2, padx=10, pady=10)


def delete():
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the employee to delete!", font=("Arial", 50))
        message.pack()
        return

    cur_item = table.focus()
    name = table.item(cur_item)['values'][0]

    new_admin.delete_employee(name)

    selected_item = table.selection()[0]  # Get selected item
    table.delete(selected_item)


add_butt = Button(win, text="Add", padx=70, command=add)
add_butt.grid(column=0, row=1, padx=50, pady=20)

edit_butt = Button(win, text="Edit", padx=70, command=edit)
edit_butt.grid(column=1, row=1, padx=50, pady=20)

del_butt = Button(win, text="Delete", padx=70, command=delete)
del_butt.grid(column=2, row=1, padx=50, pady=20)



win.mainloop()