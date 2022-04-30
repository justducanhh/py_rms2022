from tkinter import *
from tkinter import ttk
import employeem as e
import billmanagement as b

def to_employeemanagement(container,frame):
    frame.destroy()
    e.employeemanagement_frame(container).pack(side=TOP, pady=10)

def to_billmanagement(container,frame):
    frame.destroy()
    b.billmanagement_frame(container).pack(side=TOP, pady=10)


def foodmanagement_frame(container):
    container.columnconfigure(0, weight=1)
    container.rowconfigure(1, weight=2)
    frame = ttk.Frame(container)
    label = Label(frame, text="           Food management", font=("Arial Bold", 20))
    label.pack(side=TOP, pady=10)

    button1 = ttk.Button(frame, text="Employee management", command=lambda: to_employeemanagement(container,frame))
    button1.pack(side=TOP, pady=10)

    button2 = ttk.Button(frame, text="Bill management", command=lambda: to_billmanagement(container,frame)) 
    button2.pack(side=TOP, pady=10)

    button3 = ttk.Button(frame, text = "Exit", command = container.destroy)
    button3.pack(side=TOP, pady=10)

    return frame