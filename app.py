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
app.secret_key = os.urandom(32)

ACCOUNTS = {'tiff':'coder', 'shanlau':'baller'}

# Landing page
@app.route("/")
def root():
    # If not logged out, redirect to welcome page
    # Else, render login page
    if 'uname' in session.keys():
        return redirect(url_for('welcome'))
    else:
        return render_template('login.html', message = "")

# Render login page (with error) or redirect to welcome page
@app.route('/login', methods=["GET","POST"])
def login():
    # Diagnostic print statements
    testing()
    inputs = request.args
    uname = inputs['uname']
    password = inputs['password']
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
@app.route('/logout', methods=["GET","POST"])
def logout():
    # Remove username data from session
    if 'uname' in session:
        session.pop('uname')
    return redirect(url_for('root'))

# Checking methods and inputs
def testing():
    print "\n\n\n\n"
    print "_________TESTING LOGIN INPUTS__________"
    print "Print app:"
    print app
    print "Print request.method:"
    print request.method
    if request.method == "GET":
        print "Print request.args:"
        print request.args
    else:
        print "Print request.form:"
        print request.form


if __name__ == "__main__":
    app.debug = True
    app.run()
