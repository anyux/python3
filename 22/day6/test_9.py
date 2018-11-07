#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 7:33
# @Author  : anyux
# @FileName: test_9.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
def wrapper1(func):  # func = f函数名
    def inner1():
        print('wrapper1 ,before func')  # 2
        func()  # f函数名()
        print('wrapper1 ,after func')  # 4
    return inner1

def wrapper2(func):  # func = inner1
    def inner2():
        print('wrapper2 ,before func')  # 1
        func()  # inner1()
        print('wrapper2 ,after func')  # 5
    return inner2

def wrapper3(func):
    def inner3():
        print('wrapper3 ,before func')
        func()
        print('wrapper3 ,after func')
    return inner3

@wrapper3
@wrapper2  # f = warpper2(f)  里面的f是inner1 外面的f是inner2
@wrapper1  # f = warpper1(f)  里面的f函数名 外面的f 是inner1
def f():
    print('in f')  # 3

f()  # inner2()

# wrapper2 ,before func
