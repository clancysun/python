#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: number.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 18:05:25
############################

# 判断奇数偶数
# 如果偶数除于 2 余数为 0
# 如果余数为 1 则为奇数

print('这是一个判断奇数偶数的程序.')
num = int(input('请输入一个数字： '))
if (num % 2) == 0:
    print('{} 是偶数'.format(num))
else:
    print('{} 是奇数'.format(num))
