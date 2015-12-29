#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: just_counter.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 23:39:30
############################

class JustCounter:
    __secretCount = 0    # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)    # 报错，实例不能访问私有变量
print(counter._JustCounter__secretCount)    # 使用 object._className__attrName 访问属性
