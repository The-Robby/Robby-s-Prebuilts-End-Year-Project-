import mysql.connector as msql
from mysql.connector import Error
from config import dbDic

def inserDataIntoTable(table, parameters, values):
    try:
        conn = msql.connect(**dbDic) 
        if conn.is_connected():
            cursor = conn.cursor()
            query = f'''INSERT INTO {table}({parameters}) VALUES({values});'''
            cursor.execute(query)
            conn.commit()
            conn.close()
    except Error as e:
        print("Error while connecting to MySQL", e)

def getDataFromTable(table):
    try:
        conn = msql.connect(**dbDic)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = f'''SELECT * FROM {table}'''
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Error as e:
        print("Error while connecting to MySQL", e)

def getTotalBuildPrice(prebuiltid):
    try:
        conn = msql.connect(**dbDic)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = f'''CALL get_total_price({prebuiltid})'''
            cursor.execute(sql)
            result = cursor.fetchone()
            return result[0] if result else None  # Assuming the result is a single value
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None  # Return None in case of an error
    
def update_prebuiltDB(table, set_updated_values, set_conditions):
    try:
        conn = msql.connect(**dbDic) 
        if conn.is_connected():
            cursor = conn.cursor()
            query = f'''UPDATE {str(table)} SET {str(set_updated_values)} WHERE {str(set_conditions)}'''
            cursor.execute(query)
            conn.commit()
            conn.close()

    except Error as e:
        print("Error while connecting to MySQL", e)



#inserDataIntoTable("prebuilt", 'TotaalBuildPrijs', getTotalBuildPrice(1))
#getDataFromTable("prebuilt")