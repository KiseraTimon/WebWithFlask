from flask import Blueprint

#Defining the file as a blueprint
views = Blueprint('views', __name__)

#Homepage URL
@views.route('/')
def homepage():
    return '<h1>Home page</h1>'