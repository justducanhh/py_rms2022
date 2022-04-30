from tkinter import *
from tkinter import messagebox,ttk
import billmanagement as b
import employeem as e
import foodm as f

def to_employee(container,frame):
    frame.destroy()
    e.employeemanagement_frame(container).pack(side=LEFT, pady=10)

def to_billmanagement(container,frame):
    frame.destroy()
    b.billmanagement_frame(container).pack(side=LEFT, pady=10)

def to_food(container,frame):
    frame.destroy()
    f.foodmanagement_frame(container).pack(side=LEFT, pady=10)

def admin_access(container):
    frame = ttk.Frame(container)
    label = Label(frame, text="           Food management", font=("Arial Bold", 20))
    label.pack(side=TOP, pady=10)
    button1 = Button(frame, text="Employee ", command=lambda:to_employee(container,frame))
    button1.pack(side=TOP, pady=10)
    button2 = Button(frame, text="Bills", command=lambda:to_billmanagement(container,frame))
    button2.pack(side=TOP, pady=10)
    button3 = Button(frame, text="Food", command=lambda:to_food(container,frame))
    button3.pack(side=TOP, pady=10)
    return frame
    
