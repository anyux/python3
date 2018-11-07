#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
len()
print()
input()
range()
list()
tuple()
str()
int()
set()。。。。。
'''
# 1 作用域相关
# locals golbals
# 1.2其他相关
# 1.2.1 ***eval exec
# print(eval('1 + 2 +3'))
# print(eval("{'name':'alex'}"),type(eval("{'name':'alex'}")))
# exec:执行字符串类型的代码。
# print(exec('1 +2 +3'))
#
s1 = '''
for i in range(5):
    print(i)
'''
# print(exec(s1))

# 　compile:将字符串类型的代码编译。代码对象能够通过exec语句来执行或者eval()进行求值。
# 1.2.2 输入输出相关 ***input，print
# print(1, 2, 3, sep='****') # 分隔符
# print(1111,end='')  # 换行
# print(222)
# with open('练习',encoding='utf-8', mode='w') as f1:
#     print('今天天气还可以',file=f1)
# *hash：获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值。

# print(hash('alex'))
# print(hash('alex1'))
# print(hash((1,2,3)))
# print(hash(10))
# print(hash(99))
# print(hash(True))

# ** id:用于获取对象的内存地址。
# 1.2.5
# * 帮助help：函数用于查看函数或模块用途的详细说明。
# print(help(str))

# 1.2.6调用相关
# ** callable：函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败
# ；但如果返回False，调用对象ojbect绝对不会成功。
# name = 'alex'

# def func1():
#     print(111)
# print(callable(name))
# print(callable(func1))

# **1.2.7查看内置属性dir
# 1.4 基础数据类型相关
# 1.4.1数字相关（14）
# 　　数据类型（4）：
# 　　　　bool ：用于将给定参数转换为布尔类型，如果没有参数，返回 False。
# 　　　　int：函数用于将一个字符串或数字转换为整型。
# **int：函数用于将一个字符串或数字转换为整型。
# print(int())  # 0
#
# print(int('12'))  # 12
#
# print(int(3.6))  # 3

# *float：函数用于将整数和字符串转换成浮点数。
# i = 2.456
# print(i,type(i))
# print(float(1.1))

# 　complex：函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
# 如果第一个参数为字符串，则不需要指定第二个参数。。
# i = 1 + 2j
# print(type(i))
# import math
# print(math.pi)

# 进制转换（3）：*
#
# 　　　　bin：将十进制转换成二进制并返回。
#
# 　　　　oct：将十进制转化成八进制字符串并返回。
#
# 　　　　hex：将十进制转化成十六进制字符串并返回。
# print(bin(19))
# print(oct(9))
# print(hex(15))
# 数学运算（7）：
#
# 　　　　abs：函数返回数字的绝对值。
# print(abs(-1.2))
#  *** divmod：计算除数与被除数的结果，
# 返回一个包含商和余数的元组(a // b, a % b)。
# print(divmod(100,7))  #  （商，余数）
# *round：保留浮点数的小数位数，默认保留整数。
# print(round(3.43543656,4))
# *pow：求x**y次幂。（三个参数为x**y的结果对z取余）
# print(pow(2,3))
# print(pow(2, 3, 3))

# *** sum：对可迭代对象进行求和计算（可设置初始值）。
l1 = [i for i in range(100)]
# print(sum(l1))
# print(sum(l1,100))

l2 = [2, 5, 6, -7]
# ***min：返回可迭代对象的最小值（可加key，key为函数名，
# 通过函数的规则，返回最小值）。
# print(min(l2))
# print(min(l2,key=abs))
# *** max：返回可迭代对象的最大值（可加key，key为函数名，通过函数的规则，返回最大值）。
# print(max(l2,key=abs))
# reversed：将一个序列翻转，并返回此翻转序列的迭代器。
l3 = [2, 3, 9, 8, 7, 4]
# l3.reverse()
# print(l3)
# l_obj = reversed(l3)
# # print(l_obj)
# for i in l_obj:
#     print(i)

# * slice：构造一个切片对象，用于列表的切片。
# l3 = [2, 3, 9, 8, 7, 4]
# rule = slice(0,3)
# print(l3[rule])

# * format 科学计算
# print(format('test', '<30'))
# print(format('test', '>20'))
# print(format('test', '^20'))

# bytes 将unicode 转化成bytes
# s = 'alex'
# b1 = s.encode('utf-8')
# print(b1)
# print(bytes(s, encoding='utf-8'))

#
# ret = bytearray('alex',encoding='utf-8')
# print(id(ret))
# print(ret)
# print(ret[0])
# ret[0] = 65
# print(ret)
# print(id(ret))

# ret = memoryview(bytes('你好',encoding='utf-8'))  # [xe31,x312,x3 ]
# print(len(ret))
# print(ret)
# print(bytes(ret[:3]).decode('utf-8'))
# print(bytes(ret[3:]).decode('utf-8'))
# ord 输入字符找该字符编码的位置    unicode
# print(ord('a'))
# print(ord('中'))

# chr 输入位置数字找出其对应的字符
# print(chr(97))
# print(chr(20013))

# 是ascii码中的返回该值，不是就返回/u...
# print(ascii('a'))
# print(ascii('中'))

# **repr:返回一个对象的string形式（原形毕露）。
# print(repr('{"name":"alex"}'),type(repr('{"name":"alex"}')))
# print('{"name":"alex"}')
# print('python%s期' % '22')
# print('python%r期' % '22')
l3 = [2, 3, 9, 8, 7, 4]
# l3.sort()
# print(l3)
#*** 　sorted：对所有可迭代的对象进行排序操作。
# ll = sorted(l3)
# print(ll)
# sorted()
# def func(x): return x[1]
# L = [('a', 3), ('d', 4), ('b', 2), ('c', 1), ]
# print(sorted(L, key=func))
# *** enumerate:枚举，返回一个枚举对象。
l1 = ['alex', 'laonanhai', 'taibai']
# for index,content in enumerate(l1):
#     print(index,content)
# for index,content in enumerate(l1,10):
#     print(index,content)

# 　**all：可迭代对象中，全都是True才是True
#
# 　**any：可迭代对象中，有一个True 就是True
# l1 = [1, 'alex', 3]
# l2 = [0, '', False,(), 1]
# print(all(l1))
# print(any(l2))

# ***zip 拉链方法
# l1 = [1,2,3,]
# l2 = ['a','b','c',5]
# l3 = ('*','**',(1,2,3),666,777)
# for i in zip(l1, l2, l3):
#     print(i)

#***map:会根据提供的函数对指定序列做映射。返回的是迭代器
# def square(x):
#     return x ** 2
# # print(map(square, [1,2,3,4,5]) )
# for i in map(square, [1,2,3,4,5]):
#     print(i)

# print((i**2 for i in [1,2,3,4,5]))


#类似于[i for i in range(1,8) if i % 2 == 0 ]
# def func(x):return x%2 == 0
# ret = filter(func,[1,2,3,4,5,6,7])
# print(ret)
# for i in ret:
#     print(i)

# min max sorted map filter

# 匿名函数

# def func(x,y): return x + y
# print(func(3,4))
# func1 = lambda x,y: x + y
# print(func1(3,4))
# # def func1(x): return x**2
# res = map(lambda x: x**2,[1,5,7,4,8])
# for i in res:
#     print(i)

# l1 = [ {'sales_volumn': 0},
#      		{'sales_volumn': 108},
#      		{'sales_volumn': 337},
#      		{'sales_volumn': 475},
#      		{'sales_volumn': 396},
#      		{'sales_volumn': 172},
#      		{'sales_volumn': 9},
#      		{'sales_volumn': 58},
#      		{'sales_volumn': 272},
#      		{'sales_volumn': 456},
#      		{'sales_volumn': 440},
#      		{'sales_volumn': 239}]
# print(sorted(l1,key= lambda x:x['sales_volumn']))