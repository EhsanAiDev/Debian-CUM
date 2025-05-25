from customtkinter import * 
import re 
import subprocess
from funcs import *
from tkinter import *

set_appearance_mode("dark")
set_default_color_theme("./themes/theme.json")
governors = get_governors()
window = CTk()
window.maxsize(width=350, height=450)
window.minsize(width=350, height=450)
window.title("Debian Cpu Usage Manager")

current_governor = get_current_governor()
Index_Of_Current_Governor = governors.index(current_governor)

radio_frame = CTkFrame(window)
t1 = CTkLabel(window,text="Debian-CUM",font=("Helvetica",23,"bold"))
t2 = CTkLabel(window,text=f"Your Current Governor: {current_governor}",font=("Helvetica",15,"bold"))
t3 = CTkLabel(window,text="Choice a Governor To Set:",font=("Helvetica",15))

line = CTkLabel(window,text="-"*100)

user_value = StringVar(window,value=current_governor)
for governor in governors:
    Radiobutton(radio_frame, text=governor, 
                height=3,
                width=35,
                font=("Helvetica",12),
                value=governor, 
                variable=user_value, 
                indicator = 0, 
                command=lambda: set_governor(user_value.get(),t2),
                bg="#A11D1D",
                fg="#DCE4EE",
                activebackground="#8F1717",
                activeforeground="#DCE4EE",
                selectcolor="#791414",
                highlightbackground="#949A9F",
                highlightcolor="#949A9F").pack(pady=1)
t1.pack(pady=0)
t2.pack(pady=0)
t3.pack(pady=0)
radio_frame.pack()

window.mainloop()
