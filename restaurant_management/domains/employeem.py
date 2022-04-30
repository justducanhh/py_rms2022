from tkinter import *
from tkinter import ttk
import foodm as f
import billmanagement as b

def to_billmanagement(container,frame):
    frame.destroy()
    b.billmanagement_frame(container).pack(side=TOP, pady=10)

def to_foodmanagement(container,frame):
    frame.destroy()
    f.foodmanagement_frame(container).pack(side=TOP, pady=10)

def employeemanagement_frame(container):
    frame = ttk.Frame(container)
    label = Label(frame, text="           Employee Management", font=("Arial Bold", 20))
    label.pack(side=TOP, pady=10)
    button_ordermanagement = ttk.Button(frame, text="Bill Management",command = lambda: to_billmanagement(container,frame))
    button_ordermanagement.pack(side=TOP, pady=10)

    button_billmanagement = ttk.Button(frame, text="Food Management",command = lambda: to_foodmanagement(container,frame))
    button_billmanagement.pack(side=TOP, pady=10)

    button3 = ttk.Button(frame, text = "Exit", command = container.destroy)
    button3.pack(side=TOP, pady=10)

    return frame

