#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 14:36
# @Author  : anyux
# @FileName: test_04.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import json
import time
from multiprocessing import Process
from multiprocessing import Lock

'''
# 显示剩余票数
def show(i):
    with open('ticket') as f:
        dict = json.load(f)
    print('余票:%s'%dict['ticket'])
'''

def buy_ticket(i,lock):
    #拿钥匙进入
    lock.acquire()
    with open('ticket') as f:
        dict = json.load(f)
        time.sleep(0.1)
    if dict['ticket'] > 0:
        dict['ticket']=0
        print('\033[32m%s买到票了\033[0m'%i)
    else:
        print('\033[31m%s没买到票\033[0m'%i)
    time.sleep(0.1)
    with open('ticket','w') as f:
        json.dump(dict,f)
    #还钥匙
    lock.release()

if __name__ == '__main__':
    '''
    for i in range(11):
        # 创建进程实例
        p = Process(target=show,args=(i,))
        # 开启进程
        p.start()
    '''
    lock = Lock()
    for i in range(10):
        p = Process(target=buy_ticket,args=(i,lock))
        p.start()
