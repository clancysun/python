#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: file_io.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 00:53:45
############################

# 写文件
with open('/tmp/test.txt', 'wt') as out_file:
    out_file.write('该文本会写入到文件中\n看到我了吧！')

# 读文件
with open('/tmp/test.txt', 'rt') as in_file:
    text = in_file.read()

print(text)
