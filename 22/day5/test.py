#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 9:39
# @Author  : anyux
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

def winner(f):
    def inner(*args,**kwargs):
        print('222')
        res = f(*args,**kwargs)
        print('333')
        return res
    return inner

@winner # func1 = winner(func1)
def func1(a,b):
    print(a,b)
func1('a','b')
