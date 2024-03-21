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
        password = request.form['password']
        UserID = sp.get_userID(username)
        if sp.check_password(UserID ,password):
            session['account'] = {"username":username, "password":password}
            return redirect(url_for('dashboard'))
        return render_template("login.html", wrongcredentials=True)
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not sp.username_already_exists(username):
            if sp.check_pass_cond(password):
                sp.store_user(username, password)
                session['account'] = {"username":username, "password":password}
                return redirect(url_for('dashboard'))
            else:
                return render_template("login.html", register=True, wrongpass=True)
        else:
            return render_template("login.html", register=True, wrongname=True)


    return render_template("login.html", register=True)

# -----------------------------------------------------------------------------------------DASHBOARD.HTML--------------------------------------------------------------------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'account' in session:
        account = session['account']
        return render_template('dashboard.html', account=account)
    return redirect(url_for('login'))

@app.route('/get_options/<component>')
def get_options(component):
    # Fetch options for the specified component
    if component in df.components:
        return jsonify(df.components[component])
    else:
        return jsonify([]) 



if __name__ == "__main__":
    app.run(debug=True)
