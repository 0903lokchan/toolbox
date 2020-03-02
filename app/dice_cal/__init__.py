from flask import Blueprint

bp = Blueprint('dice_cal', __name__)

from app.dice_cal import main, routes