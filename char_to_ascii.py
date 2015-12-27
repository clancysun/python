#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: char_to_ascii.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 21:12:02
############################

# 用户输入字符
c = input('请输入一个字符： ')

# 用户输入ASCII码，并将输入的数字转为整型
a = int(input('请输入一个ASCII码： '))

print(c + ' 的ASCII码为： ', ord(c))
print(a, ' 对应的字符为： ', chr(a))
