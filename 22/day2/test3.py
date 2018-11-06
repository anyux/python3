#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 10:30
# @Author  : anyux
# @FileName: test3.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# 元组 只读列表
# 元组中如果包含列表，则列表操作不受限制
user_tuple = ('素还真','叶小钗','一页书',['天踦爵','无梦生'])
print(user_tuple[0])
print(user_tuple[:-1])
for item in user_tuple:
    print(item)
user_tuple[-1].append('鷇音子')
print(user_tuple)

# range
print(range(100))
for item in range(100):
    print(item,end='')
for item in range(1,12):
    print(item,end='')
for item in range(2,101,2):
    print(item,end='')
for item in range(100,0,-1):
    print(item,end='')
for item in range(len(user_tuple)):
    print(user_tuple[item])
