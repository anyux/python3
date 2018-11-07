#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 12:53
# @Author  : anyux
# @FileName: test_5.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

'''

class A:
    compay_name = '素还真' #静态变量 静态字段
    __iphone = '1353333xxx' #私有静态变量 私有静态字段

    def __init__(self,name,age): #普通方法 构造方法
        self.name = name #对象属性 普通字段
        self.__age = age #私有对象属性 私有普通字段
    def func1(self): #普通方法
        pass
    def __func(self): #私有方法
        print(666)

    @classmethod # 类方法
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')
    @staticmethod # 静态方法
    def static_func():
        """ 定义静态方法，无默认参数"""
        print('静态方法')
    @property #属性
    def prop(self):
        pass

'''
'''
class C():
    name = "公共静态字段"
    def func(self):
        print(C.name)
class D(C):
    def show(self):
        print(C.name)
'''
'''
C.name #类访问
obj = C()
obj.func() # 类内部可以访问

obj_son = D()
obj_son.show() #派生类中可以访问
'''
'''
class C:
    __name = "私有静态字段"

    def fun(self):
        print(C.__name)
class D(C):
    def show(self):
        print(C.__name)

C.__name #不可在外部访问
obj = C()
obj.__name #不可在外部访问
obj.fun() #类内部可以访问

obj_son = D()
obj_son.show() # 不可在派生类中访问

'''
'''
class C:
    def __init__(self):
        self.foo = '公有字段'
    def func(self):
        print(self.foo) #类内部访问
class D(C):
    def show(self):
        print(self.foo) #派生类中访问
obj = C()
obj.foo #通过对象访问
obj.func() #类内部访问

obj_son = D()
obj_son.show() #派生类中访问
'''
'''
class C:
    def __init__(self):
        self.__foo = "私有字段"

    def func(self):
        print(self.__foo) #类内部访问

class D(C):
    def show(self):
        print(self.__foo) #派生类中访问

obj = C()
# obj.__foo #通过对象访问 ==》错误
obj.func() #类内部访问  ==》 正确

obj_son = D()
# obj_son.show() #派生类中访问 ==》 错误
'''
'''
class C:
    def __init__(self):
        pass
    def add(self):
        print('in C')
class D(C):
    def show(self):
        print('in D')
    def func(self):
        self.show()


obj_son = D()
obj_son.show() #通过对象访问
obj_son.func() #通过类内部访问
obj_son.add() #派生类访问
'''
'''
class C:
    def __init__(self):
        pass
    def __add(self):
        print('in C')
class D(C):
    def __show(self):
        print('in D')
    def func(self):
        self.__show()
obj = D()
obj.__show() #不能通过对象访问
obj.func() #类内部访问
obj.__add() #派生类中不能访问
'''
'''
class Province:
    #静态字段
    country = "中国"
    def __init__(self,name):
        # 普通字段
        self.name = name
# 直接访问普通字段
obj = Province('河北省')
print(obj.country)

# 直接访问静态字段

print(Province.country)
'''
'''
class Foo:
    def __init__(self,name):
        self.name = name

    def ord_func(self):
        """ 定义普通访问，至少有一个self参数"""
        #print slef.name
        print('普通方法')
    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数"""
        print("类方法")
    @staticmethod
    def static_func():
        """ 定义静态方法，无默认参数"""
        print("静态方法")
#调用普通方法
f = Foo('素还真')
f.ord_func()

#调用类方法
Foo.class_func()

#调用静态方法
Foo.static_func()
'''
'''
class People:
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
    @property
    def bmi(self):
        return self.weight/self.height
p1 = People('素还真',75,1.85)
print(p1.bmi)
'''
'''
class Goods(object):
    def __init__(self):
        #原价
        self.original_price = 100
        #折扣
        self.discount = 0.8
    @property
    def price(self):
        #实际价格= 原价* 折扣
        new_price = self.original_price * self.discount
        return new_price
    @price.setter
    def price(self,value):
        self.original_price = value
    @price.deleter
    def price(self):
        del self.original_price
obj = Goods()
obj.price #获取商品价格
obj.price = 200 #修改商品价格
print(obj.price)
del obj.price #删除商价格
'''
'''
class A: pass
class B(A):pass
obj = B()
print(isinstance(obj,B)) # True
print(isinstance(obj,A)) # True
'''
'''
class A:pass
class B(A):pass
obj = B()
print(issubclass(B,A)) #True
'''
'''
class Foo:
    f = "类的静态变量"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hi(self):
        print('hi,%s' % self.name)
obj = Foo('egon',73)
#检测是否含有某种属性
print(hasattr(obj,'name'))
print(hasattr(obj,'say_hi'))

#获取属性
n = getattr(obj,'name')
print(n)
func = getattr(obj,'say_hi')
func()

# print(getattr(obj,'aaaaaa','不存在啊')) #报错

#设置属性
setattr(obj,'sb',True)
setattr(obj,'show_name',lambda self:self.name+'sb')
print(obj.__dict__)
print(obj.show_name(obj))

#删除属性
delattr(obj,'age')
delattr(obj,'show_name')
# delattr(obj,'show_name111') #不存在，则报错
print(obj.__dict__)
'''
'''
class A:
    a = 1
    b = 2
    def __init__(self):
        self.c = 3
a1 = A()
a1.a = 333
a1.b = 444
print(a1.a,a1.b,a1.c)
'''
'''
class Foo(object):
    staticFiled = 'old boy'

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'
print(getattr(Foo,'staticFiled'))
print(getattr(Foo,'func'))
print(getattr(Foo,'bar'))
'''
'''
import sys
def s1():
    print('s1')
def s2():
    print('s2')

this_module = sys.modules[__name__]
h1 = hasattr(this_module,'s1')
h2 = hasattr(this_module,'s2')
print(h1,h2)
'''

'''
#一个模块中的代码
def test():
    print('from the test')

#修改后
class A:
    def test(self):
        print('from the test')
'''
'''
程序目录
    module_test.py
    index.py
    
当前文件：
    index.py
'''
'''
# 另一个模块中的文件
# import module_test as obj

# obj.test()
# 这里实例化
obj = A()
print(hasattr(obj,'test'))
getattr(obj,'test')()
'''
'''
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __len__(self):
        return len(self.__dict__)
    def fun(self):
        return self.__len__()
a = A()
print(len(a))
print(a.__dict__)
'''
'''
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __hash__(self):
        return hash(str(self.a)+str(self.b))
a = A()
print(hash(a))
'''
'''
class A:
    def __init__(self):
        pass
    def __str__(self):
        return '素还真'
a = A()
print(a)
print('%s'% a)
'''
'''
class A:
    def __init__(self):
        pass
    def __repr__(self):
        return '素还真'
a = A()
print(repr(a))
print("%r"%a)
'''
'''
class Foo:
    def __init__(self):
        pass
    def __call__(self,*args,**kwargs):
        print('__call__')
a = Foo() # 执行 __init__
a()   # 执行 __call__
'''
'''
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __eq__(self,obj):
        if self.a == obj.a and self.b == obj.b:
            return True
a = A()
b = A()
print(a == b)
'''
'''
class A:
    def __init__(self):
        self.x = 1
        print('in init function')
    def __new__(cls, *args, **kwargs):
        print('in new function')
        return object.__new__(A,*args,**kwargs)
a = A()
print(a.x)
'''
'''
class A:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance
'''
'''
class Foo:
    def __init__(self,name):
        self.name = name
    def __getitem__(self, item):
        print(self.__dict__[item])
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self, key):
        print('del obj[del]时，我执行')
    # def __delattr__(self, item):
        
'''
'''
class A:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    @property
    def func(self):
        rev = self.weight/(self.height * self.height)
        return rev
a = A('素还真',1.8,80)
aa = a.func
print(aa)
'''
'''
class A:
    def __init__(self,name,title,age):
        self.__name = name
        self.__title = title
        self.__age = age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @name.deleter
    def name(self):
        del self.__name
a = A('素还真','半神半圣','18')
print(a.name)

'''

import module as obj
import module

print(getattr(obj,'func')())
print(getattr(getattr(module,'A'),'role'))
