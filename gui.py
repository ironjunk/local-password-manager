# File: GUI Functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from datetime import datetime

import manager as mg
from tkinter import Label, Entry, Button

# ---------- Functions : Button Click Functions

# func: to store the master password in the DB
def first_setup(text_field_1 = None, text_field_2 = None, lbl_bottom = None):
    pass_master = text_field_1.get()
    c_pass_master = text_field_2.get()

    if pass_master == c_pass_master:
        success = mg.store_master_pass(pass_master)
        
        if success:
            lbl_bottom.configure(text = f"{datetime.now()} :\nThe Master Password has been set successfully!\nNote: Kindly restart the app.",
                                fg = 'green')
        else:
            lbl_bottom.configure(text = f"{datetime.now()} :\nThe Master Password setup failed!\nKindly report to the developer.", fg = 'red')
    else:
        lbl_bottom.configure(text = f"{datetime.now()} :\nThe passwords in both the fields do not match.\nPlease try again.", fg = 'red')

# ---------- Functions : GUI Renders

# func: to draw the UI for first time setup
def gui_first_setup(root = None):

    lbl_top = Label(root, text = "It seems like this is your first time using the program. Kindly follow the instructions to get the program set up.",
                            font = "Calibri 12", wraplength = 500, justify = "center", pady = 20)
    lbl_top.grid(row = 0, column = 0, columnspan = 2)

    lbl_mid = Label(root, text = "Set a Master Password to finish first time set up.", font = "Calibri 12 bold",
                        wraplength = 500, justify = "center")
    lbl_mid.grid(row = 1, column = 0, columnspan = 2)

    lbl_field_1 = Label(root, text = "Enter Master Password:", font = "Calibri 12", justify = "left", pady = 20)
    lbl_field_1.grid(row = 2, column = 0)

    lbl_field_2 = Label(root, text = "Confirm Master Password:", font = "Calibri 12", justify = "left", pady = 20)
    lbl_field_2.grid(row = 2, column = 1)

    text_field_1 = Entry(root, show = "*")
    text_field_1.grid(row = 3, column = 0)

    text_field_2 = Entry(root, show = "*")
    text_field_2.grid(row = 3, column = 1)

    lbl_bottom = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_bottom.grid(row = 5, column = 0, columnspan = 2)

    btn_bottom = Button(root, text = "Set Master Password",
                            command = lambda: first_setup(text_field_1 = text_field_1, text_field_2 = text_field_2, lbl_bottom = lbl_bottom))
    btn_bottom.grid(row = 4, column = 0, columnspan = 2)