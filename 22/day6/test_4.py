#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/18 12:54
# @Author  : anyux
# @FileName: test_4.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
'''

def test():
    if 1==1:
        name='素还真'
test()
'''
'''
三元表达式
result = 1 if 0 else 2
print(result)
'''
'''
# 对于python，一切事物都是对象，对象是基于类创建
# 包括 字符串类，数字类 ，列表类
# print(dir(int))
# print(help(int))
# print(help(list))
'''
'''
my_list = [11,22,33,44,55,66,77,88,99,90]
my_dict = {'k1':[],"k2":[]}
for i in my_list:
    if i > 66:
        my_dict['k2'].append(i)
    else:
        my_dict['k1'].append(i)
print(my_dict)
'''

from abc import ABCMeta
from abc import abstractclassmethod


class Play(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self): pass

class QQpay(Play):
    def pay(self,money):
        print("QQpay %s 元" %money)

class Alipay(Play):
    def pay(self,money):
        print("Alipay %s 元" %money)

class Wechatpay(Play):
    def pay(self,money):
        print("Wechatpay %s 元" %money)

def player(obj,money):
    obj.pay(money)

a = QQpay()
player(a,100)
