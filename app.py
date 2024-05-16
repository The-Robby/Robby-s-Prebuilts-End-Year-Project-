from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import storing_password as sp
import data_functions as df
import ast

# -----------------------------------------------------------------------------------------GLOBALS--------------------------------------------------------------------------------
app = Flask(__name__, static_folder="static") #creates a Flask application instance named app
app.secret_key = 'your_secret_key'

# -----------------------------------------------------------------------------------------INDEX.HTML--------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    # Here we logout any accounts left in the users session
    if 'account' in session:
        session.pop('account') 
    session.clear()
    return redirect(url_for('index'))

# -----------------------------------------------------------------------------------------LOGIN.HTML--------------------------------------------------------------------------------
@app.route("/login", methods=['GET', 'POST'])
def login():
    # start with empty session to be sure
    session.clear()
    if request.method == 'POST':

        # we get username, all in lowercase and password and pass the username to get its ID
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        UserID = sp.get_userID(username)

        # if it return something it means it exists, we now pass the id togheter with the password
        if UserID != None:

            # if they match the ones in the DB we add all the info from the user to the session
            if sp.check_password(UserID ,password):
                session['account'] = df.info_catcher_in_dictionary('user', UserID)
                return redirect(url_for('dashboard'))
        return render_template("login.html", wrongcredentials=True)
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():

    # start with empty session to be sure
    session.clear()
    if request.method == 'POST':

        # we ask for all the users details from the form filled in in the html
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        name = request.form['fullname']
        adres = request.form['adres']
        if 'admin' in request.form:
            isadmin = request.form['admin']
            if isadmin == True:
                isadmin = 1
        else: isadmin = 0

        # now we check if the name already exists or not
        if not sp.username_already_exists(username):

            # now we check if the password is strong enough and meets the conditions
            if sp.check_pass_cond(password):

                # now we put all the users info in the database
                sp.store_user(username, password, name, adres, isadmin)

                # get the newly created user id
                UserID = sp.get_userID(username)

                # use it to get all the info in the correct datatype and structure and put it in the session
                session['account'] = df.info_catcher_in_dictionary('user', UserID)
                return redirect(url_for('dashboard'))
            else:
                return render_template("login.html", register=True, wrongpass=True)
        else:
            return render_template("login.html", register=True, wrongname=True, username=username)


    return render_template("login.html", register=True)

# -----------------------------------------------------------------------------------------DASHBOARD.HTML--------------------------------------------------------------------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'account' in session:
        account = session['account']
        admin = False # initialize admin variable
        noMessage = True
        noRequest = True
        # Create list of strings from the database to fill dashboard--------------------#
        prebuiltlist = [prebuilt for prebuilt in df.getDataFromTable('prebuilt')]       #
        prebuilt = df.prebuilt_name_converter(prebuiltlist)                             #
        #-------------------------------------------------------------------------------#

        if df.check_existence('message'):
            noMessage = False
        if df.check_existence('requests'):
            noRequest = False

        # render dashboard based on admin or not----------------------------------------------------#
        if account['isadmin'] == 1:                                                                 #
            admin = True                                                                            #
        return render_template('dashboard.html', account=account, admin=admin, prebuilt=prebuilt, noMessage=noMessage, noRequest=noRequest)   #
        # ------------------------------------------------------------------------------------------#
    return redirect(url_for('login'))

# -----------------------------------------------------------------------------------------BUILDER.HTML--------------------------------------------------------------------------------
@app.route('/builder', methods=['GET', 'POST'])
def builder():
    if 'account' in session:
        account = session['account']
        noButton = False
        if df.check_existence('message', userid=account['id'], returntype='bool') == True:
            noButton = True
        return render_template('builder.html', account=account, reviewcart=None, noButton=noButton)
    return redirect(url_for('login'))

@app.route('/get_options/<component>')
def get_options(component):
    components = {
    'cpu': df.info_catcher_in_dictionary('cpu'),
    'gpu': df.info_catcher_in_dictionary('gpu'),
    'ram': df.info_catcher_in_dictionary('ram'),
    'psu': df.info_catcher_in_dictionary('psu'),
    'storage': df.info_catcher_in_dictionary('opslag'),
    'mom': df.info_catcher_in_dictionary('moederbord'),
    'case': df.info_catcher_in_dictionary('behuizing'),
    'message': df.info_catcher_in_dictionary('message'),
    'prebuilt': df.info_catcher_in_dictionary('prebuilt'),
    'requests': df.info_catcher_in_dictionary('requests')
    }
    # Fetch options for the specified component which has been passed on from the html
    if component in components:
        return jsonify(components[component])
    else:
        return jsonify([])
    
#-----------------------------------------------------------------------------------------ADMIN-REVIEW.HTML----------------------------------------------------------------------------------
@app.route('/admin-review', methods = ['GET','POST'])
def admin_review():
    if 'account' in session:
        account = session['account']
        accountID = account['id']
        fail = ''
        idlist = []
        noAdminReview = True
        if request.method == 'POST':
            idlist = [(item[0], int(item[1])) for item in request.form.items() if item[1] != 'default']
            if len(idlist) < 7:
                fail = 'lengthError'
        if request.method == 'GET':
            naam = request.args.get('naam')
            if df.check_existence('message', str(naam)):
                fail = 'nameExists'
            idlist = request.args.get('idlist')
            try:
                df.inserDataIntoTable('message', 'UserID, IDLIST, naam', f'{accountID}, "{idlist}", "{naam}"')
                return redirect(url_for('builder'))
            except Exception as e:
                fail = 'inserttodatabase'
                print(f'Error: {e}')
        return render_template('admin-review.html', account=account, fail=fail, idlist=idlist, noAdminReview=noAdminReview)
    return redirect(url_for('login'))

@app.route('/review', methods = ['GET','POST'])
def review():
    if 'account' in session:
        account = session['account']
        fail = ''
        noAdminReview = True
        if account['isadmin'] == 1:
            noAdminReview = False
            return render_template('admin-review.html', account=account, fail=fail, noAdminReview=noAdminReview)
        return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/review-request', methods = ['GET','POST'])
def review_request():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            return render_template('requests.html', account=account)
        return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/request-ticket', methods = ['GET','POST'])
def request_ticket():
    if 'account' in session:
        account = session['account']
        if request.method == 'GET':
            message = str(request.args.get('ticket'))
            print(message)
            userid = account['id']
            if message != 'None':
                df.inserDataIntoTable('requests', 'userid, request', f'{userid}, "{message}"')
                return redirect(url_for('dashboard'))
        return render_template('requests.html', account=account, createTicket=True)
    return redirect(url_for('login'))

@app.route('/delete_request/<messageid>', methods = ['GET','POST'])
def delete_request(messageid):
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            df.deleteDataFromTable('requests', int(messageid))
            return redirect(url_for('review_request'))
    return redirect(url_for('login'))

@app.route('/accept_route/<messageid>', methods = ['GET','POST'])
def accept_route(messageid):
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            idlist = [id[1] for id in ast.literal_eval(df.info_catcher_in_dictionary('message', int(messageid))['idlist'])]
            title = df.info_catcher_in_dictionary('message', int(messageid))['naam']
            values = ''
            for kakid in idlist:
                values += f'{str(kakid)}, '
            values += f'"{title}"'
            values = values.rstrip(', ')
            # ['cpu', 'gpu', 'psu', 'ram', 'moederbord', 'behuizing', 'opslag']
            df.inserDataIntoTable('prebuilt', 'cpuid, gpuid, psuid, ramid, momid, behuizingid, opslagid, naam', values)
            df.deleteDataFromTable('message', int(messageid))
            return redirect(url_for('review'))
    return redirect(url_for('login'))

@app.route('/delete_route/<messageid>', methods = ['GET','POST'])
def delete_route(messageid):
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            df.deleteDataFromTable('message', int(messageid))
            return redirect(url_for('review'))
    return redirect(url_for('login'))

    

#-----------------------------------------------------------------------------------------------CART PART---------------------------------------------------------------------------------------
@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
    if 'account' in session:
        account = session['account']
        if request.method == 'POST':

            # we create the itemlist to get every possible information about every product inside a structured datatype (json type)
            itemlist = [df.info_catcher_in_dictionary(item[0],int(item[1])) for item in request.form.items() if item[1] != 'default']

            # now we simplify it for visual purposes
            cartlist = df.make_cart(itemlist)

            # pass the 2 returned values on, first is a list, second is a float
            products = cartlist[0]
            totalprice = cartlist[1]

            # we add all the items into the sessions cart
            account['cart'].extend(itemlist)

            # update the session 
            session.modified = True  

            # we pass this variable to ensure we get the right html layout
            addtocart = True

            return render_template('builder.html', account=account, addtocart=addtocart, products=products, totalprice=totalprice)
        
        else:
            return redirect(url_for('login'))
        
    return redirect(url_for('login'))

@app.route('/addtocartfromdash/<prebuilt>', methods = ['GET','POST'])
def addtocartfromdash(prebuilt):
    if 'account' in session:
        account = session['account']

        # get itemIDlist from the prebuilt and turn it into a full itemlist
        for item in df.prebuilt_name_converter(df.string_to_int_list(prebuilt), buy='buy'):
            print(item)
        itemlist = [df.info_catcher_in_dictionary(item[0],int(item[1])) for item in df.prebuilt_name_converter(df.string_to_int_list(prebuilt), buy='buy')]
        

        # now we simplify it for visual purposes
        cartlist = df.make_cart(itemlist)

        # pass the 2 returned values on, first is a list, second is a float
        products = cartlist[0]
        totalprice = cartlist[1]

        # we add all the items into the sessions cart
        account['cart'].extend(itemlist)

        # update the session 
        session.modified = True  
        
        # we pass this variable to ensure we get the right html layout
        addtocart = True
        return render_template('builder.html', account=account, addtocart=addtocart, products=products, totalprice=totalprice)

    return redirect(url_for('login'))
    

@app.route('/viewcart', methods=['GET', 'POST'])
def viewcart():
    if 'account' in session:
        account = session['account']

        # only if the cart is empty we show an empty cart text
        if len(account['cart']) == 0:
            products = ()
            totalprice = 0

            return render_template('builder.html', account=account, reviewcart=True, addtocart=False, buycart=False, products=products, totalprice=totalprice)
        
        else:

            # we simplify the itemlist stored in the sessions 'cart' for visual purposes
            cartlist = df.make_cart(account['cart'])

            # split the 2 returned values, 1st list, 2nd float
            products = cartlist[0]
            totalprice = cartlist[1]

            return render_template('builder.html', account=account, reviewcart=True, addtocart=False, buycart=False, products=products, totalprice=totalprice)
        
    return redirect(url_for('login'))

@app.route('/delete-item')
def delete_item():
    if 'account' in session:
        account = session['account']

        # we ask the item name that is passed through the url
        item_name = request.args.get('item')

        # simplifying the itemlist stored in the sessions 'cart'
        cart =  df.make_cart(account['cart']) 

        # initialize deleted item
        deleted_item = None

        # get the index of the product you want to delete inside 'i'
        for i in range(len(cart[0])):

            # if the passed on name is the same as the name in the shopping cart, delete it
            if cart[0][i] == item_name:
                deleted_item = i

                # remove the item('i') from 'cart' 
                account['cart'].pop(i)

                # stop when the item has been found
                break

        # save the session
        session.modified = True  

        return redirect(url_for('viewcart')) if deleted_item is not None else f'could not delete {cart[0][deleted_item]}'
    else:
        return redirect(url_for('login'))
    
@app.route("/buy")
def buy():
    if 'account' in session:
        account = session['account']
        if account['cart'] != []: # cant buy an empty cart
            nobuy = False
            reviewcart = False
            buycart = True
            
            # ---------------------------variables----------------------------------------------------------------------------------------------#
            table = 'user'  # table will always be user                                                                                         #
            cart = account['cart']  # get the sessions car in a local variable for readability                                                  #
            cartlist = df.make_cart(cart)  # get cartlist for visual purposes                                                                   #
            products = cartlist[0]                                                                                                              #
            totalprice = round(cartlist[1],2)                                                                                                   #
            moneyspent = df.info_catcher_in_dictionary(table, account['id'])['uitgegeven']  # get the users already spent money from database   #
            # ----------------------------------------------------------------------------------------------------------------------------------#

            # ----------------cant add a NoneType so we make it an int------------------#
            if moneyspent is None:                                                      #
                moneyspent = 0                                                          #
            # --------------------------------------------------------------------------#

            #------------------update database--------------------------------------------------------------------------------------------------------------#
            idlist = [(id['id'], id['table']) for id in cart]  # finally declare a list of id's and table names to update stock                             #
            if idlist != []:                                                                                                                                #
                for id, idtable in idlist:   # ittirate over the list                                                                                       #
                    stock = int(df.info_catcher_in_dictionary(idtable, id)['stock'])                                                                        #
                                                                                                                                                            #
                    # ----------------update stock values with one less then before---------------------#                                                   #
                    if idtable == 'moederbord':                                                         #                                                   #
                        if stock > 0:                                                                   #                                                   #
                            df.update_prebuiltDB(idtable, 'stock = stock - 1', f'momid = {id}')         #                                                   #
                        else:                                                                           #                                                   #
                            nobuy = True                                                                #                                                   #
                            buycart = False                                                             #                                                   #
                            reviewcart = True                                                           #                                                   #
                    else:                                                                               #                                                   #
                        if stock > 0:                                                                   #                                                   #
                            df.update_prebuiltDB(idtable, 'stock = stock - 1', f'{idtable}id = {id}')   #                                                   #
                        else:                                                                           #                                                   #
                            nobuy = True                                                                #                                                   #
                            buycart = False                                                             #                                                   #
                            reviewcart = True                                                           #                                                   #
                    # ----------------------------------------------------------------------------------#                                                   #
                                                                                                                                                            #
                if nobuy == False:                                                                                                                          #
                    totalmoneyspent = totalprice + moneyspent  # get the total price value in int                                                           #
                    account['cart'] = []  # empty the cart                                                                                                  #
                    account['uitgegeven'] = totalmoneyspent  # update users total money spent in local variable of the session                              #
                                                                                                                                                            #
                    # -------------update session---------------#                                                                                           #
                    session['account'] = account                #                                                                                           #
                    session.modified = True                     #                                                                                           #
                    # ------------------------------------------#                                                                                           #
                                                                                                                                                            #
                    buycart = True                                                                                                                          #
                    reviewcart = False                                                                                                                      #
                    df.update_prebuiltDB(table, f'uitgegeven = {totalmoneyspent}', f'userid = {account["id"]}')                                             # update the databases user total money spent
            #-----------------------------------------------------------------------------------------------------------------------------------------------#
    return render_template("builder.html", account=account, reviewcart=reviewcart, addtocart=False, buycart=buycart, products=products, totalprice=totalprice, nobuy=nobuy)

@app.route("/deletecart")
def deletecart():
    if 'account' in session:
        account = session['account']
        if 'cart' in account:
            account['cart'] = [] # empty the cart

            # -------------update session---------------#
            session['account'] = account                #
            session.modified = True                     #
            # ------------------------------------------#

        return redirect(url_for('viewcart' or 'dashboard'))
    
    return redirect(url_for('login'))
#------------------------------------------------------------------------------------------DEBUG.HTML----------------------------------------------------------------------------------
@app.route("/debug")
def debug():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            table = request.args.get('table') # declare variable from url argument

            # ittirate over every entity in any database.table or session to view any info--#
            if table == 'session':                                                          #
                items = [(key, value) for key, value in account.items()]                    #
            else:                                                                           #
                items = df.getDataFromTable(table)                                          #
            #-------------------------------------------------------------------------------#

        else:
            return redirect(url_for('login'))
        
    return render_template("debug.html", account=account, table=table, items=items)

#------------------------------------------------------------------------------------------PROFILE.HTML----------------------------------------------------------------------------------
@app.route("/profile")
def profile():
    if 'account' in session:

        # -----------------variables--------------------#
        account = session['account']                    #
        adres = account['adres']                        #
        username = account['gebruikersnaam']            #
        name = account['naam']                          #
        spent = account['uitgegeven']                   #
        # ----------------------------------------------#

    else:
        return redirect(url_for('login'))
    
    # simply return all defined values from the users session to view basic info
    return render_template("profile-info.html", account=account, adres=adres, username=username, name=name, spent=spent)

# -----------------------------------------------------------------------------------------UPDATEITEM.HTML--------------------------------------------------------------------------------
@app.route('/deleteitem/<table>/<itemid>', methods=['GET','POST'])
def deleteitem(table, itemid):
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:

            # rename tables to correct names like in the database ------#
            if table  in ('mom', 'storage', 'case'):                    # 
                if table == 'mom':                                      #
                    table = 'moederbord'    #---------------------------# this table has another table name
                elif table == 'storage':                                #
                    table = 'opslag'                                    #
                elif table == 'case':                                   #
                    table = 'behuizing'                                 #
            #-----------------------------------------------------------#

            df.deleteDataFromTable(table, itemid)

        return redirect(url_for('updateitem'))
    
    return redirect(url_for('login'))


@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if 'account' in session:
        account = session['account']
        table = request.form.get('table')
        
        # only render this html if you are admin
        if account['isadmin'] == 1:
            admin = True
            if request.method == 'POST':
                items = {key : value for key, value in request.form.items() if key != 'table'} #put all items with names and values inside dictionary
                print(items, "items firsdt parameter")
                # rename tables to correct names like in the database ------#
                if table  in ('mom', 'storage', 'case'):                    # 
                    if table == 'mom':                                      #
                        table = 'moederbord'    #---------------------------# this table has another table name
                    elif table == 'storage':                                #
                        table = 'opslag'                                    #
                    elif table == 'case':                                   #
                        table = 'behuizing'                                 #
                #-----------------------------------------------------------#

                stringitems = [item for item in items if item in ('naam','afmetingen','fotolink','capaciteit','socket','gddr','clock','vramcap')] # create a list of keys wich value needs to be a string type
                idstringitems = [item for item in items if item in ('leverancier', 'type')] # again for the id names

                # create the values as 1 string ----------------------------#
                values = ''                                                 #
                keys = ''                                                   #
                for key, value in items.items():                            #
                    if key in (stringitems):                                #
                        values += '"' + value + '",'                        ####
                    elif key == "prijs":
                        if ',' in value:
                            value = value.replace(',','.')
                            values += value
                            values += ',' 
                        else:
                            values += value
                            values += ',' 
                    elif key in (idstringitems):
                        if df.check_existence(key, name=value):
                            primary_key = str(df.check_existence(key, name=value, returntype="id"))
                            values += primary_key + ','
                        else:
                            str_value = '"' + value + '"'
                            df.inserDataIntoTable(key, "naam", str_value)
                            if df.check_existence(key, name=value):
                                primary_key = str(df.check_existence(key, name=value, returntype="id"))
                                values += primary_key + ','
                    else:                                                   ####
                        values += value                                     #
                        values += ','                                       #
                    if key in (idstringitems):                              #
                        keys += f'{key}id,'                                 #
                    else:                                                   #
                        keys += f'{key},'                                   #
                                                                            #
                # and finally pass them to the dedicated function handling the update event-----#
                if values != '':                                                                #
                    values = values.rstrip(",")                                                 #
                    keys = keys.rstrip(",")                                                     #
                    df.inserDataIntoTable(table, keys, values)                                  # 
                # ------------------------------------------------------------------------------# 

            return redirect(url_for('updateitem'))
        
        else:
            redirect(url_for('login'))

    return redirect(url_for('login'))

@app.route('/updateitem', methods=['POST', 'GET'])
def updateitem():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            if request.method == 'POST':

                items = {key : value for key, value in request.form.items()} #put all items with names and values inside dictionary

                # get id and remove it from dictionary afterwards-------#
                pkid = items.get('id')                                  #
                items.pop('id')                                         #
                # ------------------------------------------------------#

                # rename tables to correct names in database ---------------#
                if items['table'] not in ('mom', 'storage', 'case'):        # 
                    table = items.get('table')                              #
                else:                                                       #
                    if items['table'] == 'mom':                             #
                        table = 'moederbord'    #---------------------------# this table has another pk id name
                        pkname = 'momid'                                    #
                    elif items['table'] == 'storage':                       #
                        table = 'opslag'                                    #
                    elif items['table'] == 'case':                          #
                        table = 'behuizing'                                 #
                items.pop('table')                                          # and remove it afterwards
                #-----------------------------------------------------------#
                
                stringitems = [item for item in items if item in ('naam','afmetingen','fotolink','capaciteit','socket','gddr','clock','vramcap')] # create a list of keys wich value needs to be a string type
                idstringitems = [item for item in items if item in ('leverancier', 'type')] # again for the id names

                # create the values as 1 string ----------------------------#
                values = ''                                                 #
                for key, value in items.items():                            #
                    if key in (stringitems):                                #
                        values += key + ' = ' + '"' + value + '",'          ####
                    elif key in (idstringitems):
                        #if value returned full it means it exists and then check for that id in that table
                        if df.check_existence(key, name=value, returntype="bool"):
                            name_pk = str(df.check_existence(key, name=value, returntype="id"))
                            if isinstance(name_pk, str):
                                values += key + 'id = ' + name_pk + ','
                            else:
                                raise TypeError(f"name_pk({name_pk}) is not a string")
                    else:                                                   ####
                        values += key + ' = ' + value                       #
                        values += ','                                       #
                                                                            #
                # and finally pass them to the dedicated function handling the update event-----#
                if values != '':                                                                #
                    values = values.rstrip(",")                                                 #
                    if table == 'moederbord':                                                   #
                        df.update_prebuiltDB(table, values, f'{pkname} = {pkid}')               #
                    else:                                                                       #
                        df.update_prebuiltDB(table, values, f'{table}id = {pkid}')              #
                # ------------------------------------------------------------------------------# 
            return render_template('updateitem.html', account=account, admin=admin)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
