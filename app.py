from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import storing_password as sp
import data_functions as df


# -----------------------------------------------------------------------------------------GLOBALS--------------------------------------------------------------------------------
app = Flask(__name__, static_folder="static") #creates a Flask application instance named app
app.secret_key = 'your_secret_key'

# -----------------------------------------------------------------------------------------INDEX.HTML--------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    if 'account' in session:
        session.pop('account')
    return redirect(url_for('index'))

# -----------------------------------------------------------------------------------------LOGIN.HTML--------------------------------------------------------------------------------
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        UserID = sp.get_userID(username)
        if sp.check_password(UserID ,password):
            session['account'] = df.info_catcher_in_dictionary('user', UserID)
            return redirect(url_for('dashboard'))
        return render_template("login.html", wrongcredentials=True)
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
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
        if not sp.username_already_exists(username):
            if sp.check_pass_cond(password):
                sp.store_user(username, password, name, adres, isadmin)
                UserID = sp.get_userID(username)
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
        admin = False
        if account['isadmin'] == 1:
            admin = True
        return render_template('dashboard.html', account=account, admin=admin)
    return redirect(url_for('login'))

# -----------------------------------------------------------------------------------------BUILDER.HTML--------------------------------------------------------------------------------
@app.route('/builder', methods=['GET', 'POST'])
def builder():
    if 'account' in session:
        account = session['account']
        return render_template('builder.html', account=account, reviewcart=None)
    return redirect(url_for('login'))

@app.route('/get_options/<component>')
def get_options(component):
    # Fetch options for the specified component
    if component in df.components:
        return jsonify(df.components[component])
    else:
        return jsonify([])
    
@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
    if 'account' in session:
        account = session['account']
        if request.method == 'POST':
            itemIDlist = [int(item[1]) for item in request.form.items() if item[1] != 'default']
            itemlist = [df.info_catcher_in_dictionary(item[0],int(item[1])) for item in request.form.items() if item[1] != 'default']
            print(itemIDlist)
            
            reviewcart = True
            return render_template('builder.html', account=account, reviewcart=reviewcart)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

# -----------------------------------------------------------------------------------------ADDITEM.HTML--------------------------------------------------------------------------------
@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            return render_template('additem.html', account=account, admin=admin, table=None)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/cpu', methods=['GET', 'POST'])
def cpu():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'cpu'
            values = ''
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam', 'clock', 'socket'): 
                        values += '"' + value + '",' 
                    else:
                        values += value
                        values += ','  

                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, Clock, Cores, Socket, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/gpu', methods=['GET', 'POST'])
def gpu():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'gpu'
            values = ''
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam', 'clock', 'vramcap', 'gddr'): 
                        values += '"' + value + '",'  
                    else:
                        values += value
                        values += ','  

                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, Clock, VramCap, GDDR, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/ram', methods=['GET', 'POST'])
def ram():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'ram'
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam', 'clock', 'capaciteit'): 
                        values += '"' + value + '",' 
                    else:
                        values += value
                        values += ','  

                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, Clock, Capaciteit, DDR, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/psu', methods=['GET', 'POST'])
def psu():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'psu'
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam'):  
                        values += '"' + value + '",'  
                    else:
                        values += value
                        values += ','  
                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, Watt, TypeID, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/mom', methods=['GET', 'POST'])
def mom():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'moederbord'
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam', 'socket', 'gddr'): 
                        values += '"' + value + '",'  
                    else:
                        values += value
                        values += ','  

                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, Socket, DDR, GDDR, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/storage', methods=['GET', 'POST'])
def storage():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'opslag'
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam', 'capaciteit'):  
                        values += '"' + value + '",'  
                    else:
                        values += value
                        values += ','  

                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, TypeID, Capaciteit, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/additem/case', methods=['GET', 'POST'])
def case():
    if 'account' in session:
        account = session['account']
        if account['isadmin'] == 1:
            admin = True
            table = 'behuizing'
            if request.method == 'POST':
                for key, value in request.form.items(): 
                    if key in ('naam', 'afmetingen'):  
                        values += '"' + value + '",'  
                    else:
                        values += value
                        values += ','  

                if values != '':
                    values = values.rstrip(",")
                    print(values)
                    df.inserDataIntoTable(table, 'Naam, AantalFans, Afmetingen, Stock, Prijs, LeverancierID', values)
                    return render_template('additem.html', account=account, admin=admin, table=None)
            values = ''
            return render_template('additem.html', account=account, admin=admin, table=table)
        else:
            redirect(url_for('login'))
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)
