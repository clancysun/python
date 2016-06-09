# -*- coding: utf-8 -*-
import urllib2
import json
from city import city

cityname = raw_input('你想查哪个城市的天气？\n')
citycode = city.get(cityname)
if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content = urllib2.urlopen(url).read()
    print content
