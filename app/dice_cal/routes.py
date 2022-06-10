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

    dice_n = int(req["dice"])
    side_n = int(req["side"])
    result = simulate(dice_n, side_n)
    payload = ''

    if type(result) is dict:
        result_html_list = [f'''<tr>
                        <th scope:'row'>{outcome}</th>
                        <td>{probability}%</td>
                    </tr>''' for outcome, probability in result.items()]
        payload = ''.join(result_html_list)
    elif type(result) is str:
        payload = result
    else:
        # TODO send error response if the app function returns an unexpected result
        return make_response()

    return make_response(jsonify({"text": payload}), 200)
    

