#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: re_4.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 00:07:42
############################

import re

line = "Cats are smarter than dogs"

searchObj = re.search(r"(.*) are (.*?) .*", line, re.M|re.I)

if searchObj:
    print("searchObj.group(): {}".format(searchObj.group()))
    print("searchObj.group(1): {}".format(searchObj.group(1)))
    print("searchObj.group(2): {}".format(searchObj.group(2)))
else:
    print("Nothing found!!")
