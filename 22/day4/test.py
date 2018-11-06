#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 9:26
# @Author  : anyux
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# 形参顺序
# 位置参数 ，*args 默认参数，**kwargs
'''

def func_1():
    print('素还真')
    def func_4():
        print('风彩铃')
        name = '风彩铃'
    func_4()
    print(locals())
    print(globals())
def func_2():
    func_1()
    print('叶小钗')
def func_3():
    name = '一页书'
    func_2()
    print('一页书')

func_3()
print(globals())
'''

'''
def index():
    def get():
        url = 'http://www.xiaohua100.com/index.html'
        get =  
    return get
content = index()
print(content)
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print('list1=%s'%list1)
print('list2=%s'%list2)
print('list3=%s'%list3)
'''
import time

def get_time(x):
    def inner(*args,**kwargs): #args = (1,2),kwargs = {'sex':'man','name':'素还真'}
        start_time = time.time()
        return_name = x(*args,**kwargs) #此时函数打散 func_2(1,2,sex='man',name='素还真')
        end_time = time.time()
        print( end_time - start_time )
        return return_name
    return inner

@get_time
def func_2(a,b,name,sex):
    time.sleep(.1)
    print(a,b,name,sex)
    return name
print(func_2(1,2,sex='man',name='素还真'))


'''
@get_time #语法糖的装饰器 相当于 func_1 = get_time(func_1)
def func_1(a,b):
    print(a,b)
    time.sleep(.1)
    print("素还真")
func_1(1,2)
'''









