#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Author: Quincey Sun
# Mail: zeroonegit@gmail.com
# Created Time: 2016-06-21 23:25:24
###############################################################################

name = 'roger'

x = 0

while x < 3:
    guess = input("What's my name? ")
    if (guess != name):
        print ("Wrong")
        x += 1
        if (x == 3):
            print ("You've reached the max attempt!")
    else:
        print ("Correct")
        break
