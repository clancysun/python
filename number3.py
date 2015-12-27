#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: number3.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 19:45:30
############################

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}x{}={}\t'.format(i, j, i * j), end = '')
    print()
