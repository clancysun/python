#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: employee_table_delete.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 14:42:19
############################

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL删除记录语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 向数据库提交
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
