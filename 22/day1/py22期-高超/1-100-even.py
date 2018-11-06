#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 9:27
# @Author  : anyux
# @FileName: 1-100-even.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

i = 0
while i<101:
    if i%2 == 0: #如果为偶数
        print(i)
        i +=2
    else:        #如果为奇数
        i +=1