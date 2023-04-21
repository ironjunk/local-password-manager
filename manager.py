# File: Helper functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from random import randint, sample
from sqlite3 import connect
from passlib.hash import pbkdf2_sha256
from cryptocode import encrypt, decrypt

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

# ---------- Store Password

# func: to create new admin table
def create_pass_table():

    conn = connection()
    c = conn.cursor()

    try:
        c.execute("create table if not exists password(id text, password text)")
        conn.commit()
        conn.close()
        
        return True
    
    except:
        print("\nError creating the password table! Kindly report the issue to the developer.")
        conn.close()
        
        return False
# ----------
# func: to store the master password
def store_password(_id = None, password = None, master_password = None):

    encrypted_password = encrypt(password, master_password)

    _ = create_pass_table()

    conn = connection()
    c = conn.cursor()

    try:
        c.execute("insert into password values(?, ?)", (_id, encrypted_password))
        conn.commit()
        conn.close()

        return True
    
    except:
        print("\nError inserting record to the password table! Kindly report the issue to the developer.")
        conn.close()
    
        return False

# ---------- Update Password
# func: to store the master password
def fetch_ids():

    conn = connection()
    c = conn.cursor()

    try:
        c.execute("select id from password")
        rows = c.fetchall()
        conn.close()

        id_list = [x[0] for x in rows]

        return sorted(id_list)
    
    except:
        print("\nError inserting record to the password table! Kindly report the issue to the developer.")
        conn.close()
    
        return []

# ---------- Generate Password

# func: to generate password
def generate(w = 4, W = 4, d = 3, s = 5):
    # func: to jumble generated password
    def jumble(gen):
        
        jumbled = sample(gen, len(gen))
        
        return "".join(jumbled)
    
    spcl_char = "#_.@"

    gen = ""

    for _ in range(w):
        gen = gen + chr(randint(97,122))

    for _ in range(W):
        gen = gen + chr(randint(65,90))

    for _ in range(d):
        gen = gen + chr(randint(48,57))

    for _ in range(s):
        gen = gen + spcl_char[randint(0,2)]

    return jumble(gen)

# ---------- Main

if __name__ == "__main__":

    fetch_ids()
    
    print("Error\t: Not a runnable program. \nNote\t: Run main.py instead.")