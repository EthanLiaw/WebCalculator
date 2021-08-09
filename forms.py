from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import Input

class CalculatorForm(FlaskForm):
    input1 = DecimalField('Input 1', places=10, validators=[DataRequired()])
    input2 = DecimalField('Input 2', places=10, validators=[DataRequired()])
    operator = StringField('Operator',validators=[DataRequired()])
    submit = SubmitField('Execute')
