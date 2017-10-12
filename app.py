'''
Shannon Lau and Tiffany Moi
SoftDev1 Period 7
HW #08: Do I Know You?
2017-10-6
'''

from flask import Flask, render_template, redirect, url_for, session, request, flash
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
        return render_template('login.html')

# Render login page (with error) or redirect to welcome page
@app.route('/login', methods=["GET","POST"])
def login():
    # Diagnostic print statements
    testing()
    inputs = request.form
    uname = inputs['uname']
    password = inputs['password']
    # Check for existing username
    if uname not in ACCOUNTS:
        flash('Incorrect username.')
        return render_template('login.html')
    # Check for valid password
    if ACCOUNTS[uname] != password:
        flash('Incorrect password.')
        return render_template('login.html')
    # Add username data to session
    session['uname'] = uname
    # Redirect to welcome page
    return redirect(url_for('welcome'))

# Render welcome page
@app.route('/welcome')
def welcome():
    try:
        #If someone is logged in, go to welcome page
        # Note: in the template, the variable for username is 'username'
        uname = session['uname']
        flash('You have successfully logged in!')
        return render_template('welcome.html', username = uname)
    except:
        #If not, go back to login
        flash( 'Whoops! You forgot to log in!')
        return render_template('login.html')
        
# Log out procedure
@app.route('/logout', methods=["GET","POST"])
def logout():
    # Remove username data from session
    if 'uname' in session:
        session.pop('uname')
    flash("You have successfully logged out!")
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
