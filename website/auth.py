from flask import Blueprint, render_template

#Defining the file as a blueprint
auth = Blueprint('auth', __name__)

#Login URL
@auth.route('/login')
def login():
    return render_template("login.html")

#Logout URL
@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

#Signup URL
@auth.route('/signup')
def signup():
    return render_template("signup.html")