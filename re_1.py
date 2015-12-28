#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: re_1.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 23:52:34
############################

import re
print(re.match("www", "www.zeroonecloud.com").span())    # 在起始位置匹配
print(re.match("com", "www.zeroonecloud.com"))    # 不在起始位置匹配
