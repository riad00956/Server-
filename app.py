from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# ✅ Secure Secret Key
app.secret_key = '9a8a76f4c33e443fab7b4d36f73edb9d2e9f181bc3f207eef1012deed15e8bd1'

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
            return "Invalid login"
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
