#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: fibo2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 19:57:55
############################

'''
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
'''

# Python 斐波那契数列实现

# 获取用户输入数据
netrms = int(input('你需要几项？ '))

# 第一项和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if netrms < 0:
    print('请输入一个正数。')
elif netrms == 1:
    print('斐波那契数列： ')
    print(n1)
else:
    print('斐波那契数列： ')
    print('{}, {}'.format(n1, n2), end = ', ')
    while count < netrms:
        nth = n1 + n2
        print(nth, end = ', ')
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
