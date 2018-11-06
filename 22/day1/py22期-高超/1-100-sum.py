#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 9:02
# @Author  : anyux
# @FileName: 1-100-sum.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

sum = 0
i = 1   #累加器初始值 1
while i < 100 :
    sum += i
    i +=1 #累加器自增1
print(sum) # 4950
