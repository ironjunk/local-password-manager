# File: Main file for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from tkinter import Tk, PhotoImage

from manager import check_first_time_setup, init_tables
from gui import gui_first_time_setup, gui_main_menu

# ---------- Main

if __name__ == "__main__":

    app_version = 1

    lpm_win = Tk()
    lpm_win.title("Local Password Manager (v{})".format(app_version))
    lpm_win.geometry('500x400')

    favicon = PhotoImage(file = "favicon.png")
    lpm_win.iconphoto(False, favicon)

    if check_first_time_setup():
        init_tables()

        gui_first_time_setup(root = lpm_win)
    else:
        gui_main_menu(root = lpm_win)

    for ncol in range(4):
        lpm_win.grid_columnconfigure(ncol, weight = 1)

    lpm_win.mainloop()