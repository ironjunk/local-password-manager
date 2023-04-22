# File: Helper functions for Local Password Manager
# Author: Aditya Pandit

# ---------- Required Modules

from sqlite3 import connect

from passlib.hash import pbkdf2_sha256
from passlib.pwd import genword

from cryptocode import encrypt, decrypt

# ---------- Check Text

# func: to check if text does not contain any malicious code
def check_text(text = None):

    bad_keywords = ["create", "delete", "update", "alter", "and", "or", "not"]

    for keyword in bad_keywords:
        if keyword in text:
            return False
            
    return True

# ---------- Database Connection

# func: create connection to database
def connection(db_name = "lpm"):

    conn = connect(".\{}.db".format(db_name))

    return conn

# ---------- First Time Setup

# func: check first time set up
def check_first_time_setup():

    conn = connection()
    cur = conn.cursor()

    cur.execute("select name from sqlite_master where type = 'table'")
    tables = cur.fetchall()
    conn.close()

    if tables == []:
        return True
    else:
        return False
    
# func: create 'tbl_admin' and 'tbl_password' tables
def init_tables():

    conn = connection()
    cur = conn.cursor()

    cur.execute("create table if not exists tbl_admin(master_password text)")
    cur.execute("create table if not exists tbl_password(id text primary key, password text)")

    conn.commit()
    conn.close()
    return True

# ---------- Database Admin

# func: store the master password
def store_master_pass(master_password = None):

    if check_text(text = master_password):
        conn = connection()
        cur = conn.cursor()

        cur.execute("insert into tbl_admin values(?)", (pbkdf2_sha256.hash(master_password),))

        conn.commit()
        conn.close()
        return True
    else:
        return False

# func: check master password
def check_master_pass(master_password = None):

    conn = connection()
    cur = conn.cursor()

    cur.execute("select master_password from tbl_admin limit 1")
    key = cur.fetchone()[0]
    
    conn.close()
    return pbkdf2_sha256.verify(master_password, key)
    
# ---------- Generate Password

def generate_password():
    return genword(length = 16, charset = "ascii_72")

# ---------- Store Password

# func: store the password
def store_password(_id = None, password = None, master_password = None):

    if check_text(text = _id) and check_text(text = password):
        encrypted_password = encrypt(password, master_password)

        conn = connection()
        cur = conn.cursor()

        cur.execute("insert into tbl_password values(?, ?)", (_id, encrypted_password))

        conn.commit()
        conn.close()
        return True
    else:
        return False

# ---------- Update Password

# func: update the password
def update_password(_id = None, password = None, master_password = None):

    if check_text(text = _id) and check_text(text = password):
        encrypted_password = encrypt(password, master_password)

        conn = connection()
        cur = conn.cursor()

        cur.execute("update tbl_password set password = ? where id = ?", (encrypted_password, _id))

        conn.commit()
        conn.close()
        return True
    else:
        return False
    
# ---------- Retrieve Password

# func: retrieve the password
def retrieve_password(_id = None, master_password = None):

    if check_text(text = _id):
        conn = connection()
        cur = conn.cursor()

        cur.execute("select password from tbl_password where id = ?", (_id,))
        encrypted_password = cur.fetchone()[0]
        conn.close()

        decrypted_password = decrypt(encrypted_password, master_password)
        return decrypted_password
    else:
        return False

# ---------- Fetch IDs

# func: fetch stored IDs
def fetch_ids():

    conn = connection()
    cur = conn.cursor()

    cur.execute("select id from tbl_password")
    rows = cur.fetchall()
    conn.close()

    if rows:
        id_list = [x[0] for x in rows]
    else:
        id_list = []

    return sorted(id_list)

# ---------- Main

if __name__ == "__main__":
    
    print("Error\t: Not a runnable program. \nNote\t: Run main.py instead.")