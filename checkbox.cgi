#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: checkbox.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 01:31:26
############################

# 引入CGI模块
import cgi, cgitb

# 创建 FieldStorage 实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue("maths"):
    math_flag = "ON"
else:
    math_flag = "OFF"

if form.getvalue("physics"):
    physics_flag = "ON"
else:
    physics_flag = "OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Checkbox - Third CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> CheckBox Maths is: %s</h2>" % math_flag)
print("<h2> CheckBox Physics: %s</h2>" % physics_flag)
print("</body>")
print("</html>")
