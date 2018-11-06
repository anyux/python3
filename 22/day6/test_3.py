#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 19:55
# @Author  : anyux
# @FileName: test_3.py
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
def opener(target):
    while True:
        abs_path = yield
        target.send(abs_path)


# 第三步：读取文件
@init
def cat(target):
    abs_path = yield
    while True:
        with open(abs_path,mode='rb') as file_handle:
            for line in file_handle:
                target.send((abs_path,line))


# 第四步：检索匹配字符串
@init
def grep(target,pattern):
    pattern = pattern.encode('utf-8')
    abs_path,line = yield
    while True:
        if pattern in line:
            # abs_path = yield abs_path
            target.send(abs_path)


# 第五步：打印匹配到的文件
@init
def printer():
    while True:
        abs_path = yield
        print("< %s >" % abs_path)


g=search(opener(cat(grep(printer(),'python'))))
g.send(r'c:/Users/lenovo/PycharmProjects/22/day6')


# target = opener()
# g = search(target)
# g.send(r'c:/Users/lenovo/PycharmProjects/22/day6')