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

    key = random_key()

    #Configure random key
    app.config['SECRET_KEY'] = key
    return app