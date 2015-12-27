#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: if.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 17:43:03
############################

# 用户输入数字

num = float(input('输入一个数字： '))
if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')
