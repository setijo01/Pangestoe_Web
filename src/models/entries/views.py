from flask import Blueprint

entries_bp = Blueprint('entries', __name__)


@entries_bp.route('/')
def blog_list():
    pass


@entries_bp.route('/create_new')
def create_new():
    pass


@entries_bp.route('/<string:entry_id>')
def entry_view(entry_id):
    pass
