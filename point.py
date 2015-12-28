#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: point.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 20:57:43
############################

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print("{} 销毁".format(class_name))


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))    # 打印对象的 id
del pt1
del pt2
del pt3
