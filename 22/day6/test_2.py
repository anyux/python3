#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 19:48
# @Author  : anyux
# @FileName: test_2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
# 第一步：拿到一个文件夹下所有的文件的绝对路径
import os

def init(func):
    def inner(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return inner
@init
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
@init
def opener():
    while True:
        abs_path = yield
        print("opener func--->",abs_path)

target = opener()
g = search(target)
g.send(r'c:/Users/lenovo/PycharmProjects/22/day6')