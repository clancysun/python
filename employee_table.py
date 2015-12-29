#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: employee_table.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 13:40:31
############################

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TESTDB")

# 使用cursur()方法获取操作游标
cursur = db.cursur()

# 如果数据表已经存在使用execute()方法删表
cursur.execute("DROP TABLE IF EXISTS EMPLOYEE;")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT
)"""

cursur.execute(sql)

# 关闭数据库连接
db.close()
