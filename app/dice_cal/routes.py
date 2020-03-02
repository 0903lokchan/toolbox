from flask import render_template, request, render_template, url_for
from flask import current_app

from app.dice_cal import bp

@bp.route('/dice_cal')
def main():
    return render_template('dice_cal/main.html', title='Home')


