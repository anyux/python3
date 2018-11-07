#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 20:18
# @Author  : anyux
# @FileName: test_1.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# 第一步：拿到一个文件夹下所有的文件的绝对路径
import os

def search(target): # c:/Users/lenovo/PycharmProjects/22/day6
    while True:
        file_path = yield
        g = os.walk(file_path)
        for pardir,_,files in g:
            for file in files:
                abs_path = r'%s/%s' % (pardir,file)
                # print(abs_path)
                target.send(abs_path)

# 第二步：打开文件拿到文件对象f
def opener():
    while True:
        abs_path = yield
        print("opener func--->",abs_path)

target = opener()
next(target)

g = search(target)
next(g)
g.send(r'c:/Users/lenovo/PycharmProjects/22/day6')
