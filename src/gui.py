# File: GUI Functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from tkinter import Label, Entry, Button, OptionMenu, StringVar

import src.manager as mg
from pyperclip import copy

# ---------- Global Vars

op_selection = None

# ---------- Functions : Button Click Functions

# func: store the master password in the DB
def btn_func_store_master_pass(tf_master_password = None, tf_master_password_confirm = None, lbl_msg = None):
    master_password = tf_master_password.get()
    master_password_confirm = tf_master_password_confirm.get()

    try:
        if master_password == master_password_confirm:
            if master_password != "" and master_password_confirm != "" and mg.store_master_pass(master_password = master_password):
                lbl_msg.configure(text = "The master password has been set successfully!\nNote: Kindly restart the app.",
                                    fg = 'green')
            else:
                lbl_msg.configure(text = "Prohibited keywords/Blank texts not allowed in the text field!", fg = 'red')
        else:
            lbl_msg.configure(text = "The passwords in both the fields do not match.\nPlease try again.", fg = 'red')
    except Exception as exc:
        lbl_msg.configure(text = "Failed to set the master password!\nERR: {}".format(exc), fg = 'red')

# func: copy text from the text field
def btn_func_copy_text(tf_password = None, lbl_msg = None):
    try:
        text = tf_password.get()
        copy(text = text)

        lbl_msg.configure(text = "Password copied to clipboard!", fg = 'green')
    except Exception as exc:
        lbl_msg.configure(text = "Failed to copy!\nERR: {}".format(exc), fg = 'red')

# func: generate password
def btn_func_generate_password(tf_password = None, lbl_msg = None):
    try:
        password = mg.generate_password()

        tf_password.delete(0, "end")       # empty field
        tf_password.insert(0, password)    # insert into field
    except Exception as exc:
        lbl_msg.configure(text = "Failed to generate password!\nERR: {}".format(exc), fg = 'red')

# func: store password
def btn_func_store_password(tf_id = None, tf_password = None, tf_master_password = None, lbl_msg = None):
    _id = tf_id.get()
    password = tf_password.get()
    master_password = tf_master_password.get()

    try:
        if mg.check_master_pass(master_password = master_password):
            if _id != "" and password != "" and mg.store_password(_id = _id, password = password, master_password = master_password):
                lbl_msg.configure(text = "Password stored successfully!", fg = 'green')
            else:
                lbl_msg.configure(text = "Prohibited keywords/Blank texts not allowed in the text field!", fg = 'red')
        else:
            lbl_msg.configure(text = "Incorrect Master Password!", fg = 'red')
    except Exception as exc:
        lbl_msg.configure(text = "Failed to store password!\nERR: {}".format(exc), fg = 'red')

# func: update password
def btn_func_update_password(_id = None, tf_password = None, tf_master_password = None, lbl_msg = None):
    # _id = op_id.get()
    password = tf_password.get()
    master_password = tf_master_password.get()

    try:
        if mg.check_master_pass(master_password = master_password):
            if _id != "" and password != "" and mg.update_password(_id = _id, password = password, master_password = master_password):
                lbl_msg.configure(text = "Password updated successfully!", fg = 'green')
            else:
                lbl_msg.configure(text = "Prohibited keywords/Blank texts not allowed in the text field!", fg = 'red')
        else:
            lbl_msg.configure(text = "Incorrect Master Password!", fg = 'red')
    except Exception as exc:
        lbl_msg.configure(text = "Failed to update password!\nERR: {}".format(exc), fg = 'red')

# func: get drop down selection
def op_func_selection(selection):
    global op_selection
    op_selection = selection

# func: retrieve password
def btn_func_retrieve_password(_id = None, tf_password = None, tf_master_password = None, lbl_msg = None):
    # _id = op_id.get()
    master_password = tf_master_password.get()

    try:
        if mg.check_master_pass(master_password = master_password):
            password = mg.retrieve_password(_id = _id, master_password = master_password)
            if password:
                tf_password.delete(0, "end")
                tf_password.insert(0, password)
                lbl_msg.configure(text = "Password retrieved successfully!", fg = 'green')
            else:
                lbl_msg.configure(text = "Prohibited keywords not allowed in the text field!", fg = 'red')
        else:
            lbl_msg.configure(text = "Incorrect Master Password!", fg = 'red')
    except Exception as exc:
        lbl_msg.configure(text = "Failed to retrieve password!\nERR: {}".format(exc), fg = 'red')

# ---------- Functions : GUI Renders

# func: remove existing UI
def gui_remove(root = None):
    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) >= 1:
            widget.grid_forget()

# func: draw the UI for first time setup
def gui_first_time_setup(root = None):
    lbl_msg_header = Label(root, text = "It seems like this is your first time using the program. Kindly follow the instructions to get the program set up.",
                            font = "Calibri 12", wraplength = 500, justify = "center")
    lbl_msg_header.grid(row = 0, column = 0, columnspan = 2, pady = 20)

    lbl_msg_sub_header = Label(root, text = "Set a Master Password to finish first time set up.", font = "Calibri 12 bold",
                        wraplength = 500, justify = "center")
    lbl_msg_sub_header.grid(row = 1, column = 0, columnspan = 2)

    lbl_master_password = Label(root, text = "Enter Master Password:", font = "Calibri 12", justify = "left")
    lbl_master_password.grid(row = 2, column = 0, pady = 10)

    lbl_master_password_confirm = Label(root, text = "Confirm Master Password:", font = "Calibri 12", justify = "left")
    lbl_master_password_confirm.grid(row = 2, column = 1, pady = 10)

    tf_master_password = Entry(root, show = "*")
    tf_master_password.grid(row = 3, column = 0, pady = 10)

    tf_master_password_confirm = Entry(root, show = "*")
    tf_master_password_confirm.grid(row = 3, column = 1, pady = 10)

    lbl_msg = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_msg.grid(row = 5, column = 0, columnspan = 2, pady = 20)

    btn_store_master_password = Button(root, text = "Set Master Password",
                            command = lambda: btn_func_store_master_pass(tf_master_password = tf_master_password, tf_master_password_confirm = tf_master_password_confirm, lbl_msg = lbl_msg))
    btn_store_master_password.grid(row = 4, column = 0, columnspan = 2, pady = 10)

# func: render group for generate password button, password text field and copy button
def gui_group_generate_copy(root = None, group_row = None, lbl_msg = None, render_btn_generate = True):
    tf_password = Entry(root, show = "*", width = 30)
    tf_password.grid(row = group_row, column = 1, columnspan = 2, pady = 20)

    if render_btn_generate:
        btn_generate_password = Button(root, text = "Generate",
                            command = lambda: btn_func_generate_password(tf_password = tf_password, lbl_msg = lbl_msg))
        btn_generate_password.grid(row = group_row, column = 0, pady = 20)

    btn_copy = Button(root, text = "Copy",
                     command = lambda: btn_func_copy_text(tf_password = tf_password, lbl_msg = lbl_msg))
    btn_copy.grid(row = group_row, column = 3, pady = 20)

    return tf_password

# func: render group for id label, id text field and id drop down menu
def gui_group_id(root = None, group_row = None, drop_down = False):

    lbl_id = Label(root, text = "ID : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_id.grid(row = group_row, column = 0, pady = 10)

    if drop_down:
        id_list = mg.fetch_ids()

        id_menu = StringVar()
        id_menu.set("Select ID")

        op_id = OptionMenu(root, id_menu, *id_list if id_list else ["empty"], command = op_func_selection)
        op_id.grid(row = group_row, column = 1, columnspan = 2, pady = 10)

        return op_id
    else:
        tf_id = Entry(root, width = 30)
        tf_id.grid(row = group_row, column = 1, columnspan = 2, pady = 10)

        return tf_id

# func: render group for master password label, master password text field and action button
def gui_group_master_password_action(root = None, group_row = None, action_type = None, wg_id = None, tf_password = None, lbl_msg = None):
    global op_selection

    lbl_master_password = Label(root, text = "Master\nPassword : ", font = "Calibri 12", wraplength = 300, justify = "center")
    lbl_master_password.grid(row = group_row, column = 0, pady = 10)

    tf_master_password = Entry(root, show = "*", width = 30)
    tf_master_password.grid(row = group_row, column = 1, columnspan = 2, pady = 10)

    if action_type == "store":
        btn_action = Button(root, text = "Store",
                        command = lambda: btn_func_store_password(tf_id = wg_id, tf_password = tf_password, tf_master_password = tf_master_password, lbl_msg = lbl_msg))
        btn_action.grid(row = group_row, column = 3, pady = 10)
    elif action_type == "update":
        btn_action = Button(root, text = "Update",
                        command = lambda: btn_func_update_password(_id = op_selection, tf_password = tf_password, tf_master_password = tf_master_password, lbl_msg = lbl_msg))
        btn_action.grid(row = group_row, column = 3, pady = 10)
    elif action_type == "retrieve":
        btn_action = Button(root, text = "Retrieve",
                        command = lambda: btn_func_retrieve_password(_id = op_selection, tf_password = tf_password, tf_master_password = tf_master_password, lbl_msg = lbl_msg))
        btn_action.grid(row = group_row, column = 3, pady = 10)

# func: draw the UI for generate password tab
def gui_generate_password(root = None):
    gui_remove(root = root)

    lbl_msg = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_msg.grid(row = 4, column = 0, columnspan = 4)

    tf_password = gui_group_generate_copy(root = root, group_row = 1, lbl_msg = lbl_msg)

# func: draw the UI for store password tab
def gui_store_password(root = None):
    gui_remove(root = root)

    lbl_msg = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_msg.grid(row = 4, column = 0, columnspan = 4)

    wg_id = gui_group_id(root = root, group_row = 1)
    tf_password = gui_group_generate_copy(root = root, group_row = 2, lbl_msg = lbl_msg)
    gui_group_master_password_action(root = root, group_row = 3, action_type = "store", wg_id = wg_id, tf_password = tf_password, lbl_msg = lbl_msg)

# func: draw the UI for update password tab
def gui_update_password(root = None):

    gui_remove(root = root)

    lbl_msg = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_msg.grid(row = 4, column = 0, columnspan = 4)

    wg_id = gui_group_id(root = root, group_row = 1, drop_down = True)
    tf_password = gui_group_generate_copy(root = root, group_row = 2, lbl_msg = lbl_msg)
    gui_group_master_password_action(root = root, group_row = 3, action_type = "update", wg_id = wg_id, tf_password = tf_password, lbl_msg = lbl_msg)

# func: draw the UI for retrieve password tab
def gui_retrieve_password(root = None):

    gui_remove(root = root)

    lbl_msg = Label(root, font = "Calibri 12 bold", wraplength = 500, justify = "center", pady = 20)
    lbl_msg.grid(row = 4, column = 0, columnspan = 4)

    wg_id = gui_group_id(root = root, group_row = 1, drop_down = True)
    tf_password = gui_group_generate_copy(root = root, group_row = 2, lbl_msg = lbl_msg, render_btn_generate = False)
    gui_group_master_password_action(root = root, group_row = 3, action_type = "retrieve", wg_id = wg_id, tf_password = tf_password, lbl_msg = lbl_msg)

# func: draw the UI for main menu
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