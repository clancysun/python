#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: parent_child_2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 23:23:13
############################

class Parent:    # 定义父类
    def myMethod(self):
        print("调用父类方法")


class Child(Parent):    # 定义子类
    def myMethod(self):
        print("调用子类方法")


c = Child()    # 子类实例化
c.myMethod()    # 子类调用重写方法
