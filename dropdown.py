#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: dropdown.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 01:38:42
############################

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue("dropdown"):
    subject = form.getvalue("dropdown")
else:
    subject = "Not entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Dropdown Box - Sixth CGI Program</title>")
print("</head>")
print("<body>")
print("<h2> Selected Subject is: %s</h2>" % subject)
print("</body>")
print("</html>")
