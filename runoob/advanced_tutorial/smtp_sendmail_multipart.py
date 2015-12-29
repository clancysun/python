#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: smtp_sendmail_multipart.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 15:37:28
############################

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# 创建一个带附件的实例
msg = MIMEMultipart()

# 构造附件1
att1 = MIMEText(open('/tmp/123.rar', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = "application/octet-stream"
att1["Content-Disposition"] = "attachment; filename='123.doc'"    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

# 构造附件2
att2 = MIMEText(open('/tmp/123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = "application/octet-stream"
att2["Content-Disposition"] = "attachment; filename='123.txt'"    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att2)

# 加邮件头
msg['to'] = 'YYY@YYY.com'
msg['from'] = 'XXX@XXX.com'
msg['subject'] = 'hello world'

# 发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.XXX.com')
    server.login('XXX', 'XXXXXX')    # XXX为用户名， XXXXXX为密码
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()
    print("发送成功")
except Exception as e:
    print(str(e))
