#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time



# 带参数的装饰器

# def timmerout(flag1):  # flag1 =flag
#     def timmer(f):
#         def inner(*args,**kwargs):
#             if flag1:
#                 start_time = time.time()
#                 ret = f(*args,**kwargs)
#                 end_time = time.time()
#                 print('此函数的执行效率%s' % (end_time - start_time))
#                 return ret
#             else:
#                 ret = f(*args, **kwargs)
#                 return ret
#         return inner
#     return timmer


# flag = False
# @timmerout('alex','nan',1000)  # 1,将@ 与函数分开@     timmerout(flag)  返回了timmer 2，将@timmer结合。
# def func1():
#     time.sleep(0.3)
#     print('非常复杂......')
#     return 666
#
# @timmerout(flag)
# def func2():
#     time.sleep(0.3)
#     print('非常复杂......')
#     return 666
#
#
# @timmerout(flag)
# def func3():
#     time.sleep(0.1)
#     print('非常复杂......')
#     return 666
# 1,将@ 与函数分开@     timmerout(flag)  返回了timmer
# 2，将@timmer结合



# def timmerout(flag1):  # flag1 =flag
#     def timmer(f):
#         def inner(*args,**kwargs):
#             if flag1:
#                 start_time = time.time()
#                 ret = f(*args,**kwargs)
#                 end_time = time.time()
#                 print('此函数的执行效率%s' % (end_time - start_time))
#                 return ret
#             else:
#                 ret = f(*args, **kwargs)
#                 return ret
#         return inner
#     return timmer

# @timmerout('京东')  # 1,将@ 与函数分开@     timmerout(flag)  返回了timmer 2，将@timmer结合。
# def JDshop():
#     time.sleep(0.3)
#     print('非常复杂......')
#     return 666
#
# @timmerout('京东')
# def JD():
#     time.sleep(0.3)
#     print('非常复杂......')
#     return 666
#
#
# @timmerout('淘宝')
# def taobao():
#     time.sleep(0.1)
#     print('非常复杂......')
#     return 666
#
# @timmerout('淘宝')
# def taobaoshop():
#     time.sleep(0.1)
#     print('非常复杂......')
#     return 666
#
# func1()
# func2()
# func3()


# 多个装饰器装饰一个函数


def wrapper1(func):  # func = f函数名
    def inner1():
        print('wrapper1 ,before func')  # 2
        func()  # f函数名()
        print('wrapper1 ,after func')  # 4
    return inner1

def wrapper2(func):  # func = inner1
    def inner2():
        print('wrapper2 ,before func')  # 1
        func()  # inner1()
        print('wrapper2 ,after func')  # 5
    return inner2

def wrapper3(func):
    def inner3():
        print('wrapper3 ,before func')
        func()
        print('wrapper3 ,after func')
    return inner3

# @wrapper3
# @wrapper2  # f = warpper2(f)  里面的f是inner1 外面的f是inner2
# @wrapper1  # f = warpper1(f)  里面的f函数名 外面的f 是inner1
# def f():
#     print('in f')  # 3
#
# f()  # inner2()

# wrapper2 ,before func
# wrapper1 ,before func
# in f
# wrapper1 ,after func
# wrapper2 ,after func
l = ['您好', '3.64',
     '请问您是刘晓宇同学的家长吗', '6.25',
     '是的有什么事情吗', '6.15',
     '您好我是学大教育的刘老师', '5.06',
     '这次给给您打电话主要是想了解一下孩子上学期的协议情况',
     '5.86', '针对于上学期的学习状况', '5.37', '我们学校邀请您和孩子周末过来听一下针对性的辅导课好吧好吧', '5.36', '可以我想问一下都有什么课程呢', '5.65', '呃主要是有英语和语文', '4.35', '你看', '3.77', '到时候咱们再联系好吧', '6.10', '好的', '6.45', '恩再见', '4.84']
# [{"onebest":"您好", "speed":"6.060606"},
# {"onebest":"我这是中国电信的客户代表请问您是幺五幺幺零幺五六六六幺号码的长期使用者吗", "speed":"5.479452"},
# {"onebest":"是的", "speed":"5.405406"},
# {"onebest":"为啥谢谢您长期以来的支持",  "speed":"5.529954"},
# {"onebest":"交银退掉", "speed":"4.938272"},
# {"onebest":"考虑了解生活小贴士服务美元四月","speed":"4.672897"},
# {"onebest":"你们可以收到天气情况活动", "speed":"5.529954"},
# {"onebest":"我建议", "speed":"4.347826"},
# {"onebest":"生活中了就是周转现在开通后","speed":"4.024768"},
# {"onebest":"发到您的", "speed":"8.510638"},
# {"onebest":"都会","speed":"4.255319"},
# {"onebest":"现在","speed":"6.451613"},
# {"onebest":"可以享有就是看吗", "speed":"5.161290"},
# {"onebest":"可以","speed":"6.451613"},
# {"onebest":"改天先生那是的",  "speed":"4.046243"},
# {"onebest":"另外再见",  "speed":"5.479452"}
# ]


