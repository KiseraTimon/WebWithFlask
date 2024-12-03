from flask import Blueprint

#Defining the file as a blueprint
auth = Blueprint('auth', __name__)

#Login URL
@auth.route('/login')
def login():
    return '<h1>Login</h1>'

#Logout URL
@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

#Signup URL
@auth.route('/signup')
def signup():
    return '<h1>Sign up</h1>'