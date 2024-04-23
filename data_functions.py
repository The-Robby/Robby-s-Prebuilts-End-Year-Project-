import mysql.connector as msql
import ast
from mysql.connector import Error
from config import dbDic

def inserDataIntoTable(table, columnnames, values):
    """
    insert data into any table in database

    parameters: table (what table in database)(str)
                columnnames (give column names seperated by comma in 1 string)
                values (give the corresponding values based on their column name)(str, int...)
    
    Returns: nothing, if error, check terminal
    """
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

def deleteDataFromTable(table, value):
    """
    deletes data from any table in database

    parameters: table (what table in database)(str)
                value (give the right id)(int)
    
    Returns: nothing, if error, check terminal
    """
    try:
        conn = msql.connect(**dbDic) 
        if conn.is_connected():
            cursor = conn.cursor()
            if table == 'moederbord':
                query = f'''DELETE FROM {table} WHERE momid = {value};'''
            else:
                query = f'''DELETE FROM {table} WHERE {table}id = {value};'''
            cursor.execute(query)
            conn.commit()
            conn.close()
    except Error as e:
        print("Error while connecting to MySQL", e)

def getDataFromTable(table, where=None):
    """
    gets everything from the database from the given table, if where is used it checks on conditions

    parameters: table (in what table from database)(str)

    returns: list of dictionaries (all data from given table)
        if where: a list of evry column or list of dictionary based on your where condition
    """
    try:
        conn = msql.connect(**dbDic)
        if conn.is_connected():
            cursor = conn.cursor()
            if where is None:
                sql = f'''SELECT * FROM {table}'''
            else:
                sql = f'''SELECT * FROM {table} WHERE {where}'''
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Error as e:
        print("Error while connecting to MySQL", e)

def get_prebuilt_price(prebuiltid):
    """
    gets the total price of the prebuilt

    parameters: prebuiltid (the id of the given prebuilt)(int)

    returns: totalprice in float
    """
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
    """
    update given item in database

    parameters: table (which database talbe)(str)
                set_updated_values (column_name = {value})(str)
                where (for giving the specific ID)(str)

    return:     nothing (if error, check terminal)
    """
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
    """
    Finds the name of a a foreign key, canbe used also to find just the name.

    parameters: table (for in what table we want to find the name)(str)

    returns: the name, not sure if in string or in list or something, i think list
    """
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
    """
    Catches everything from the given table and if the id is given it returns only 1 row

    parameters: table (in which table are we gonna check)(str)
                id (for what item we specifically want the data)(int)

    returns: all item data inside either a list of dictionary (when 2 or more items are returned)
            or a dictionary itself if only 1 item is returned (when id is given)
    """
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
                datalist = [{'id':row[0], 'naam': row[1], 'clock':row[2], 'vramcap':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7]), 'fotolink':row[8]} for row in result]
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
                datalist = [{'table':table, 'id':row[0], 'naam': row[1], 'clock':row[2], 'vramcap':row[3], 'gddr':row[4], 'stock':row[5],'prijs':row[6], 'leverancier':get_foreign_key_name('leverancier', row[7])} for row in result if row[0] == id]
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
    """
    Takes a list of dictionaries to turn it into a list of only names and the total price. Is used to make the cart visually look better

    Parameters: itemlistdict (a list containing all dictionaries of items returned from the database)(list[dict])

    returns: a list of names and totalprice
    """
    list_of_names = [dict['leverancier'] + ' ' + dict['naam'] + ' $' + str(round(dict['prijs'], 2)) for dict in itemlistdict]
    totalprice = 0
    for dict in itemlistdict:
        totalprice += dict['prijs']
    return list_of_names, round(totalprice, 2)

def string_to_int_list(input_str):
    """this function will convert a string in to a list of id's. 
        Is only used when a list of id's is returned from the html. 
        This results in it being a string, therefore this function.

        Parameters: string (list of ID's disguised as string)("[1,2,3,4,2,1]" --> [1,2,3,4,2,1])

        Returns: List containing all ID's
    """
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
    """this function takes every column returned from the database (which are all FK ID's)
        and converts them into tuples of their name and ID.

        Parameters: Prebuiltlist (which is the list containing every column in the database from the table (prebuilt) of one PK)(list[pk,fk,fk,fk,fk,fk,fotolink...])
                    buy (default is none and will return the list of tuples, in front is total price, in the back is IDlist) (str = "buy")
        
        Returns: tuple list of name and pk but if buy= buy it returns a list of tuples but only the parts
    """
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
            #print(idlist)
            idlist.pop(8)
            #print(idlist)
            idlist.pop(2)
            #print(idlist)

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
        #print(newlist)
        return newlist
    
def check_existence(table, name=None, id=None, returntype="bool"):
    """
    This function checks if something exists in the database.

    Parameters: Table (in which table do we want to check)(str)
                name (if only the name is known)(str)
                ID (if only PK is known)(int)
                ReturnType (you can choose what you want as returntype, default is bool)(str)
        
    Returns: Bool (true if exists, false if not found)
            ID (Returns int of PK id, possible error when item doesnt exist)
    """
    acceptedreturnvalues = ["id", "bool"]
    try:
        conn = msql.connect(**dbDic)
        if conn.is_connected():
            cursor = conn.cursor()
            if name is not None:
                print(name, table)
                sql = f'''SELECT * FROM {table} WHERE naam = "{name}"'''
            if id is not None:
                print(id, table)
                if table in ('mom', 'moederbord', 'motherboard'):
                    sql = f'''SELECT * FROM {table} WHERE momid = {id}'''
                sql = f'''SELECT * FROM {table} WHERE {table}id = {id}'''
            cursor.execute(sql)
            result = cursor.fetchall()
            if returntype == acceptedreturnvalues[0]:
                return result[0][0]
            elif returntype is acceptedreturnvalues[1]:
                print(result)
                if result != []:
                    return True
                return False
            else:
                raise ValueError(f"The accepted return values are {acceptedreturnvalues}, if you are sure you have the right accepted value, check if the item exists first")
    except Error as e:
        print("Error while connecting to MySQL", e)
    



