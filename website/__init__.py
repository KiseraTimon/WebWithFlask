from flask import Flask
import random
import string

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

    #Importing blueprints
    from .views import views
    from .auth import auth

    #Registering blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app