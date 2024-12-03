from flask import Blueprint, render_template
from flask_login import login_required, current_user


#Defining the file as a blueprint
views = Blueprint('views', __name__)

#Homepage URL
@views.route('/')
@login_required
def homepage():
    return render_template("home.html")