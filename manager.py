# File: Helper functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from random import randint, sample
from sqlite3 import connect
from passlib.hash import pbkdf2_sha256

# ---------- Database Connection

# func: to create connection to database
def connection():

    conn = connect(".\lpm.db")

    return conn
# ----------
# func: check connection status
def check_status():

    conn = connection()
    c = conn.cursor()

    try:
        c.execute("select name from sqlite_master where type = 'table' and name = 'admin'")

        if c.fetchone()[0]:
            conn.close()
            return True
        else:
            conn.close()
            return False
    
    except:
        conn.close()
        return False

# ---------- Database Admin

# func: to create new admin table
def create_admin_table():

    conn = connection()
    c = conn.cursor()

    try:
        c.execute("create table if not exists admin(master_pass text)")
        conn.commit()
        conn.close()
        
        return True
    
    except:
        print("\nError creating the admin table! Kindly report the issue to the developer.")
        conn.close()
        
        return False
# ----------
# func: to store the master password
def store_master_pass(pass_master):
    
    if create_admin_table():
        conn = connection()
        c = conn.cursor()

        try:
            c.execute("insert into admin values(?)", (pbkdf2_sha256.hash(pass_master),))
            conn.commit()
            conn.close()

            return True
        
        except:
            print("\nError adding the master password to the admin table! Kindly report the issue to the developer.")
            conn.close()
        
            return False

    return False
# ----------
# func: check password to access database
def check_master_pass(pass_master):

    conn = connection()
    c = conn.cursor()

    c.execute("select master_pass from admin limit 1")
    key = c.fetchone()[0]
    conn.close()

    return pbkdf2_sha256.verify(pass_master, key)

# ---------- Scope: Create {Begin} ---------- #



# ---------- Scope: Create {End} ---------- #

# ---------- Scope: Store {Begin} ---------- #



# ---------- Scope: Store {End} ---------- #

# ---------- Scope: Update {Begin} ---------- #
# ---------- Scope: Update {End} ---------- #

# ---------- Scope: Generate {Begin} ---------- #

# func: to generate password
def generate(w = 1, W = 1, d = 1, s = 1):
    
    spcl_char = "#_.@"

    gen = ""

    for i in range(w):
        gen = gen + chr(randint(97,122))

    for i in range(W):
        gen = gen + chr(randint(65,90))

    for i in range(d):
        gen = gen + chr(randint(48,57))

    for i in range(s):
        gen = gen + spcl_char[randint(0,2)]

    return jumble(gen)

# func: to extract parameter values
def separate(value):
    
    return [int(x) for x in value]

# func: to jumble generated password
def jumble(gen):
    
    jumbled = sample(gen, len(gen))
    
    return "".join(jumbled)

# ---------- Scope: Generate {End} ---------- #

# ---------- Scope: Main {Begin} ---------- #

if __name__ == "__main__":
    
    print("Error : Not a runnable program. \nNote : Run lpm_main.py")


    # value = input("Enter Value: ")
    # w, W, d, s = separate(value)
    
    # pswd = generate(w, W, d, s)
    # print(pswd)

# ---------- Scope: Main {End} ---------- #