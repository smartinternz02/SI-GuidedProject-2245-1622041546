# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:11:49 2021

@author: vinay
"""

import numpy as np
from flask import Flask,request,jsonify,render_template
import joblib
import requests

app = Flask(__name__)
model = joblib.load('power_prediction.sav')

@app.route('/windapi',methods=['POST'])
def windapi():
    city=request.form.get('city')
    apikey="31c8146c2c21db88bcfc138f0ee0798c"
    url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID="+apikey
    resp = requests.get(url)
    resp=resp.json()
    temp = str(resp["main"]["temp"])+" °C"
    humid = str(resp["main"]["humidity"])+" %"
    pressure = str(resp["main"]["pressure"])+" mmHG"
    speed = str(resp["wind"]["speed"])+" m/s"
    return render_template('predict.html', temp=temp, humid=humid, pressure=pressure, speed=speed)

@app.route('/')
def home():
    return render_template('intro.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    for rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    return render_template('predict.html',prediction_text='The Energy Predicted Is {:.2f} kwh'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
    