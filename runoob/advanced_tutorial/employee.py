#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: employee.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 20:18:40
############################

class Employee:
    """所有员工的基类"""

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee {}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name: {}, Salary: {}".format(self.name, self.salary))


# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000)
# 创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee {}".format(Employee.empCount))

# 添加，修改，删除类的属性
emp1.age = 7    # 添加一个 'age' 属性
emp1.age = 8    # 修改 'age' 属性
del emp1.age    # 删除 'age' 属性

# 用函数的方式来访问属性
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True
setattr(emp1, 'age', 8)    # 添加 'age' 属性的值为 8
getattr(emp1, 'age')    # 返回 'age' 属性的值
delattr(emp1, 'age')    # 删除属性 'age'

# 内置类属性调用
print("Employee.__doc__: {}".format(Employee.__doc__))
print("Employee.__name__: {}".format(Employee.__name__))
print("Employee.__module__: {}".format(Employee.__module__))
print("Employee.__bases__: {}".format(Employee.__bases__))
print("Employee.__dict__: {}".format(Employee.__dict__))
