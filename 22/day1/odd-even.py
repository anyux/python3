#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 9:29
# @Author  : anyux
# @FileName: odd-even.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

i = 0
sum = 0
while i<100:
    if i%2 == 1: #如果为奇数
        sum += i
    else:        #如果为偶数
        sum -= i
    i +=1
print(sum)
