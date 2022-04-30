
from tkinter import *
from tkinter import messagebox,ttk
import order as o

import routeadmin as ra

pass_word_list =["st21","ad21"]

#staff acces    
def switch_to_staff(container,frame):
    frame.destroy()
    o.order_frame(container)

#admin access

def admin_access(container,frame):
    frame.destroy()
    ra.admin_access(container).pack(side=TOP, pady=10)
    
#login validation
def login_validate(pget,container,frame):
    if  pget== pass_word_list[0]:
        switch_to_staff(container,frame)
        
    elif pget == pass_word_list[1]:
        admin_access(container,frame)
    
    else:
        messagebox.showinfo("Error", "Invalid Password")

def create_frame(container):
    container.columnconfigure(0, weight=1)
    container.rowconfigure(1, weight=2)
    frame = ttk.Frame(container)
    label = Label(frame, text="           Password Generator", font=("Arial Bold", 20))
    label.pack(side=TOP, pady=10)

    #Password entry
    pass_label = Label(frame,text = "Enter the password: ", font=("Arial Bold", 12))
    pass_label.pack(side=TOP, pady=10)

    pass_entry = Entry(frame, width =30,show = "*")
    pass_entry.get()
    pass_entry.pack(side=TOP, pady=10)

    #Button login and exit
    login_button  = Button(frame, text="Login", command =lambda:login_validate(pass_entry.get(),container, frame))
    login_button.pack(side=TOP, pady=10)
    
    exit_button = Button(frame, text="Exit", command = container.destroy)
    exit_button.pack(side=TOP, pady=10)
    return frame


def main_window():
    root = Tk()
    root.resizable(True, True)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.title("WELCOME")
    frame_buttons = create_frame(root)
    frame_buttons.pack(side=TOP, pady=10)
    root.mainloop()

if __name__ == "__main__":
    main_window()








