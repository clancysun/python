#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: save_file.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 02:01:27
############################

import cgi, os
import cgitb; cgitb.enable()

from = cgi.FieldStorage()

# 获取文件名
fileitem = form["filename"]

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径
    fn = os.path.basename(fileitem.filename)
    open("/tmp/" + fn, "wb").write(fileitem.file.read())

    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = "No file was uploaded"

print("""\
      Content-Type: text/html\n
      <html>
      <body>
        <p>%s</p>
      </body>
      </html>
      """ % message)
