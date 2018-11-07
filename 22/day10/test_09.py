#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 9:13
# @Author  : anyux
# @FileName: test_09.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from multiprocessing import Pipe
from multiprocessing import Process

def func(conn1):
    while True:
        msg = conn1.recv()
        if msg == None:
            break
        else:
            print(msg)

if __name__ == '__main__':
    conn1,conn2=Pipe()
    Process(target=func,args=(conn1,)).start()
    conn1.close()
    for i in range(20):
        conn2.send('吃了么')
    conn2.send(None)
    conn2.close()