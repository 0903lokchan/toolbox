from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class ParameterForm(FlaskForm):
    dice = IntegerField('Number of dice', validators=[DataRequired()])
    side = IntegerField('Number of sides of each dice', validators=[DataRequired()])
    target_sum = IntegerField('Target sum of dice result')
    submit = SubmitField('Calculate')