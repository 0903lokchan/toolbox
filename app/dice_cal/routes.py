from flask import render_template, request, render_template, url_for, jsonify
from flask import current_app

from app.dice_cal import bp
from app.dice_cal.forms import ParameterForm
from app.dice_cal.main import simulate

@bp.route('/dice_cal', methods=['GET', 'POST'])
def main():
    form = ParameterForm()
    return render_template('dice_cal/main.html', title='Home', form=form)

@bp.route('/dice_cal/cal_sim', methods=['POST'])
def cal_sim():
    form = ParameterForm()
    if form.validate_on_submit():
        return jsonify(simulate(form.dice.data, form.side.data, form.target_sum.data))
    return jsonify(form.errors)

