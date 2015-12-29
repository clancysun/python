#!/usr/bin/env python3
# -*- coding: utf-8 -*-
############################
# File Name: xml_3.py
# Author: One Zero
# Mail: zeroonegit@gmail.com
# Created Time: 2015-12-29 21:24:55
############################

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开XML文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element: %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))

    type = movie.getElementByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)
    format = movie.getElementByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)



