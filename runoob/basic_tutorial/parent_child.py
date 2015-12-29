#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: parent_child.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 21:06:02
############################

class Parent:    # 定义父类
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性: {}".format(Parent.parentAttr))


class Child(Parent):    # 定义子类
    def __init__(self):
        print("调用子类构造函数")

    def childMethod(self):
        print("调用子类方法 child method")


c = Child()    # 实例化子类
c.childMethod()    # 调用子类的方法
c.parentMethod()    # 调用父类的方法
c.setAttr(2000)    # 再次调用父类的方法
c.getAttr()    # 再次调用父类的方法

print("Child is Parent subclass: {}".format(issubclass(Child, Parent)))
print("c is Child instance: {}".format(isinstance(c, Child)))
