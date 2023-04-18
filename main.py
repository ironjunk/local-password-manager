# File: Main file for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from tkinter import Tk

from manager import check_status
from gui import gui_first_setup, gui_main_menu
from getpass import getpass

# ---------- Main

if __name__ == "__main__":

    root = Tk()
    root.title("Local Password Manager")
    root.geometry('500x300')

    if not check_status():
        gui_first_setup(root = root)
    else:
        gui_main_menu(root = root)
        

    # root.grid_rowconfigure(0, weight = 1)
    # root.grid_rowconfigure(1, weight = 1)
    # root.grid_rowconfigure(2, weight = 1)

    root.grid_columnconfigure(0, weight = 1)
    root.grid_columnconfigure(1, weight = 1)
    root.grid_columnconfigure(2, weight = 1)

    root.mainloop()

    # for x in sorted(list(font.families())):
    #     print(x)

    # if not mg.check_status():
    #     first_setup()
    # else:
    #     pass_master = getpass("Enter Master Password: ")
        
    #     if not mg.check_master_pass(pass_master):
    #         print("Invalid Password !")
    #         exit()