import mysql.connector as msql
from mysql.connector import Error
from config import dbDic

def inserDataIntoTable(table, columnnames, values):
    try:
        conn = msql.connect(**dbDic) 
        if conn.is_connected():
            cursor = conn.cursor()
            query = f'''INSERT INTO {table} ({columnnames}) VALUES ({values});'''
            cursor.execute(query)
            conn.commit()
            conn.close()
    except Error as e:
        print("Error while connecting to MySQL", e)

def getDataFromTable(table, where=None):
    if where is None:
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
    else:
        try:
            conn = msql.connect(**dbDic)
            if conn.is_connected():
                cursor = conn.cursor()
                sql = f'''SELECT * FROM {table} WHERE {where}'''
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

def get_foreign_key_name(table, fk):
    try:
        conn = msql.connect(**dbDic)
        if conn.is_connected():
            cursor = conn.cursor()
            sql = f'''SELECT naam FROM {table} WHERE {table}id = {fk}'''
            cursor.execute(sql)
            result = cursor.fetchall()
            return result[0][0]
    except Error as e:
        print("Error while connecting to MySQL", e)

def info_catcher_in_dictionary(table, id=None):
    result = getDataFromTable(table)
    if id is None:
        match table:
            case 'behuizing':
                datalist = [{'id':row[0], 'naam': row[1], 'aantalfans':row[2], 'afmetingen':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result]
                return datalist
            case 'cpu':
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'cores':row[3], 'socket':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result]
                return datalist
            case 'gpu':
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result]
                return datalist
            case 'moederbord':
                datalist = [{'id':row[0], 'naam': row[1], 'socket':row[2], 'ddr':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result]
                return datalist
            case 'opslag':
                datalist = [{'id':row[0], 'naam': row[1], 'type':get_foreign_key_name('type', row[2]), 'capaciteit':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result]
                return datalist
            case 'psu':
                datalist = [{'id':row[0], 'naam': row[1], 'watt':row[2], 'type':get_foreign_key_name('type', row[3]), 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result]
                return datalist
            case 'ram':
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'ddr':row[4], 'stock':row[5], 'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result]
                return datalist
            case 'user':
                datalist = [{'id':row[0], 'gebruikersnaam': row[1], 'pass':row[2], 'naam':row[3], 'adres':row[4], 'uitgegeven':row[5], 'isadmin':row[6]} for row in result]
                return datalist
            case _:
                str = f''
    else:
        match table:    
            case 'behuizing':
                datalist = [{'naam': row[1], 'aantalfans':row[2], 'afmetingen':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result if row[0] == id]
                return datalist[0]
            case 'cpu':
                datalist = [{'naam': row[1], 'clock':row[2], 'cores':row[3], 'socket':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'gpu':
                datalist = [{'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'moederbord':
                datalist = [{'naam': row[1], 'socket':row[2], 'ddr':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'opslag':
                datalist = [{'naam': row[1], 'type':get_foreign_key_name('type', row[2]), 'capaciteit':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result if row[0] == id]
                return datalist[0]
            case 'psu':
                datalist = [{'naam': row[1], 'watt':row[2], 'type':get_foreign_key_name('type', row[3]), 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result if row[0] == id]
                return datalist[0]
            case 'ram':
                datalist = [{'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'ddr':row[4], 'stock':row[5], 'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'user':
                datalist = [{'id':row[0], 'gebruikersnaam': row[1], 'pass':row[2], 'naam':row[3], 'adres':row[4], 'uitgegeven':row[5], 'isadmin':row[6]} for row in result if row[0] == id]
                return datalist[0]
            case _:
                str = f''

components = {
    'cpu': info_catcher_in_dictionary('cpu'),
    'gpu': info_catcher_in_dictionary('gpu'),
    'ram': info_catcher_in_dictionary('ram'),
    'psu': info_catcher_in_dictionary('psu'),
    'storage': info_catcher_in_dictionary('opslag'),
    'mom': info_catcher_in_dictionary('moederbord'),
    'case': info_catcher_in_dictionary('behuizing')
}