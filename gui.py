# File: GUI Functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from datetime import datetime
from pyperclip import copy

import manager as mg
from tkinter import Label, Entry, Button, OptionMenu, StringVar

# ---------- Functions : Button Click Functions

# func: to store the master password in the DB
def btn_first_setup(text_field_1 = None, text_field_2 = None, lbl_bottom = None):
    pass_master = text_field_1.get()
    c_pass_master = text_field_2.get()

    if pass_master == c_pass_master:
        success = mg.store_master_pass(pass_master)
        
        if success:
            lbl_bottom.configure(text = "The Master Password has been set successfully!\nNote: Kindly restart the app.",
                                fg = 'green')
        else:
            lbl_bottom.configure(text = "The Master Password setup failed!\nKindly report to the developer.", fg = 'red')
    else:
        lbl_bottom.configure(text = "The passwords in both the fields do not match.\nPlease try again.", fg = 'red')
# ----------
# func: to generate password
def btn_generate_password(text_field_1 = None):
    password = mg.generate()

    text_field_1.delete(0, "end")       # empty field
    text_field_1.insert(0, password)    # insert into field
# ----------
# func: to copy text from the text field
def btn_copy_text(text_field_1 = None, lbl_bottom = None):
    text = text_field_1.get()

    copy(text = text)

    lbl_bottom.configure(text = "Password copied to clipboard!", fg = 'green')
# ----------
# func: to copy text from the text field
def btn_store_password(text_field_1 = None, text_field_2 = None, text_field_3 = None, lbl_bottom = None):
    _id = text_field_1.get()
    password = text_field_2.get()
    master_password = text_field_3.get()

    if mg.check_master_pass(master_password):
        if mg.store_password(_id = _id, password = password, master_password = master_password):
            lbl_bottom.configure(text = "Password stored successfully!", fg = 'green')
        else:
            lbl_bottom.configure(text = "Error in storing password.\nKindly report to developer.", fg = 'green')
    else:
        lbl_bottom.configure(text = "Incorrect Master Password!", fg = 'red')

# ---------- Functions : GUI Renders

# func: to remove existing UI
def gui_remove(root = None):

    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 1:
            widget.grid_forget()
# ----------
# func: to draw the UI for first time setup
def gui_first_setup(root = None):

    lbl_top = Label(root, text = "It seems like this is your first time using the program. Kindly follow the instructions to get the program set up.",
                            font = "Calibri 12", wraplength = 500, justify = "center")
    lbl_top.grid(row = 0, column = 0, columnspan = 2, pady = 20)

    lbl_mid = Label(root, text = "Set a Master Password to finish first time set up.", font = "Calibri 12 bold",
                        wraplength = 500, justify = "center")
    lbl_mid.grid(row = 1, column = 0, columnspan = 2)

    lbl_field_1 = Label(root, text = "Enter Master Password:", font = "Calibri 12", justify = "left")
    lbl_field_1.grid(row = 2, column = 0, pady = 10)

    lbl_field_2 = Label(root, text = "Confirm Master Password:", font = "Calibri 12", justify = "left")
    lbl_field_2.grid(row = 2, column = 1, pady = 10)

    text_field_1 = Entry(root, show = "*")
    text_field_1.grid(row = 3, column = 0, pady = 10)

    text_field_2 = Entry(root, show = "*")
    text_field_2.grid(row = 3, column = 1, pady = 10)

    lbl_bottom = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_bottom.grid(row = 5, column = 0, columnspan = 2, pady = 20)

    btn_bottom = Button(root, text = "Set Master Password",
                            command = lambda: btn_first_setup(text_field_1 = text_field_1, text_field_2 = text_field_2, lbl_bottom = lbl_bottom))
    btn_bottom.grid(row = 4, column = 0, columnspan = 2, pady = 10)
# ----------
# func: to draw the UI for generate password tab
def gui_generate_password(root = None):

    gui_remove(root = root)

    text_field_1 = Entry(root, show = "*", width = 30)
    text_field_1.grid(row = 1, column = 1, columnspan = 2, pady = 20)

    btn_generate = Button(root, text = "Generate",
                          command = lambda: btn_generate_password(text_field_1 = text_field_1))
    btn_generate.grid(row = 1, column = 0, pady = 20)

    lbl_bottom = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_bottom.grid(row = 4, column = 0, columnspan = 4)

    btn_cpy = Button(root, text = "Copy",
                     command = lambda: btn_copy_text(text_field_1 = text_field_1, lbl_bottom = lbl_bottom))
    btn_cpy.grid(row = 1, column = 3, pady = 20) 
# ----------
# func: to draw the UI for store password tab
def gui_store_password(root = None):

    gui_remove(root = root)

    lbl_1 = Label(root, text = "ID : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_1.grid(row = 1, column = 0, pady = 10)

    text_field_1 = Entry(root, width = 30)
    text_field_1.grid(row = 1, column = 1, columnspan = 2, pady = 10)

    text_field_2 = Entry(root, show = "*", width = 30)
    text_field_2.grid(row = 2, column = 1, columnspan = 2, pady = 10)

    btn_generate = Button(root, text = "Generate",
                          command = lambda: btn_generate_password(text_field_1 = text_field_2))
    btn_generate.grid(row = 2, column = 0, pady = 10)

    btn_cpy = Button(root, text = "Copy",
                     command = lambda: btn_copy_text(text_field_1 = text_field_2, lbl_bottom = lbl_bottom))
    btn_cpy.grid(row = 2, column = 3, pady = 10)

    lbl_2 = Label(root, text = "Master\nPassword : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_2.grid(row = 3, column = 0, pady = 10)

    text_field_3 = Entry(root, show = "*", width = 30)
    text_field_3.grid(row = 3, column = 1, columnspan = 2, pady = 10)

    lbl_bottom = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_bottom.grid(row = 4, column = 0, columnspan = 4)

    btn_store = Button(root, text = "Store",
                     command = lambda: btn_store_password(text_field_1 = text_field_1, text_field_2 = text_field_2, text_field_3 = text_field_3, lbl_bottom = lbl_bottom))
    btn_store.grid(row = 3, column = 3, pady = 10)
# ----------
# func: to draw the UI for update password tab
def gui_update_password(root = None):

    gui_remove(root = root)

    id_list = mg.fetch_ids()

    lbl_1 = Label(root, text = "ID : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_1.grid(row = 1, column = 0, pady = 10)

    menu = StringVar()
    menu.set("Select ID")

    drop = OptionMenu(root, menu, *id_list)
    drop.grid(row = 1, column = 1, columnspan = 2, pady = 10)

    text_field_2 = Entry(root, show = "*", width = 30)
    text_field_2.grid(row = 2, column = 1, columnspan = 2, pady = 10)

    btn_generate = Button(root, text = "Generate",
                          command = lambda: btn_generate_password(text_field_1 = text_field_2))
    btn_generate.grid(row = 2, column = 0, pady = 10)

    btn_cpy = Button(root, text = "Copy",
                     command = lambda: btn_copy_text(text_field_1 = text_field_2, lbl_bottom = lbl_bottom))
    btn_cpy.grid(row = 2, column = 3, pady = 10)

    lbl_2 = Label(root, text = "Master\nPassword : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_2.grid(row = 3, column = 0, pady = 10)

    text_field_3 = Entry(root, show = "*", width = 30)
    text_field_3.grid(row = 3, column = 1, columnspan = 2, pady = 10)

    lbl_bottom = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_bottom.grid(row = 4, column = 0, columnspan = 4)

    btn_store = Button(root, text = "Update")#,
                    #  command = lambda: btn_store_password(text_field_1 = text_field_1, text_field_2 = text_field_2, text_field_3 = text_field_3, lbl_bottom = lbl_bottom))
    btn_store.grid(row = 3, column = 3, pady = 10)
# ----------
# func: to draw the UI for update password tab
def gui_retrieve_password(root = None):

    gui_remove(root = root)

    id_list = mg.fetch_ids()

    lbl_1 = Label(root, text = "ID : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_1.grid(row = 1, column = 0, pady = 10)

    menu = StringVar()
    menu.set("Select ID")

    drop = OptionMenu(root, menu, *id_list)
    drop.grid(row = 1, column = 1, columnspan = 2, pady = 10)

    lbl_2 = Label(root, text = "Master\nPassword : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_2.grid(row = 2, column = 0, pady = 10)

    text_field_3 = Entry(root, show = "*", width = 30)
    text_field_3.grid(row = 2, column = 1, columnspan = 2, pady = 10)

    btn_store = Button(root, text = "Retrieve")#,
                    #  command = lambda: btn_store_password(text_field_1 = text_field_1, text_field_2 = text_field_2, text_field_3 = text_field_3, lbl_bottom = lbl_bottom))
    btn_store.grid(row = 2, column = 3, pady = 10)

    text_field_2 = Entry(root, show = "*", width = 30)
    text_field_2.grid(row = 3, column = 1, columnspan = 2, pady = 10)

    btn_cpy = Button(root, text = "Copy",
                     command = lambda: btn_copy_text(text_field_1 = text_field_2, lbl_bottom = lbl_bottom))
    btn_cpy.grid(row = 3, column = 3, pady = 10)

    lbl_bottom = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_bottom.grid(row = 4, column = 0, columnspan = 4)
# ----------
# func: to draw the UI for first time setup
def gui_main_menu(root = None):

    btn_menu_generate = Button(root, text = "Generate\nPassword", padx = 20, pady = 20, 
                               command = lambda: gui_generate_password(root = root))
    btn_menu_generate.grid(row = 0, column = 0, pady = 20)

    btn_menu_store = Button(root, text = "Store\nPassword", padx = 20, pady = 20,
                            command = lambda: gui_store_password(root = root))
    btn_menu_store.grid(row = 0, column = 1, pady = 20)

    btn_menu_update = Button(root, text = "Update\nPassword", padx = 20, pady = 20,
                             command = lambda: gui_update_password(root = root))
    btn_menu_update.grid(row = 0, column = 2, pady = 20)

    btn_menu_retrieve = Button(root, text = "Retrieve\nPassword", padx = 20, pady = 20,
                               command = lambda: gui_retrieve_password(root = root))
    btn_menu_retrieve.grid(row = 0, column = 3, pady = 20)

# ---------- Main

if __name__ == "__main__":
    
    print("Error\t: Not a runnable program. \nNote\t: Run main.py instead.")