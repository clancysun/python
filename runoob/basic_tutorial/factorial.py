#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: factorial.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 19:34:31
############################

'''
整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
'''

# 通过用户输入数字计算阶乘

# 获取用户输入的数字
num = int(input('请输入一个数字： '))
factorial = 1

# 查看数字是负数，0 或者正数
if num < 0:
    print('抱歉，负数没有阶乘')
elif num == 0:
    print('0 的阶乘为 1')
else:
    for i in range(1, num + 1):
        factorial *= i
    print('{0} 的阶乘为 {1}'.format(num, factorial))