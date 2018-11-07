#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 15:00
# @Author  : anyux
# @FileName: test_05.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import json
import time
import random
from multiprocessing import Process

def buy_ticket(i):
    # 模拟网络延迟
    time.sleep(random.randint(1,3))
    # 打开文件
    with open('ticket') as f:
        dict = json.load(f)
    if dict['ticket'] >0:
        dict["ticket"]-=1
    # 模拟网络延迟
        time.sleep(random.randint(1,3))
        print('%s你已抢到票了'%i)
    else:
        # 模拟网络延迟
        time.sleep(random.randint(1,3))
        print('没票啦,%s你没抢到票'%i)
    with open("ticket","w") as f:
        json.dump(dict,f)

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=buy_ticket,args=(i,))
        p.start()
