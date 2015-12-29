#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: re_5.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 00:12:46
############################

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r"dogs", line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group(): ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r"dogs", line, re.M|re.I)
if matchObj:
    print("search --> matchObj.group(): ", matchObj.group())
else:
    print("Nothing found!!")
