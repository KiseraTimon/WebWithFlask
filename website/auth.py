from flask import Blueprint, render_template, request, flash

#Defining the file as a blueprint
auth = Blueprint('auth', __name__)

#Login URL
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

#Logout URL
@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

#Signup URL
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    #Fetching form data
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        uname = request.form.get('uname')
        email = request.form.get('email')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')

    return render_template("signup.html")