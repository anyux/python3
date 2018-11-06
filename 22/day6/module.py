#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 18:41
# @Author  : anyux
# @FileName: module.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

def module():
    print("this is print 666")

import sys
this_module = sys.modules[__name__]
# msg = input(">>>")
msg = 'login'
# print(getattr(this_module,'msg'))
a = getattr(sys.modules[__name__],"msg")
a()

class A:
    role = "admin"
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
