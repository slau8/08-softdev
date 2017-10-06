'''
Shannon Lau and Tiffany Moi
SoftDev1 Period 7
HW #08: Do I Know You?
2017-10-6
'''

from flask import Flask, render_template, redirect, url_for, session, request
import os

# Create flask app and establish secret_key
app = Flask(__name__)

#encrypts cookie values
app.secret_key = os.urandom(32)

ACCOUNTS = {'tiff':'coder', 'shanlau':'baller'}

# Landing page
@app.route("/")
def hello_world():
    # If not logged out, redirect to welcome page
    # Else, render login page
    if 'uname' in session.keys():
        return redirect(url_for('welcome'))
    else:
        return render_template('login.html', message = "")

# Render login page (with error) or redirect to welcome page
@app.route('/login')
def login():
    form_dict = request.args
    uname = form_dict['uname']
    password = form_dict['password']
    # Check for existing username
    if uname not in ACCOUNTS:
        return render_template('login.html', message = 'Incorrect username.')
    # Check for valid password
    if ACCOUNTS[uname] != password:
        return render_template('login.html', message = 'Incorrect password.')
    # Add username data to session
    session['uname'] = uname
    # INSERT CODE HERE TO REDIRECT WELCOME


# Render welcome page
@app.route('/welcome')
def welcome():
    uname = session['uname']
    # INSERT CODE HERE TO RENDER TEMPLATE
    # Note: in the template, the variable for username is 'username'

# Log out procedure
@app.route('/logout')
def logout():
    # Remove username data from session
    if 'uname' in session:
        session.pop('uname')
    return redirect(url_for('hello_world'))

if __name__ == "__main__":
    app.debug = True
    app.run()
