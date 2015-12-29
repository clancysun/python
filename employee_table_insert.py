#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: employee_table_insert.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 13:58:24
############################

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# 关闭数据库连接
db.close()
