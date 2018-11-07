#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 11:08
# @Author  : anyux
# @FileName: test_10.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import os
import time
from multiprocessing import Pool

def func(n):
    print('start fun%s'%n,os.getpid())
    time.sleep(1)
    print('end fun%s'%n,os.getpid())

if __name__ == "__main__":
    p = Pool(5)
    for i in range(6):
        p.apply_async(func,args=(i,))
    p.close()
    p.join()
