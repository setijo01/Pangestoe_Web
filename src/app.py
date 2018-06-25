from flask import Flask, render_template, request, session, redirect, url_for
from src.common.database import Database
import os
from src.models.users.views import users_bp
from src.models.galleries.views import galleries_bp

app = Flask(__name__)
app.config.from_object('src.config')

app.secret_key = str(os.environ.get('SECRET_KEY'))


@app.before_first_request
def initialize_database():
    Database.initialize()
    session['email'] = None


@app.route('/')
def index():
    return render_template('index.jinja2')


app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(galleries_bp, url_prefix='/galleries')


