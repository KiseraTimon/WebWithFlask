from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import jsonify


#Defining the file as a blueprint
views = Blueprint('views', __name__)

#Homepage URL
@views.route('/', methods=['GET', 'POST'])
@login_required
def homepage():
    #Fetching data from the input form
    if request.method == 'POST':
        note = request.form.get('note')
        userID = current_user.userID

        #Validating note data length
        if len(note) < 1:
            flash(f'Note is too short!', category='error')
        else:

            #Populating note db fields
            new_note = Note(data = note, userID = userID)

            #Submitting field data to the database
            db.session.add(new_note)
            db.session.commit()

            #Success message
            flash(f'Note added successfully!', category='success')
    return render_template("home.html", user = current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    #Handling JS request to delete note
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)

    #Verify the note exists
    if note:
        #Verify the correct user is deleting the note
        if note.userID == current_user.userID:
            #Delete the note
            db.session.delete(note)
            db.session.commit()

            #Return an empty response
            return jsonify({})