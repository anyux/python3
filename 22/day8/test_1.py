#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 10:36
# @Author  : anyux
# @FileName: test_1.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

from math import sqrt
import collections
import time

# Point = collections.namedtuple('point',['x','y'])
# p = Point(1,2)
#
# print(p.x) # 访问元组的第一个元素
#
# len = sqrt(p.x**2 + p.y**2)
# print(len)

# 程序会变得更明确，可读性更高

# q = collections.deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)
# print(q.pop())
# print(q.popleft())
# print(q)

# d = dict([('a',1),('b',2),('c',3)])
# print(d)
# od = collections.OrderedDict([('a',1),('b',2),('c',3)])
# print(od)
# od['z'] = 1
# od['y'] = 2
# od['x'] = 3
# print(od.keys())

# values = [11, 22, 33,44,55,66,77,88,99,90]
# my_list = collections.defaultdict(list)
# for value in values:
#     if value > 66:
#         my_list['k1'].append(value)
#     else:
#         my_list['k2'].append(value)
# print(my_list)
# dd = collections.defaultdict(lambda: 'N/A')
# dd['k1'] = 'abc'
# print(dd['k1'])
# print(dd['k2'])

# tf = '%Y-%m-%d %H:%M'
# print(time.strftime(tf,time.localtime(time.time())))


def get_code(num):
	import string
	import random

	test_code = []
	codes = ''

	lower_letter = list(string.ascii_lowercase[:])
	upper_letter = list(string.ascii_lowercase[:].upper())
	test_number = [i for i in range(0,10)]

	sum_char = lower_letter + upper_letter + test_number
	random.shuffle(sum_char)

	for i in range(num):
		code = str(random.choice(sum_char))
		codes = codes + code
	return codes
print(get_code(10))

