#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: re_2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 23:57:12
############################

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r"(.*) are (.*?) .*", line, re.M|re.I)

if matchObj:
    print("matchObj.group(): {}".format(matchObj.group()))
    print("matchObj.group(1): {}".format(matchObj.group(1)))
    print("matchObj.group(2): {}".format(matchObj.group(2)))
else:
    print("No match!!")
