#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: high_low.py

'''
该实例演示了数字猜谜游戏
'''

number = 7
guess = -1
print('Guess the number!')
while guess != number:
    guess = int(input('Is it... '))

    if guess == number:
        print('Hooray! You guessed it right!')
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
