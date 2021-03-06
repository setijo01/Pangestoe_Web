from flask import Blueprint, request, session, redirect, url_for, render_template

import src.models.users.errors as UserErrors
from src.models.users.user import User

users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        sha512_password = request.form['hashed']
        try:
            if User.is_login_valid(email, sha512_password):
                session['email'] = email
                return redirect(url_for(".user_page", user_id=User.get_by_email(email)._id))
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/login.jinja2")


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        sha512_password = request.form['hashed']
        try:
            if User.register(email, sha512_password):
                session['email'] = email
                return redirect(url_for(".user_page", user_id=User.get_by_email(email)._id))
        except UserErrors.UserError as e:
            return e.message
    return render_template("users/register.jinja2")


@users_bp.route('/logout')
def logout():
    session['email'] = None


@users_bp.route('/<string:user_id>')
def user_page(user_id):
    return "Welcome, {}".format(user_id)