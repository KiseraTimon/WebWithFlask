from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

#Defining the file as a blueprint
auth = Blueprint('auth', __name__)

#Login URL
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #Fetching form data
    if request.method == 'POST':
        uname =  request.form.get('uname')
        password = request.form.get('password')

        #Validate if the account exists
        user = User.query.filter_by(uname = uname).first()
        if user:
            #Validate password
            if check_password_hash(user.password, password):
                flash(f'Login successfull', category='success')
                return redirect(url_for('views.homepage'))
            else:
                flash(f'Incorrect password', category='error')
        else:
            flash(f'Username does not exist', category='error')


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

        #Validate if similar account exists
        user = User.query.filter((User.email == email) | (User.uname == uname)).first()

        #condition checking
        if user:
            flash('Username or email already exists', category='error')
        elif len(fname) < 1:
            flash(f'First name length must be greater than 3', category='error')
        elif len(lname) < 1:
            flash(f'Last name length must be greater than 3', category='error')
        elif len(uname) < 4:
            flash(f'Username length must be greater than 3', category='error')
        elif len(email) < 4:
            flash(f'Email length must be greater than 3', category='error')
        elif (len(pass1) and len(pass2)) < 7:
            flash(f'Passwords must be at least 7 characters', category='error')
        elif pass1 != pass2:
            flash(f'Passwords do not match', category='error')
        else:
            #Populating database with input details
            new_user = User(fname=fname, lname=lname, uname=uname, email=email, password=generate_password_hash(pass1))
            
            #Pushing to the database
            db.session.add(new_user)
            db.session.commit()
        
            #Output message
            flash(f'Account created successfully', category='success')

            return redirect(url_for('views.homepage'))

    return render_template("signup.html")