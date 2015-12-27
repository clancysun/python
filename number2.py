#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: number2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 18:56:36
############################

'''一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。'''

# Python 程序用于检测用户输入的数字是否为质数

# 用户输入数字
num = int(input('请输入一个数字： '))

# 质数大于1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print('{} 不是质数'.format(num))
            print('{0} 乘于 {1} 是 {2}'.format(i, num//i, num))
            break
    else:
        print('{} 是质数'.format(num))

# 如果输入的数字小于或等于 1，不是质数
else:
    print('{} 不是质数'.format(num))
