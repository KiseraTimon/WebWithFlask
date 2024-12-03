from flask import Blueprint, render_template

#Defining the file as a blueprint
views = Blueprint('views', __name__)

#Homepage URL
@views.route('/')
def homepage():
    return render_template("home.html")