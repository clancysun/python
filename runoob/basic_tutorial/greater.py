#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: greater.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 00:09:13
############################

# 定义函数
def lcm(x, y):

    # 获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm

# 获取用户输入
num1 = int(input('请输入第一个数字： '))
num2 = int(input('请输入第二个数字： '))

print('{} 和 {} 的最小公倍数为 {}'.format(num1, num2, lcm(num1, num2)))
