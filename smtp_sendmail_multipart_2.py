#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: smtp_sendmail_multipart_2.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 15:54:55
############################

import smtplib
import base64

filename = "/tmp/text.txt"

# 读取文件内容并使用base64编码
fo = open(filename, 'rb')
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)    # base64

sender = 'webmaster@tutorialpoint.com'
reciever = 'amrood.admin@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send  an attachement.
"""

# 定义头部信息
part1 = """
From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# 定义消息动作昌
part2 = """
Content-Type: text/plain
Content-Transfer-Encoding: 8bit

%s
--%s
""" % (body, marker)

# 定义附近部分
part3 = """
Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding: base64
Content-Disposition: attachement; filename=%s

%s
--%s--
""" % (filename, filename, encodedcontent, marker)

message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, reciever, message)
    print("Successfully sent email")
except Exception:
    print("Error: unable to send email")
