#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 14:55
# @Author  : anyux
# @FileName: test_03.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from multiprocessing import Process
import os

def func():
    print(123)
    print(os.getpid())
    print(os.getppid())

if __name__ == '__main__':
    p = Process()
    p.start()
    print(456)
    print(os.getpid())
    print(os.getppid())

