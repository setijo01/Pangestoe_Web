from flask import Blueprint, request, session, redirect, url_for, render_template

import src.models.users.errors as UserErrors
from src.models.users.user import User

images_bp = Blueprint('images', __name__)


@images_bp.route('/gallery')
def gallery():
    return render_template('images/gallery.jinja2')


@images_bp.route('/<string:user_id>/upload', methods=['GET', 'POST'])
def upload(user_id):
    if session['email'] == User.get_by_id(user_id).email:
        if request.method == 'POST':
            #some upload function
            pass
        return render_template('images/upload.jinja2')
    return render_template('users/login.jinja2')


@images_bp.route('/<string:image_id>')
def image_view(image_id):
    pass