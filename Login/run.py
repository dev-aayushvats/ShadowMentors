import sqlite3
from flask import Flask, render_template, request, jsonify, g

app = Flask(__name__)
app.config['DATABASE'] = 'mydatabase.db'  # Name of your SQLite database file

# Function to establish a connection to the database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
    return g.db

# Function to close the database connection when the request is finished
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

# Create a table for users in the SQLite database
with app.app_context():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students ( username TEXT PRIMARY KEY, email TEXT, password TEXT, no_of_projects INTEGER, xp INTEGER )''')
    db.commit()

@app.route('/home')
@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form('username')
    password = request.form('password')

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user and user[2] == password:  # Assuming email is in column 1 and password is in column 2 of your users table
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"})

@app.route('/signup', methods=['POST','GET'])
def signup():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        return jsonify({"error": "username already in use"})
    else:
        cursor.execute("INSERT INTO students (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        db.commit()
        return jsonify({"message": "Signup successful"})

@app.route('/reset_password', methods=['POST'])
def reset_password():
    username = request.form.get('username')

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        # Implement password reset logic here (send email with reset link, etc.)
        return jsonify({"message": "Password reset instructions sent to your email"})
    else:
        return jsonify({"error": "Email not found"})

if __name__ == '__main__':
    app.run(debug=True)
