#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 9:30
# @Author  : anyux
# @FileName: test_01.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from multiprocessing import Process
import os

class MyProcess(Process):
    def run(self):
        print(os.getpid())

if __name__ == '__main__':
    print("当前进程：",os.getpid())
    p1 = MyProcess()
    p1.start()
    p2 = MyProcess()
    p2.start()
