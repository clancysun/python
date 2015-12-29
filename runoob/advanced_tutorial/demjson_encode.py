#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: demjson_encode.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 16:21:12
############################

import demjson

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json = demjson.encode(data)

print(json)
