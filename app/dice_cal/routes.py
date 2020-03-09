from flask import render_template, request, render_template, url_for, jsonify, make_response
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
    req = request.get_json()

    print(req)

    dice = int(req["dice"])
    side = int(req["side"])
    result = simulate(dice, side)

    res = make_response(jsonify({"text": result}), 200)
    return res

