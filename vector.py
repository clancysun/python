#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: vector.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-28 23:30:30
############################

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector ({}, {})".format(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
