from flask import Flask, redirect, url_for, request, render_template
from weather import Weather, Unit
import requests
import template

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    ttype = request.form['ttype']
    zip = request.form['zip']
    weather = Weather(unit=Unit.type)
    lookup = weather.lookup('zip')
    condition = lookup.condition
    print(condition.text)
    return render_template('temperature.html',temp=condition.text)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

