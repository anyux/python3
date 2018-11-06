#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/3 15:43
# @Author  : anyux
# @FileName: test_10.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import time
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time
# struct_time=time.gmtime(dif_time)
now_time = time.strftime("%Y-%m-%d %X",time.gmtime(dif_time))
print(now_time)