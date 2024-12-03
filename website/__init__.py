from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import string
from os import path
from flask_login import LoginManager

#Initializing Database Connection
db = SQLAlchemy()
DB_NAME = "database.db"

#Initializing Flask
def create_app():
    app = Flask(__name__)
    
    #Flask random key to encrypt data
    def random_key(length = 16):
        char = string.ascii_letters + string.digits
        randkey = ''.join(random.choices(char, k=length))
        return randkey

    #Configuring random key
    key = random_key()
    app.config['SECRET_KEY'] = key

    #Configuring database connection
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #Importing blueprints
    from .views import views
    from .auth import auth

    #Registering blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #Implementing database
    from .models import User, Note

    #User session management
    loginmanager = LoginManager()
    loginmanager.login_view = 'auth.login'
    loginmanager.init_app(app)

    @loginmanager.user_loader
    def load_user(userID):
        return User.query.get(int(userID))

    return app

#Database creation
def create_database(app):
    if not path.exists('website/ '+DB_NAME):
        db.create_all()
        print('Created Database!')