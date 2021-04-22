from flask import Blueprint, render_template, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from .models import Note
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note = request.form.get('note')
        title = request.form.get('title')

        if len(title) <3:
            flash('Title is too short!', category='error')
        elif len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(title=title, data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("index.html", user=current_user)
