#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: cookie.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 01:54:42
############################

# Import modules for CGI handling
import cgi, cgitb
from os import environ

if environ.has_key("HTTP_COOKIE"):
    for cookie in map(strip, split(environ["HTTP_COOKIE"], ";")):
        (key, value) = split(cookie, "=")
        if key == "UserID":
            user_id =value

        if key == "Password":
            password = value


print("User ID = %s" % user_id)
print("Password = %s" % password)
