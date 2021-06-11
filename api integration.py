# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:46:22 2021

@author: vinay
"""
import requests
apikey = "31c8146c2c21db88bcfc138f0ee0798c"
resp = requests.get("http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID="+apikey)
print(resp.json())
resp=resp.json()
temp = resp["main"]["temp"]
humid = resp["main"]["humidity"]
pressure = resp["main"]["pressure"]
humid = resp["wind"]["speed"]
print(temp,humid,pressure,humid)