from flask import Blueprint

bp = Blueprint('post_wall', __name__)

from app.post_wall import routes, forms