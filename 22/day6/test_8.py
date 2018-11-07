#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 9:58
# @Author  : anyux
# @FileName: test_8.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from functools import wraps

def logger(f):
    @wraps(f)
    def inner(*args, **kwargs):
        """
        :param args: 函数名，密码
        :param kwargs: 备用
        :return:  True
        """
        ret = f(*args, **kwargs)
        return ret
    return inner

@logger
def login(username,password):
    """
    此函数是完成登录功能的函数，需要用户名，和密码两个参数，返回True 登陆成功
    :return:  True
    """
    print(666)
    return True
# login(1,2)  #inner()
# # login('alex', 123)
print(login.__doc__)
print(login.__name__)