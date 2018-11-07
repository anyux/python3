#!/usr/bin/env python
# -*- coding:utf-8 -*-
# a = 1
# def func1():
#     print(a)
# func1()

# a = 1
# def func1():
#     global a
#     a += 1
#     print(a)
# func1()



# def func1():
#     a = 1
#     def inner():
#         print(a)
#     inner()
# func1()

def wrapper(f):  # f = func1
    def inner(*args, **kwargs): # *args：将所有的位置参数聚合成一个元素赋值给args
        args = (1,2)
        '''被装饰的函数之前的操作'''
        print(222)
        ret = f(*args, **kwargs)  # 函数的执行：*args 将可迭代对象中每个元素打散成位置参数 f(1,2)
        '''被装饰的函数之后的操作'''
        print(333)
        return ret
    return inner

@wrapper  # func1 = wrapper(func1)  被装饰函数的函数名新 = 装饰器的函数名（被装饰函数的函数名）
def func1(a,b):
    print(666)
    return True
print(func1(1,2))  # inner(1,2)
# * 的魔法功能
# *变量  在函数的定义中，是聚合。
# *变量  在函数的执行中，是打散。

#

# 1  执行wrapper函数，将func1函数名传给f
# 2  将inner函数名 返回给了新的变量func1  (func1 = inner)
# 3  func1()  ==  inner()  执行inner函数
#4   执行 222 执行func1 函数  执行333

# @wrapper
# def func2(k1):
#     print(666)
#
# func2(3)

# def func3(a):
#     a = 5
#     print(a)
#     return True
# func3(5)