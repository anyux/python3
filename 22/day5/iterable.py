#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 22:14
# @Author  : anyux
# @FileName: iterable.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
'''


# 字符串、列表、元组、字典、集合都可以被for循环，说明他们是可迭代对象
from collections import Iterable
list_ = [1,2,3,4]
type_ = (1,2,3,4)
dict_ = {1:2,3:4}
set_ = {1,2,3,4}

# isinstance 证明对方是可迭代对象
# isinstance 是python中的内建函数。是用来判断一个对象的变量类型
# 语法：
# isinstance(object,classinfo)
# 如果参数object是classinfo的实例，或者object是classinfo类的子类的一个实例，返回True.如果object不是给定类型的对象，则返回False
# 如果classinfo不表示一个类(类型对象),那么它要么是一个类的元组，或者递归地包含这样的(由数据类型构成的)元组，其他的序列类型是不被库允许的
# 如果classinfo不是一种数据类型或者由数据类型构成的元组，将引发一个TypeError异常
# 在python的IDLE或命令行解释器 键入help(isinstance)即可获得该函数的帮助信息：
# instance(object,class-or-type-or-tuple)
# print(isinstance(list_,Iterable))

# class my_class:
#     pass
# test = my_class()
#
# print(isinstance(test,my_class))

# 可迭代协议
# 可以被迭代要满足的要求就叫做可迭代协议。可迭代协议的定义非常简单，就是内部实现了__iter__方法

  # 总结 可以被for循环的都是可迭代的，要想可迭代，内部必须有一个__iter__方法
  # 接着分析,__iter__方法做了什么事情
  # 可迭代的：内部必须含有一个__iter__方法
# 迭代器
# 什么叫做迭代器？迭代器的英文意思是iterator
# list__ = [1,2,3,4]
# list__iter = list__.__iter__() #将可迭代对象转换为迭代器
# item = list__iter.__next__()
# print(item)
# item = list__iter.__next__()
# print(item)

# 迭代器遵循迭代器协议：必须拥有__iter__方法和__next__方法
# for 循环能遍历一个可迭代对象，他的内部到底做了什么？
# 将可迭代对象转换成迭代器 （可迭代对象.__iter()）
# 内部使用__next__方法一个一个取值
# 加了异常处理功能，取值到底后自动停止

# 使用while循环模板for循环
'''
'''
list__ = [1,2,3,4]
list__iter = list__.__iter__()

while True:
    try:
        print(list__iter.__next__())
    except StopIteration:
        break
'''

# 为什么要有for循环
'''
list = ['素还真','叶小钗','一页书']
for n in range(0,len(list)):
    print(list[n])
'''

'''
没错，序列类型字符串，列表，元组，都有下标，使用上面的方式访问，没有问题。
但是对于非序列类型，像字典，集合，文件对象，所以for 循环是基于迭代器协议提供的一个统一的可以遍历所有对象的方法，即在遍历之前，先调用对象__iter__()方法，将其转换成迭代器，再使用迭代器协议去实现循环访问，这样所有的对象就都可以通过for循环来遍历了，而且你看到的效果也确实如此，这就是无所不能的for循环，最重要的一点，转化成迭代器，在循环时，在同一时刻内存中只出现一条数据，极大限度地节省内存
'''

# 生成器
# 初始生成器
'''
我们知道的迭代器有两种，一种是调用方法直接返回的，一种是可迭代对象通过iter方法得到的，迭代器有的好处是可以节省内存
某些情况下，需要自己写
我们自己写的这个能实现迭代器功能的东西就叫做生成器
1.生成器函数，常规函数定义，但是，使用yield语句而不是return语句返回结果，yield语句一次返回一个结果，在每个结果的中间，扶起函数的状态，以便下次从它离开的地方继续执行
2.生成器表达式：类似于列表推导，但是，生成器返回按需产生结果的一个对象，而不是构建一个结果列表
生成器Generator:
    本质：迭代器（所以自带了__iter__方法和__next__()方法，不需要我们去实现）
    特点：惰性运算，开发者自定义
'''

# 生成器函数

'''
一个包含yield关键字的函数就是一个生成器函数。
yield可以为我们在函数中返回值，但yield又不同于return，return的执行意味着函数结束，
而调用生成器函数不会得到具体的值，而是一个可迭代的对象。
每获取这个可迭代对象的值，就能推动函数的执行，获取新的返回值，直到函数结束
'''

'''
import time

def genrator_func1():
    a = 1
    print("现在定义了变量a")
    yield a
    b = 2
    print("现在定义了变量b")
    yield b

genrator = genrator_func1()
print(genrator)
print('-'*20)
print(genrator.__next__())
time.sleep(.5)
print(genrator.__next__())

# 初始生成器函数
'''

'''
生成器有什么好处呢？就是不会一下子在内存中生成太多数据
假如我想让工厂给学生做校服，生产2000件衣服，此时，我选择一件一件的拿衣服，而不是批量的获取
即不是说一下子生产2000件衣服
'''

'''
def make_cloth():
#     生产衣服
    for i in range(1,2000):
        yield ( "生产第%s件衣服" % i)
cloth = make_cloth() # 返回值cloth 是 <generator object make_cloth at 0x02B9B2D8>
print(cloth)
print(cloth.__next__()) #执行__next__()方法，返回的是yield的内容
print(cloth.__next__())
print(cloth.__next__())

num = 0
for i in cloth: #再生产五件衣服 因为for循环会自动调用__next__()方法，所以可以直接打印 yield的返回值
    print(i)
    num += 1
    if num == 5: break
'''

''''

# send
def get_cloth():
    print(123)
    content = yield 1
    print('=====',content)
    print(456)
    yield 2
cloth = get_cloth()
ret = cloth.__next__()
print('***',ret)
ret = cloth.send('hello') # send 的效果和next一样
print('***',ret)

# send 获取下一个值的效果和next一样
# 只是在获取下一个值的时候给上一个yield的位置传递一个数据
# 使用send注意事项
# 第一次使用生成器的时候，是用next获取下一个值
# 最后一次yield不能接受外部的值
'''

# 列表推导式和生成器表达式
'''
list = [i for i in range(10)]
print(list)

list2 = ['选项%s' % i for i in range(10)]
print(list2)
1.把列表解析的[]换成()得到的就是生成器表达式
2.列表解析与生成器表达式都是一种便利的编程方式，只不过生成器表达式更节省内存
3.python不但使用迭代器协议，让for 循环更加通用，大部分内置函数，也就是使用迭代器协议访问对象，例如，sum函数是python内置函数，该函数使用迭代器函数访问对象而生成器实现了迭代器协议，所以我们可以直接这样计算一系列值的和：
print(sum(x ** 2 for x in range(40)))
'''

# 推导式套路
'''
之前已经学习了最简单的列表推导式和生成器的表达式。但是除此之外，还有字典推导式，集合推导式等。
下面是一个以列表推导式为例的推导式详细格式，同样适用于其他推导式。
variable = [out_exp_res for out_exp in inputlist if out_exp == 2]
    out_exp_res: 列表生成元素表达式，可以是有返回值的函数
    for out_exp in inputlist:迭代inputlist 将out_exp 传入out_exp_res表达式中
    if out_exp == 2: 根据条件过滤哪些值可以
'''

# 列表推导式
'''
例一：30以内所有能被3整除的数
muliples = [i for i in range(30) if i % 3 ==0]
print(muliples)

#例二：30以内所有能被3整除的数的平方
mutiples = [i*i for i in range(30) if i % 3 == 0]
print(mutiples)
# 例三：找到嵌套列表中名字含有两个'e'的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

name_list =([name  for list_names in names for name in list_names if name.count('e') >= 2] ) #注意遍历顺序，这是实现的关键
print(name_list)
'''

# 字典推导式
'''
#例一：将一个字典的key和value对调
mcase = {
    'a':10,
    'b':34
}
mcase_frequency = {mcase[k]:k for k in mcase}
print(mcase_frequency)
# 例二：合并大小写对应的value值，将k统一成小写
mcase = {
    'a':10,
    'b':34,
    'A':7,
    'Z':3,
}
mcase_frequency = {k.lower():mcase.get(k.lower(),0)+mcase.get(k.upper(),0) for k in mcase.keys()} #强行对每一个键的不区别大小写的相加
print(mcase_frequency)
'''

# 集合推导式
'''
# 例：计算列表中每个值的平方，自带去重功能
squared = {x**2 for x in [1,-1,2]}
squared = ((x**2 for x in [1,-1,2]))
squared = [x**2 for x in [1,-1,2]]
print(squared)
'''

# 练习题
'''
# 例一：过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
word_list = ['abc','a','b','c','poiu','NMKHGU','dhfkdfh']
my_word_list = [words.upper() for words in word_list if words.__len__() >= 3]
print(my_word_list)

# 例二：求(x,y)其中0-5之间的偶数，y是0-5之间的奇数组成的无组列表
my_tuple = [(x,y) for x in range(0,5) if x % 2 == 0 for y in range(0,5) if y % 2 == 1]
print(my_tuple)

# 例三：求M中3，6，9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]

M = [[i-2,i-1,i] for i in [3,6,9]]
print(M)
'''

# 递归函数
# 递归初始
'''
递归函数：在一个函数里调用这个函数本身
递归的最大深度是：998
递归不受阻止会一直执行下去，函数调用时说过，每一次函数调用都会产生一个属于它的名称空间，如果一直调用下去，会造成名称空间占用太多内存的问题，于是python为了杜绝此类现象，强制将递归层数设置为997
证明997的理论
def func(n):
    print(n)
    n += 1
    if n != 998:
        func(n)

func(1)
由此，看出，未报错之前能看到的最大数字是998，当然，997是内存优化所设定的默认值。我们可以修改它
import sys
print(sys.setrecursionlimit(100000))
我们可以通过以上代码修改递归深度，实际到达的深度取决于计算机性能。不建议修改递归次数默认值

'''

# 递归示例讲解
'''

'''




























