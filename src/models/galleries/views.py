from flask import Blueprint, request, session, redirect, url_for, render_template

import src.models.users.errors as UserErrors
from src.models.galleries.gallery import Gallery
from src.models.users.user import User

galleries_bp = Blueprint('galleries', __name__)


@galleries_bp.route('/<string:gallery_id>')
def gallery(gallery_id):
    return render_template('galleries/gallery.jinja2', gallery=Gallery.get_by_id(gallery_id))


@galleries_bp.route('/<string:user_id>/upload', methods=['GET', 'POST'])
def upload(user_id):
    if session['email'] == User.get_by_id(user_id).email:
        if request.method == 'POST':
            #some upload function
            pass
        return render_template('galleries/upload.jinja2')
    return render_template('users/login.jinja2')