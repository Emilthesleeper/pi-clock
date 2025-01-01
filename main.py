import tkinter, customtkinter
from tkinter.ttk import *

import time

colors=[
    ["white", "black"],
    ["black", "white"],
    ["black", "#fed700"],
    ["white", "#fed700"],
    ["#5865F2", "white"]
]
current_color=0

root = tkinter.Tk()
root.attributes("-fullscreen", True)
root.config(background=colors[0][0], cursor="none")

def time_update():
    string = time.strftime("%H:%M:%S")
    date_str = time.strftime("%d.%m.%Y")
    label.config(text=string)
    date.config(text=date_str)
    label.after(100, time_update)

date = tkinter.Label(root, foreground=colors[0][1], background=colors[0][0], font=("DMMono", 20))
date.place(relx=0.5, rely=0.33, anchor="center")

label = tkinter.Label(root, foreground=colors[0][1], background=colors[0][0], font=("DMMono", 80))
label.place(relx=0.5, rely=0.5, anchor="center")
time_update()

def exit_bt_press():
    exit()

def color_bt_press():
    global current_color
    if current_color == len(colors)-1:
        current_color=0
    else:
        current_color+=1
    root.config(background=colors[current_color][0])
    date.config(foreground=colors[current_color][1], background=colors[current_color][0])
    label.config(foreground=colors[current_color][1], background=colors[current_color][0])
    exit_bt.configure(fg_color=colors[current_color][1], text_color=colors[current_color][0])
    color_bt.configure(fg_color=colors[current_color][1], text_color=colors[current_color][0])
    dark_bt.configure(fg_color=colors[current_color][1], text_color=colors[current_color][0])

def dark_bt_press():
    dark2_bt.place_configure(relheight=1.2, relwidth=1.2)
    dark2_bt.config(background="black")

def dark2_bt_press():
    dark2_bt.place_configure(relheight=0, relwidth=0)

exit_bt = customtkinter.CTkButton(root, text="Exit", fg_color=colors[0][1], text_color=colors[0][0], command=exit_bt_press, height=40)
exit_bt.place(relx=0.405, rely=0.7, anchor="center")

color_bt = customtkinter.CTkButton(root, text="Color", fg_color=colors[0][1], text_color=colors[0][0], command=color_bt_press, height=40)
color_bt.place(relx=0.595, rely=0.7, anchor="center")

dark_bt = customtkinter.CTkButton(root, text="Dunkelschalten", fg_color=colors[0][1], text_color=colors[0][0], command=dark_bt_press, height=40)
# dark_bt.place(relx=0.5, rely=0.775, anchor="center")

dark2_bt = tkinter.Button(root, text="", background="black", command=dark2_bt_press)
# dark2_bt.place_configure(relx=-0.1, rely=-0.1, relheight=0, relwidth=0)

tkinter.mainloop()