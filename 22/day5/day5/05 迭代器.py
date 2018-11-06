#!/usr/bin/env python
# -*- coding:utf-8 -*-

# s1 = 'asvdcsdgfds'
# for i in s1:
#     print(i)
# l2 = [1, 2, 3]
# for i in l2:
#     print(i)

# i1 = 123  # 不可迭代 'int' object is not iterable
# for i in i1:
#     print(i)

#  str, list tuple dict set range 文件句柄
# 该对象中，含有__iter__方法的就是可迭代对象，遵循可迭代协议。
# print(dir(str))
# 第一种方法：
# 1,判断该对象是不是可迭代对象  '__iter__' in dir(对象)
# print('__iter__' in dir(str))
# print('__iter__' in dir(list))

# 2,判断该对象是不是可迭代对象  isinstance('abc',Iterable)
from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance('abc',str))

# 迭代器 内部含有__iter__ 且含有__next__方法的对象就是迭代器，遵循迭代器协议。
# with open('01 今日内容大纲',encoding='utf-8') as f1:
#     print(f1)  # <_io.TextIOWrapper name='01 今日内容大纲' mode='r' encoding='utf-8'>
s1 = 'abc'
# obj_s = s1.__iter__()  # 可迭代对象转化成迭代器
# obj_s = iter(s1)  # 可迭代对象转化成迭代器
# print(obj_s)  # <str_iterator object at 0x0000000001F4A128>
# print(obj_s.__next__())
# print(obj_s.__next__())
# print(obj_s.__next__())
# print(obj_s.__next__())

# 第一种方法：
# 1,判断该对象是不是迭代器
# s1 = 'abc'
# print('__iter__' in dir(s1))
# print('__next__' in dir(s1))

# 2,判断该对象是不是可迭代器
# from collections import Iterator
# l1 = [1,2,3]
# print(isinstance(l1,Iterator))
# l1_obj = l1.__iter__()
# print(isinstance(l1_obj,Iterator))
#迭代器的好处
# 1,节省内存
# 2，惰性机制
# 3，单向执行，不可逆。

s1 = 'fkdsafhdskfhsdklfjdslfksd'
s1_obj = s1.__iter__()
while True:
    try:
        print(s1_obj.__next__())
    except StopIteration:
        break