#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: fibo.py

# Fibonacci numbers module

def fib(n):             # write Fibonacci series upto n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()

def fib2(n):            # return Fibonacci series to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result
