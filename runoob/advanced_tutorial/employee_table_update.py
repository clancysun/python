#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: employee_table_update.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 14:28:36
############################

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 更新语句
sql = """UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
