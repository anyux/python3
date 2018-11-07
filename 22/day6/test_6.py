#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/24 13:29
# @Author  : anyux
# @FileName: test_6.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
'''

# python 提供了68个内置函数，可以直接拿来使用
# 作用域相关
# locals:函数会以字典的类型返回当前位置的全部的局部变量
# globals: 函数会以字典的类型返回全部的全局变量

a = 1
b = 2
print(locals())
print(globals())
# 这两个一样，因为都是在全局执行的

'''
'''
a = 1
def func(argv):
    c = 1
    print(locals())
    print(globals())
func(3)
'''
'''
字符串类型代码的执行 eval,exec,complie
eval : 执行字符串类型的代码，并返回最终结果
print(eval('2+2'))
n = 81
print(eval('n+4'))
eval('print(6666)')
'''
'''
exec: 执行字符串类型的代码
s = '''
'''
for i in [1,2,3]:
    print(i)
'''
'''
exec(s)
'''
'''
compile:将字符串类型的代码编译。代码的对象能通过exec语句来执行或者eval()进行求值
参数说明：
1.source,需要执行的代码
2.filename,从文件中读取，1，2只能先一个
3.指定编译种类，exec,eval,single 三种，
    a.代码包有流程语句使用exec
    b.求值时 eval
    c.交互时 single
#流程语句使用exec
code1 = 'for i in range(0,10):print(i)'
compile1 = compile(code1,'','exec')
exec(compile1)
#简明求值表达式
code2 = '1 + 2 + 3 + 4'
compile2 = compile(code2,'','eval')
print(eval(compile2))
compile2 = compile(code2,'','exec')
print(exec(compile2))
'''
'''
输入输出相关input,print
input:函数接受一个标准输入数据，返回string类型
print:打印输出
'''
'''
内存相关hash id
hash 获取一个对象 （可哈希对象：int,str,bool,tuple）的哈希值
print(hash(123))
print(hash('123'))
print(hash('arg'))
print(hash(True))
print(hash(False))
print(hash((1,2,3)))
id：用于获取对象的内存地址
print(id(123))
print(id('123'))
'''
