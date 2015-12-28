#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: re_3.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 00:05:14
############################

import re

print(re.search("www", "www.zeroonecloud.com").span())    # 在起始位置匹配
print(re.search("com", "www.zeroonecloud.com").span())    # 不在起始位置匹配
