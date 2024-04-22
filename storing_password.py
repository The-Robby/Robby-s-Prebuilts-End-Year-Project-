import hashlib
from hashlib import pbkdf2_hmac as pbkdf2
import mysql.connector as msql
from mysql.connector import Error
from config import dbDic
import os
import re

def create_hash(password, salt):
    """
    Creates a hashed password using sha256 togheter with a unknown salt

    Parameters: password (user given password)
                salt (random determined salt)
    """
    plaintext = password.encode()
    digest = pbkdf2('sha256', plaintext, salt, 100000)
    hex_hash = digest.hex()
    return hex_hash

def create_connection():
    """
    Simply create connection between database and application
    """
    conn = msql.connect(**dbDic)
    return conn

def store_user(username, password, naam, adres, admin=0):
    """
    Adds user to the database

    Parameters: Username
                Password 
                Naam
                Adres
                Admin   (these are all user inputs)
    """
    salt=os.urandom(32)
    hashed_password = create_hash(password,salt)
   
    conn = create_connection()
    if conn.is_connected():
        try:
            cursor = conn.cursor()       
            cursor.callproc("insert_user_account", [username, hashed_password, salt.decode('latin1'), naam, adres, admin])
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def check_password(userid, userPassword):
    """
    Checks if password is correct

    Parameters: userid (int)
                userPassword (string)
    
    Returns: True or False (bool)
    """
    try:
        conn = create_connection()
        sql = f'''call get_user({userid})'''
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()[0]
            
        hash_password_InDB = result[2]
        salt = result[7].encode('latin1')

        hex_hash = create_hash(userPassword,salt)
        return hex_hash == hash_password_InDB
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def get_userID(username):
    """
    Simple aid function to get the userID based on the username

    parameters: Username (str)
    """
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
        cursor.close()
        conn.close()

def get_user_data(username):
    """
    Get all data based on the username

    Parameters: Username (str)
    """
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
        cursor.close()
        conn.close()

def check_pass_cond(password):
    """
    Checks if the password is strong enough and meets conditions

    Parameters: Password (str)
    """
    pattern = re.compile(r'^(?=.*[a-z])(?=.*\d)(?=.*[A-Z])(?=.*[\W_])[a-zA-Z0-9\W_]{6,18}$')

    if re.match(pattern, password):
        return True
    else:
        return False
    
def username_already_exists(username):
    user_id = get_userID(username)
    if user_id is not None:
        return True
    return False
