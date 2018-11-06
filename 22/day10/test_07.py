#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 15:51
# @Author  : anyux
# @FileName: test_07.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from multiprocessing import Process, Event
import time, random


def car(e, n):
    while True:
        if not e.is_set():  # 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait()    # 阻塞，等待is_set()的值变成True，模拟信号灯为绿色
            print('\033[32m车%s 看见绿灯亮了\033[0m' % n)
            time.sleep(random.randint(3, 6))
            if not e.is_set():   #如果is_set()的值是Flase，也就是红灯，仍然回到while语句开始
                continue
            print('车开远了,car', n)
            break


def police_car(e, n):
    while True:
        if not e.is_set():# 进程刚开启，is_set()的值是Flase，模拟信号灯为红色
            print('\033[31m红灯亮\033[0m，car%s等着' % n)
            e.wait(0.1) # 阻塞，等待设置等待时间，等待0.1s之后没有等到绿灯就闯红灯走了
            if not e.is_set():
                print('\033[33m红灯,警车先走\033[0m，car %s' % n)
            else:
                print('\033[33;46m绿灯，警车走\033[0m，car %s' % n)
        break



def traffic_lights(e, inverval):
    while True:
        time.sleep(inverval)
        if e.is_set():
            print('######', e.is_set())
            e.clear()  # ---->将is_set()的值设置为False
        else:
            e.set()    # ---->将is_set()的值设置为True
            print('***********',e.is_set())


if __name__ == '__main__':
    e = Event()
    for i in range(10):
        p=Process(target=car,args=(e,i,))  # 创建是个进程控制10辆车
        p.start()

    for i in range(5):
        p = Process(target=police_car, args=(e, i,))  # 创建5个进程控制5辆警车
        p.start()
    t = Process(target=traffic_lights, args=(e, 10))  # 创建一个进程控制红绿灯
    t.start()

    print('============》')


