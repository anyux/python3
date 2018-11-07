#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 12:44
# @Author  : anyux
# @FileName: test2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

def func_1():
    import os
    name = '素还真'
    var = locals()
    print(var)
# func_1()
from urllib.request import urlopen
def index():
    url = "http://www.xiaohua100.cn/index.html"
    def get():
        return urlopen(url).read()
    return get
xiaohua = index()
content = xiaohua()
print(content)
