from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'a3b584f07e08b9e5f48924fd1da00bc5760111806f51724ffccdf72b570ad2aa'  # Secure secret key

# Dummy admin login
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Login"
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    if 'admin' in session:
        return render_template("dashboard.html")
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
