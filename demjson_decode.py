#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: demjson_decode.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 16:23:41
############################

import demjson

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = demjson.decode(json)

print(text)
