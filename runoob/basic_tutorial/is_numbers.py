#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: is_numbers.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-27 17:51:25
############################

def is_numbers(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 测试字符串和数字
print(is_numbers('foo'))            # False
print(is_numbers('1'))              # True
print(is_numbers('1.3'))            # True
print(is_numbers('-1.37'))          # True
print(is_numbers('1e3'))            # True

# 测试 Unicode
# 阿拉伯语 5
print(is_numbers('٥'))              # True
# 中文数字
print(is_numbers('四'))             # True
# 版权号
print(is_numbers('©'))              # False

