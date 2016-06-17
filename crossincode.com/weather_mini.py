#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

url=r'http://wthrcdn.etouch.cn/weather_mini?citykey=101210101'
jsonStr = requests.get(url).text

data = json.loads(jsonStr)
weather = data['data']

print('city:', weather['city'])
print('prompt:', weather['ganmao'])
for x in weather['forecast']:
    print(x['date'], x['type'], x['high'],
          x['low'], x['fengxiang'], x['fengli'])
