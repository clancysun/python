#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: view.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2016-01-01 22:41:58
############################

from django.http import HttpResponse

def hello(requst):
    return HttpResponse("Hello world!")
