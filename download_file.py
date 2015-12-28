#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: download_file.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 02:11:10
############################

# HTTP头部
print("Content-Disposition: attachment; filename=\"foo.txt\"\r\n\n")

# 打开文件
fo = open("foo.txt", "rb")

str = fo.read()
print(str)

fo.close()
