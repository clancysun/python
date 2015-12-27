#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: cal2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 01:18:45
############################

# 计算每个月天数
import calendar

yy = int(input('请输入年份： '))
mm = int(input('请输入月份： '))
monthRange = calendar.monthrange(yy, mm)
print(monthRange)
