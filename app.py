from flask import Flask, render_template,  redirect
from config import Config
from forms import PredictForm

app = Flask(__name__)
app.config.from_object(Config)

from joblib import dump, load
linear_reg2 = load('weather_model.joblib') 

'''
@app.route('/')
def hello():
    return 'Hello, World2!'

@app.route('/apparent_temperature/<app_temp_value>/humidity/<humidity_value>/visibility/<visibility_value>/')
def show_temperature(app_temp_value, humidity_value, visibility_value):
	x = [[float(app_temp_value), float(humidity_value), float(visibility_value)]]
	ypred = linear_reg2.predict(x)
	
	return 'The data given is ' + str(x) + '\nThe predicted temperature is ' + str(ypred)
'''
@app.route('/', methods=['GET', 'POST'])
def predict():
	form = PredictForm()
	if form.validate_on_submit():
		x = [[form.apparent_temperature.data, form.humidity.data, form.visibility.data]]
		ypred = round(linear_reg2.predict(x)[0,0],2)
		return render_template('predict_form.html', form=form, prediction=ypred)
	return render_template('predict_form.html', form=form)