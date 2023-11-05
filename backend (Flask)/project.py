from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.secret_key = "hello"
db = SQLAlchemy(app)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    roll_number = db.Column(db.String(20))
    role = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    # email = db.Column(db.String(100))  # Add the email field

    def __init__(self, name, roll_number, role, gender):  # Include 'email' in the constructor
        self.name = name
        self.roll_number = roll_number
        self.role = role
        self.gender = gender
        # self.email = email  # Initialize the email field


@app.route('/')
def homepage():
    return render_template('registration.html')

# @app.route('/registration', methods=['POST'])
# def registration_form():
#     if request.method == 'POST':
#         name = request.form['name']
#         roll_number = request.form['roll_number']
#         role = request.form['role']
#         phone = request.form['phone']
#         gender = request.form['gender']

#         session["name"] = name
#         session["roll_number"] = roll_number
#         session["role"] = role
#         session["phone"] = phone
#         session["gender"] = gender

#         user_data = UserData(name=name, roll_number=roll_number, role=role, gender=gender)
#         db.session.add(user_data)
#         db.session.commit()
#         flash('Form submitted successfully!')
#         return redirect(url_for('view', values=user_data))

#     return render_template('registration.html')

@app.route('/registration', methods=['POST', "GET"])
def registration_form():
    if request.method == 'POST':
        session.permanent= True
        name = request.form["name"]
        roll_number = request.form["roll_number"]
        role = request.form["role"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        # email = request.form["email"]  # Capture the 'email' input

        session["name"] = name
        session["roll_number"] = roll_number
        session["role"] = role
        session["phone"] = phone
        session["gender"] = gender

        user_data = UserData(name=name, roll_number=roll_number, role=role, gender=gender)
        db.session.add(user_data)
        db.session.commit()
        flash('Form submitted successfully!')

        # Now that the user data is in the database, you can redirect to the 'view' route
        return redirect(url_for('view.html', values=user_data))

    return render_template('registration.html')


@app.route('/view')
def view():
    users = UserData.query.all()
    return redirect(url_for('view.html', values=users))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
