#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: re_6.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 00:18:34
############################

import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r"#.*$", "", phone)
print("Phone Num: {}".format(num))

# Remove anything other than digits
num = re.sub(r"\D", "", phone)
print("Phone Num: {}".format(num))
