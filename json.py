# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 20:53:29 2019

@author: Penny
"""

import json

with open('weather_data/20190130.json', encoding = 'utf-8') as f:
    line = f.readline()
    d = json.loads(line)
    print(d)
    f.close()

tuple(d.keys())
tuple(d.values())
tuple(d.items())

province = input("请输入省份")
city = input("请输入城市")
d.get('china/'+province+'/'+city)


