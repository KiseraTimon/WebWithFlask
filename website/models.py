from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#User's model
class User(db.Model, UserMixin):
    #Fields
    userID = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String(50))
    uname = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    #Relationships
    notes = db.relationship('Note')

    # Overriding get_id method for Flask-Login compatibility
    def get_id(self):
        return str(self.userID)

#Notes model
class Note(db.Model):
    #Fields
    noteID = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    #Foreign key fields
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))