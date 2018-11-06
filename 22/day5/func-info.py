#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 10:42
# @Author  : anyux
# @FileName: func-info.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from functools import wraps
import time
def time_outer(flag):
        def outer(f):
            @wraps(f)
            def inner(*args,**kwargs):
                if flag:
                    start_time = time.time()
                    ret = f(*args,**kwargs)
                    dif_time = time.time()-start_time
                    print("函数执行时间为 %s " % dif_time)
                    return ret
                else:
                    ret = f(*args,**kwargs)
                    return ret
            return inner
        return outer

flag = False
# flag = True
@time_outer(flag) #1.将@与函数time_outer()分开 time_outer(flag) 返回outer 2.将@outer结合 执行装饰器，与之前一样
def login(username,passwd):
    '''
    :param username:
    :param passwd:
    :return:
    '''
    print('%s 的密码是 %s' % (username,passwd))
    return False

login('素还真','叶小钗')
# print(login.__doc__)
# print(login.__name__)
# print(login.__globals__)
# print(login.__file__)
