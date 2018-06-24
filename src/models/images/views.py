from flask import Blueprint

images_bp = Blueprint('images', __name__)


@images_bp.route('/')
def gallery():
    pass


@images_bp.route('/upload')
def upload():
    pass


@images_bp.route('/<string:image_id>')
def image_view(image_id):
    pass