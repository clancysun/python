#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################
# File Name: employee_table_select.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 14:10:10
############################

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = """SELECT * FROM EMPLOYEE
WHERE INCOME > 1000"""

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % \
             (fname, lname, age, sex, income))
except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
