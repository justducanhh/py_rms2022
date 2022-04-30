from tkinter import *
from tkinter import ttk
import employeem as e
import foodm as f

def to_employeemanagement(container,frame):
    frame.destroy()
    e.employeemanagement_frame(container).pack(side=TOP, pady=10)

def to_foodmanagement(container,frame):
    frame.destroy()
    f.foodmanagement_frame(container).pack(side=TOP, pady=10)

def billmanagement_frame(container):
    frame = ttk.Frame(container)
    
    label = Label(frame, text="          Bill management", font=("Arial Bold", 20))
    label.pack(side=TOP, pady=10)

    button1 = ttk.Button(frame, text="Employee management", command=lambda: to_employeemanagement(container,frame))
    button1.pack(side=TOP, pady=10)
    button2 = ttk.Button(frame, text="Food management", command=lambda: to_foodmanagement(container,frame))
    button2.pack(side=TOP, pady=10)

    button3 = ttk.Button(frame, text = "Exit", command = container.destroy)
    button3.pack(side=TOP, pady=10)

    
    return frame