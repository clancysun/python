#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author by: One Zero
# Filename: celsius_to_fahrenheit.py


# 用户输入摄氏温度

# 接收用户输入
celsius = float(input('请输入摄氏温度： '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('{0:.1f} 摄氏温度转为华氏温度为 {1:.1f} '.format(celsius, fahrenheit))
