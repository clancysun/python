#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: tkinter_demo_2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 22:13:37
############################

from Tkinter import *    # 导入Tkinter库
root = Tk()    # 创建窗口对象的背景色
# 创建两个表
li = ['C', 'Python', 'PHP', 'HTML', 'SQL', 'Java']
movie = ['CSS', 'JQuery', 'Bootstrap']
# 创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:    # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:    # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()    #   将小部件放置到主窗口中
listb2.pack()
root.mainloop()    # 进入消息循环
