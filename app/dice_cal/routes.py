from flask import render_template, request, render_template, url_for, jsonify, make_response
from flask import current_app

from app.dice_cal import bp
from app.dice_cal.forms import ParameterForm
from app.dice_cal.main import TooManyCombinationsError, simulate

@bp.route('/dice_cal', methods=['GET', 'POST'])
def main():
    form = ParameterForm()
    return render_template('dice_cal/main.html', title='Home', form=form)

@bp.route('/dice_cal/cal_sim', methods=['POST'])
def cal_sim():
    try:
        req = request.get_json()
    
        if req is None or req["dice"] == '' or req["side"] == '':
            return make_response(jsonify({"response_text": 'Invalid input'}), 400)
            
        dice_n = int(req["dice"])
        side_n = int(req["side"])
        result = simulate(dice_n, side_n)
        return make_response(jsonify({"result": result}), 200)
    
    except TooManyCombinationsError:
        return make_response(jsonify({"response_text": 'The number of possible combination exceeds 10000. Please try with smaller numbers.'}), 400)
    
    except:
        # catch all error response
        return make_response(jsonify({"response_text": 'The server has encountered an unexpected error.'}), 500)
    
