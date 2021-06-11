# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:46:21 2021

@author: vinay


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import joblib

loaded_model = joblib.load('power_prediction.sav')

#X = [['Theoretical_Power_Curve (KWh)','WindSpeed(m/s)']]...
print(loaded_model.predict([[416.328907824861,5.31133604049682]])[0],"KWh")

#active value is predicted
