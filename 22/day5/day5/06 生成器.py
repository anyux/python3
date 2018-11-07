#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 生成器本质就是迭代器，他是自定义的迭代器（自己用python代码写的迭代器）

#1 函数方式的构建一个生成器。
#，生成器表达式。

# def func1():
#     print(111)
#     return 666
# ret = func1()
# print(ret)

# def func1():
#     print(111)
#     yield 666
# g_obj = func1()  # 生成器对象
# # print(g_obj)  # <generator object func1 at 0x0000000001E21E60>
# # 凡事函数中见到yield 他就是生成器
# print(g_obj.__next__())

# def func1():
#     # print(111)
#     yield 666
#     print(222)
#     print(333)
#     yield 'alex'
#     print(888)
# g_obj = func1()  # 生成器对象
# #__next__() 和 yield 必须一一对应
# print(g_obj.__next__())
# print(g_obj.__next__())
# print(g_obj.__next__())

# def cloth():
#     for i in range(1,5001):
#         print('衣服%s' %i)
# cloth()

# def cloth1():
#     for i in range(1,5001):
#         yield  '衣服%s' %i
#
# g_obj = cloth1()  # 生成器对象
#
# for i in range(50):
#     print(g_obj.__next__())
#
# for i in range(150):
#     print(g_obj.__next__())

# send

# def func1():
#     count = yield 666
#     print(count)
#     yield 'alex'
#     yield 'abc'
# g_obj = func1()  # 生成器对象
# print(g_obj.__next__())
# print(g_obj.__next__())
# send 和next 都是对生成器取值。
# send 会给上一个yield 发送一个值。
# send 不能用在第一次取值。
# 最后一个yield 不能得到值
# print(g_obj.send('taibai'))
# print(g_obj.send('taibai'))
# print(g_obj.__next__())