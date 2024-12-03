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

        #condition checking
        if len(fname) < 1:
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
            flash(f'Account created successfully', category='success')

    return render_template("signup.html")