#https://flask.palletsprojects.com/en/3.0.x/quickstart/

from flask import Flask, request, render_template
import storing_password as sp

app = Flask(__name__, static_folder="static") #creates a Flask application instance named app

@app.route("/")
def index():
    # Sending the index.html file as response
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(sp.check_password(sp.get_userID(username),password))

    # You can return a response or redirect to another page
    return "Login successful!"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/registered', methods=['POST'])
def registered():
    if request.method == "POST":
        new_username = request.form.get("new-username")
        new_password = request.form.get("new-password")
        confirm_password = request.form.get("confirm-password")

        if new_password != confirm_password:
            return f"Registration successful for user: {new_username}"
        else:
            return "Registration failed."

@app.route("/about")
def about():
    # Sending the about.html file as response
    return render_template("about.html")

@app.route("/contact")
def contact():
    # Sending the contact.html file as response
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)


'''
app.run(debug=True) is a method call that starts the Flask development server. Here's a breakdown:

- app: This refers to the Flask application instance that you created earlier using Flask(__name__).
- run(): This is a method provided by the Flask application instance to run the development server.
- debug=True: This is an argument passed to the run() method. When debug is set to True, Flask runs the application in debug mode.
            Debug mode provides helpful features such as interactive debugger and reloader, which automatically restarts the server when you make changes to your code.
'''
