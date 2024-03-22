import hashlib
#PBKDF2 is a modern hashing algorithm that is being used nowadays since it has a considerable computational cost which reduces the vulnerabilities of brute force attacks.
from hashlib import pbkdf2_hmac as pbkdf2
import mysql.connector as msql
from mysql.connector import Error
from config import dbDic
import os
import re

def create_hash(password, salt):
    #https://levelup.gitconnected.com/python-salting-your-password-hashes-3eb8ccb707f9
    #Python String encode() converts a string value into a collection of bytes, using an encoding scheme specified by the user.
    plaintext = password.encode()
    digest = pbkdf2('sha256', plaintext, salt, 100000)
    hex_hash = digest.hex()
    return hex_hash

def create_connection():
    conn = msql.connect(**dbDic)
    return conn

def store_user(username, password, naam, adres, admin=0):
    salt=os.urandom(32)
    hashed_password = create_hash(password,salt)
   
    conn = create_connection()
    if conn.is_connected():
        cursor = conn.cursor()       
        # query = f'''call insert_user_account( %s, %s, %s);'''
        # val = (username, hashed_password, salt.decode('latin1'))
        # cursor.execute(query,val)
        cursor.callproc("insert_user_account", [username, hashed_password, salt.decode('latin1'), naam, adres, admin])
        conn.commit()
        conn.close()

def check_password(userid, userPassword):
    conn = create_connection()
    sql = f'''call get_user({userid})'''
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()[0]
        
    hash_password_InDB = result[2]
    salt = result[7].encode('latin1')

    hex_hash = create_hash(userPassword,salt)
    return hex_hash == hash_password_InDB

def get_userID(username):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        result = cursor.callproc("get_userID", [username, 0])
        user_id = result[1]
        return user_id
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def get_user_data(username):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        result = cursor.callproc("get_userID", [username, 0])
        user_id = result[1]
        return user_id
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

def check_pass_cond(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*\d)(?=.*[A-Z])(?=.*[\W_])[a-zA-Z0-9\W_]{6,12}$')

    if re.match(pattern, password):
        return True
    else:
        return False
    
def username_already_exists(username):
    user_id = get_userID(username)
    if user_id is not None:
        return True
    return False
