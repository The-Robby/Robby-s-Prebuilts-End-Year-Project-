from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import storing_password as sp
import data_functions as df

app = Flask(__name__, static_folder="static") #creates a Flask application instance named app
app.secret_key = 'your_secret_key'


# @app.route("/")
# def index():
#     # Sending the index.html file as response
#     return render_template("index.html")

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     print(sp.check_password(sp.get_userID(username),password))

#     # You can return a response or redirect to another page
#     return "Login successful!"

# @app.route("/register")
# def register():
#     return render_template("register.html")

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




# @app.route('/registered', methods=['POST'])
# def registered():
#     if request.method == "POST":
#         new_username = request.form.get("new-username")
#         new_password = request.form.get("new-password")
#         confirm_password = request.form.get("confirm-password")

#         if new_password != confirm_password:
#             return f"Registration successful for user: {new_username}"
#         else:
#             return "Registration failed."

# @app.route("/about")
# def about():
#     # Sending the about.html file as response
#     return render_template("about.html")

# @app.route("/contact")
# def contact():
#     # Sending the contact.html file as response
#     return render_template("contact.html")
cpudata = df.getDataFromTable('cpu')
cpudict = [{'id': i+1, 'name':row[1]} for i, row in enumerate(cpudata)]

components = {
    'cpu': [cpudict],
    'gpu': [{'id': 1, 'name': 'GPU 1'}, {'id': 2, 'name': 'GPU 2'}],
    'ram': [{'id': 1, 'name': 'RAM 1'}, {'id': 2, 'name': 'RAM 2'}]
}

@app.route('/get_options/<component>')
def get_options(component):
    # Fetch options for the specified component
    if component in components:
        return jsonify(components[component])
    else:
        return jsonify([]) 

if __name__ == "__main__":
    app.run(debug=True)


'''
app.run(debug=True) is a method call that starts the Flask development server. Here's a breakdown:

- app: This refers to the Flask application instance that you created earlier using Flask(__name__).
- run(): This is a method provided by the Flask application instance to run the development server.
- debug=True: This is an argument passed to the run() method. When debug is set to True, Flask runs the application in debug mode.
            Debug mode provides helpful features such as interactive debugger and reloader, which automatically restarts the server when you make changes to your code.
'''
