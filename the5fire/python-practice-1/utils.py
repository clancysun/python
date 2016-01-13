#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: utils.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2016-01-14 00:29:48
############################

def line(self):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
