import mysql.connector as msql
import ast
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

def get_prebuilt_price(prebuiltid):
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
    if table != 'moederbord':
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
    else:
        try:
            conn = msql.connect(**dbDic)
            if conn.is_connected():
                cursor = conn.cursor()
                sql = f'''SELECT naam FROM {table} WHERE momid = {fk}'''
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
                datalist = [{'id':row[0], 'naam': row[1], 'aantalfans':row[2], 'afmetingen':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6]), 'fotolink':row[7]} for row in result]
                return datalist
            case 'cpu':
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'cores':row[3], 'socket':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7]), 'fotolink':row[8]} for row in result]
                return datalist
            case 'gpu':
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7]), 'fotolink':row[8]} for row in result]
                return datalist
            case 'moederbord':
                datalist = [{'id':row[0], 'naam': row[1], 'socket':row[2], 'ddr':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7]), 'fotolink':row[8]} for row in result]
                return datalist
            case 'opslag':
                datalist = [{'id':row[0], 'naam': row[1], 'type':get_foreign_key_name('type', row[2]), 'capaciteit':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6]), 'fotolink':row[7]} for row in result]
                return datalist
            case 'psu':
                datalist = [{'id':row[0], 'naam': row[1], 'watt':row[2], 'type':get_foreign_key_name('type', row[3]), 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6]), 'fotolink':row[7]} for row in result]
                return datalist
            case 'ram':
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'ddr':row[4], 'stock':row[5], 'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7]), 'fotolink':row[8]} for row in result]
                return datalist
            case 'user':
                datalist = [{'id':row[0], 'gebruikersnaam': row[1], 'pass':row[2], 'naam':row[3], 'adres':row[4], 'uitgegeven':row[5], 'isadmin':row[6], 'cart': []} for row in result]
                return datalist
            case _:
                str = f''
    else:
        match table:    
            case 'behuizing':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'aantalfans':row[2], 'afmetingen':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6]), 'fotolink': row[7]} for row in result if row[0] == id]
                return datalist[0]
            case 'cpu':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'clock':row[2], 'cores':row[3], 'socket':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'gpu':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'moederbord':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'socket':row[2], 'ddr':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'opslag':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'type':get_foreign_key_name('type', row[2]), 'capaciteit':row[3], 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result if row[0] == id]
                return datalist[0]
            case 'psu':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'watt':row[2], 'type':get_foreign_key_name('type', row[3]), 'stock':row[4], 'prijs':row[5], 'leverancier':get_foreign_key_name('leverancier', row[6])} for row in result if row[0] == id]
                return datalist[0]
            case 'ram':
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'clock':row[2], 'capaciteit':row[3], 'ddr':row[4], 'stock':row[5], 'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
                return datalist[0]
            case 'user':
                datalist = [{'table':table, 'id':row[0], 'gebruikersnaam': row[1], 'pass':row[2], 'naam':row[3], 'adres':row[4], 'uitgegeven':row[5], 'isadmin':row[6], 'cart': []} for row in result if row[0] == id]
                return datalist[0]
            case _:
                str = f''

def make_cart(itemlistdict):
    list_of_names = [dict['leverancier'] + ' ' + dict['naam'] + ' $' + str(round(dict['prijs'], 2)) for dict in itemlistdict]
    totalprice = 0
    for dict in itemlistdict:
        totalprice += dict['prijs']
    return list_of_names, round(totalprice, 2)

def string_to_int_list(input_str):
    try:
        # Using ast.literal_eval to safely evaluate the string as a Python literal
        int_list = ast.literal_eval(input_str)
        # Filter out non-integer elements
        int_list = [x for x in int_list if isinstance(x, int)]
        return int_list
    except (SyntaxError, ValueError) as e:
        print(f"Error converting string to list: {e}")
        return None

def prebuilt_name_converter(prebuiltlist, buy=None):
    if buy == None or buy != 'buy':
        newlist = []
        for tup in prebuiltlist:
            tuplelist = []
            for i in range(len(tup)):
                if len(tup) <= 9:
                    match i:
                        case 0:
                            tuplelist.append(get_prebuilt_price(tup[i]))
                        case 1:   
                            name = get_foreign_key_name('behuizing', tup[i])
                            tuplelist.append(name)
                            image_url = info_catcher_in_dictionary('behuizing', tup[0])
                            tuplelist.append(image_url['fotolink'])
                        case 2:   
                            name = get_foreign_key_name('opslag', tup[i])
                            tuplelist.append(name)
                        case 3:   
                            name = get_foreign_key_name('cpu', tup[i])
                            tuplelist.append(name)
                        case 4:   
                            name = get_foreign_key_name('gpu', tup[i])
                            tuplelist.append(name)
                        case 5:   
                            info = info_catcher_in_dictionary('ram', tup[i])
                            string = info['leverancier'] + ' ' + info['naam'] + ' ' + info['clock']
                            tuplelist.append(f'{string}')
                        case 6:   
                            name = get_foreign_key_name('psu', tup[i])
                            tuplelist.append(name)
                        case 7:   
                            name = get_foreign_key_name('moederbord', tup[i])
                            tuplelist.append(name)
                        case 8:
                            tuplelist.append(tup[i]) 
                        case _:
                            raise ValueError("Item index cannot be empty")
                else:
                    raise ValueError("Tuple is wrong length, check if the correct tuple was given")
            idlist = list(tup)
            idlist.pop(8)
            idlist.pop(2)
            idlist.pop(0)

            tuplelist.append(idlist)
            newlist.append(tuple(tuplelist))
        return newlist
    elif buy == 'buy':
        newlist = []
        if isinstance(prebuiltlist, list):
            for item in range(len(prebuiltlist)):
                match item:
                    case 0:   
                        name = ('behuizing', prebuiltlist[item])
                        newlist.append(name)
                    case 1:   
                        name = ('opslag', prebuiltlist[item])
                        newlist.append(name)
                    case 2:   
                        name = ('cpu', prebuiltlist[item])
                        newlist.append(name)
                    case 3:   
                        name = ('gpu', prebuiltlist[item])
                        newlist.append(name)
                    case 4:   
                        name = ('ram', prebuiltlist[item])
                        newlist.append(name)
                    case 5:   
                        name = ('psu', prebuiltlist[item])
                        newlist.append(name)
                    case 6:   
                        name = ('moederbord', prebuiltlist[item])
                        newlist.append(name)
                    case _:
                        raise ValueError(f"Item index cannot be empty, errors in this list: {prebuiltlist}")
        else:
            raise TypeError(f"{prebuiltlist} is not a list, check if correct list is given")
        print(newlist)
        return newlist



components = {
    'cpu': info_catcher_in_dictionary('cpu'),
    'gpu': info_catcher_in_dictionary('gpu'),
    'ram': info_catcher_in_dictionary('ram'),
    'psu': info_catcher_in_dictionary('psu'),
    'storage': info_catcher_in_dictionary('opslag'),
    'mom': info_catcher_in_dictionary('moederbord'),
    'case': info_catcher_in_dictionary('behuizing')
}