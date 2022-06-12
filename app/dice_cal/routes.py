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
    req = request.get_json()
    
    if req is None or req["dice"] is None or req["side"] is None:
        return make_response("Invalid input", 400)
        
    dice_n = int(req["dice"])
    side_n = int(req["side"])
    
    try:
        #TODO API should not return html element string. change it to dict instead
        result = simulate(dice_n, side_n)
        # result_html_list = [f'''<tr>
        #                 <th scope:'row'>{outcome}</th>
        #                 <td>{probability}%</td>
        #             </tr>''' for outcome, probability in result.items()]
        # payload = ''.join(result_html_list)
        return make_response(jsonify({"result": result}), 200)
    
    except TooManyCombinationsError:
        return make_response('The number of possible combination exceeds 10000. Please try with smaller numbers.', 400)
    
    except:
        # catch all error response
        return make_response('The server has encountered an unexpected error.', 500)
    
