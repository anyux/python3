#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 12:02
# @Author  : anyux
# @FileName: func-outer2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/


def wrapper1(func):
    def inner():
        print('wrapper1 ,before func')
        func()
        print('wrapper1 ,after func')

    return inner


def wrapper2(func):
    def inner():
        print('wrapper2 ,before func')
        func()
        print('wrapper2 ,after func')

    return inner


@wrapper2
@wrapper1
def f():
    print('in f')


dict_user = {
    1: "1",
    2: "1",
    3: "1",
    4: "1",
}
# print('__iter__' in dir(str))

# from collections import Iterable
# print(isinstance('a',Iterable))
str = '123'
obj = str.__iter__()  # <str_iterator object at 0x02B53950> 可迭代对象转换为迭代器
obj = iter(str)  # 可迭代对象转换为迭代器
# print(obj)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# while 循环模拟 for 循环
user_name = "素还真"
user_name_obj = user_name.__iter__()  # 转换成迭代器


def my_for():
    while True:
        try:
            tmp_user_name = user_name_obj.__next__()
            print(tmp_user_name)
        except StopIteration:
            break


import os, sys

# print(os.getcwd())
file = sys.argv[0]

'''
with open(file,encoding='UTF-8') as file_handle_1:
    print( '__iter__' in dir(file_handle_1))
    print( '__next__' in dir(file_handle_1))
    # for line in file_handle_1:
    #     print(line,end='')
'''

'''
def func1():
    print(111)
    yield 666
    print(222)
    print(333)
    yield 555
    print(6666)
    yield 777
ret = func1()
print(ret.__next__())
print(ret.__next__())
print(ret.__next__())
'''

'''
def cloth1():
    for i in range(50):
        yield  "衣服 %s " % i

cloth_obj = cloth1()

for i in range(5):
    print(cloth_obj.__next__())

for i in range(5):
    print(cloth_obj.__next__())

'''

'''
# 生成式表达式，列表推导式
py_list = []
for i in range(1,23):
    py_list.append("py%s期 " % i)
print(py_list)
'''

'''
l = [i for i in range(1,10)]
# [变量 (加工后的变量) for 变量 in iterable(可迭代对象)]
# print(l)

l2 = ['python %s 期 ' % i for i in range(1,23)]
print(l2)
'''

'''
num_list = []
for i in range(31):
    if i % 3 == 0:
        num_list.append(i)
print(num_list)

num_list2 = [i for i in range(31) if i%3 == 0]
print(num_list2)

'''

'''
list_obj = (i for i in range(1,10) if i % 3 == 0)
for i in list_obj:
    print(i)
print(list_obj)

'''

# 构建列表  10以内的所有元素的平方
# 30以内所有能被3整除的数据的平方
# [3,6,9]组成的表达式

number_10_inner = []
number_10_inner = [i * i for i in range(10)]
print(number_10_inner)

number_10_inner = []
number_10_inner = [i * i for i in range(10) if i % 3 == 0]
print(number_10_inner)

number_10_inner = [[], [], []]
number_3_inner = [3, 6, 9]
n = 0
number_10_inner = [[i - 2, i - 1, i] for i in number_3_inner]
'''
for i in number_3_inner:
    for j in range(i-2,i+1):
        number_10_inner[n].append(j)
    n +=1
'''
# print(number_10_inner)

x = {
    'name': 'alex',
    'Values': [{'timestamp': 1517991992.94,
                'values': 100, },
               {'timestamp': 1517992000.94,
                'values': 200, },
               {'timestamp': 1517992014.94,
                'values': 300, },
               {'timestamp': 1517992744.94,
                'values': 350},
               {'timestamp': 1517992800.94,
                'values': 280}
               ], }

list = x['Values']
list_info = []
# list_info = [[i['timestamp'],i['values']] for i in list  ]
# list_info = [[i['timestamp'],i['values']]  for i in x['Values']  ]
# list_info = [[j['timestamp'],j['values']] for j in  ]
# list_info = [[x[j][n]['values'],x[j][n]['timestamp']] for j in x  if j == 'Values' ]
list_info = [[j] for j in x if j == 'Values']
# print(list_info)

l1 = [ {'sales_volumn': 0},
     		{'sales_volumn': 108},
     		{'sales_volumn': 337},
     		{'sales_volumn': 475},
     		{'sales_volumn': 396},
     		{'sales_volumn': 172},
     		{'sales_volumn': 9},
     		{'sales_volumn': 58},
     		{'sales_volumn': 272},
     		{'sales_volumn': 456},
     		{'sales_volumn': 440},
     		{'sales_volumn': 239}]

L = [('a', 1), ('c', 3), ('d', 4),('b', 2), ]
sorted(L, key=lambda x:x[1])               # 利用key[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(sorted(l1, key = lambda x:x['sales_volumn']))

