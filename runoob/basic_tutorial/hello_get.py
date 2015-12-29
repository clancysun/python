#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: hello_get.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 01:27:03
############################

# 引入CGI模块
import cgi, cgitb

# 创建 FieldStorage 实例
form = cgi.FieldStorage()

# 获取表单数据
first_name = form.getvalue("first_name")
last_name = form.getvalue("last_name")
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>" % (first_name, last_name))
print("</body>")
print("</html>")
