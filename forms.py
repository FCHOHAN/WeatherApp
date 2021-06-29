from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

class PredictForm(FlaskForm):
    apparent_temperature = FloatField('Apparent Temperature', validators=[DataRequired()])
    humidity = FloatField('Humidity', validators=[DataRequired()])
    visibility = FloatField('Visibility', validators=[DataRequired()])
    submit = SubmitField('Predict')