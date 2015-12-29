#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: example_3.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 23:39:52
############################

"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：在10000以内判断，先将该数加上100后再开方，再将该数加上268后再开方，
如果开方后的结果满足条件，即是结果。
"""

import math

for i in range(10000):
    # 转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
        print(i)
