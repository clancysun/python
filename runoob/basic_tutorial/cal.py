#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: cal.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 00:36:38
############################

# 引入日历模块
import calendar

# 输入指定年月
yy = int(input('请输入年份： '))
mm = int(input('请输入月份： '))

# 显示日历
print(calendar.month(yy, mm))
