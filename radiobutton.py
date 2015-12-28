#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: radiobutton.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 01:38:42
############################

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue("subject"):
    subject = form.getvalue("subject")
else:
    subject = "Not set"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Radio - Fourth CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> Selected Subject is: %s</h2>" % subject)
print("</body>")
print("</html>")
