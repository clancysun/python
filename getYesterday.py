#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: getYesterday.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 01:26:19
############################

# 引入 datetime 模块
import datetime

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    return yesterday

# 输出
print(getYesterday())
