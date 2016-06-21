#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# Author: Quincey Sun
# Mail: zeroonegit@gmail.com
# Created Time: 2016-06-21 23:14:26
###############################################################################

## This programs asks a user for a name and a password.
# It then checks them to make sure that the user is allowed in .
# Note that this is a simple and insecure example,
# real password code should never be implemented this way.

name = input("What is your name? ")
password = input("What is the password? ")
if name == "Josh" and password == "Friday":
    print ("Welcome Josh")
elif name == "Fred" and password == "Rock":
    print ("Welcome Fred")
else:
    print ("I don't know you.")
