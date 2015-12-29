#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: database_version.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 13:32:56
############################

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION();")

# 使用fetchone()方法获取一条数据库
data = cursor.fetchone()

print("Database version: %s" % data)

# 关闭数据库连接
db.close()
