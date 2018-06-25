from flask import Blueprint, request, session, redirect, url_for, render_template

import src.models.users.errors as UserErrors
from src.models.users.user import User

galleries_bp = Blueprint('galleries', __name__)


@galleries_bp.route('/')
def gallery():
    return render_template('galleries/gallery.jinja2')


@galleries_bp.route('/<string:user_id>/upload', methods=['GET', 'POST'])
def upload(user_id):
    if session['email'] == User.get_by_id(user_id).email:
        if request.method == 'POST':
            #some upload function
            pass
        return render_template('galleries/upload.jinja2')
    return render_template('users/login.jinja2')