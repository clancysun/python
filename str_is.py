#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: str_is.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 00:59:48
############################

# 测试实例一
print('测试实例一')
str = 'zeroonegit@gmail.com'
print(str.isalnum())                    # 判断所有字符都是数字或者字母
print(str.isalpha())                    # 判断所有字符都是字母
print(str.isdigit())                    # 判断所有字符都是数字
print(str.islower())                    # 判断所有字符都是小写
print(str.isupper())                    # 判断所有字符都是大写
print(str.istitle())                    # 判断所有单词都是首字母大写，像标题
print(str.isspace())                    # 判断所有字符都是空白字符、\t、\n、\r

print('---------------------------------')

# 测试实例二
print('测试实例二')
str = 'zeroonegit'
print(str.isalnum())                    # 判断所有字符都是数字或者字母
print(str.isalpha())                    # 判断所有字符都是字母
print(str.isdigit())                    # 判断所有字符都是数字
print(str.islower())                    # 判断所有字符都是小写
print(str.isupper())                    # 判断所有字符都是大写
print(str.istitle())                    # 判断所有单词都是首字母大写，像标题
print(str.isspace())                    # 判断所有字符都是空白字符、\t、\n、\r
