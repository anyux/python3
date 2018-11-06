#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 15:43
# @Author  : anyux
# @FileName: test_06.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from multiprocessing import Process
from multiprocessing import Semaphore
import time
import random

def go_ktv(sem,user):
    sem.acquire()
    print('%s 占到一间ktv小屋'%user)
    time.sleep(random.randint(0,3))
    sem.release()

if __name__ == "__main__":
    sem = Semaphore(4)
    p_l = []
    for i in range(13):
        p = Process(target=go_ktv,args=(sem,'user%s'%i))
        p.start()
        p_l.append(p)
    for i in p_l:
        i.join()
    print('=================================>')