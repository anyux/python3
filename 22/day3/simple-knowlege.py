#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/19 10:22
# @Author  : anyux
# @FileName: simple-knowlege.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# int
# == 比较数值
# is 比较内存地址 是否相等 is 是比较运算
# id() 测试内存地址 返回数值形式的内存地址
'''

id(object)
Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

CPython implementation detail: This is the address of the object in memory.
'''


# 小数据池 为了节省内存 只有int str有
# str 不能有特殊符号
# 单个元素 *数字 ，不能超过21
'''


i = 'a'*20
i1 = 'a'*20
print(id(i),id(i1))
i = 'a'*21
i1 = 'a'*21
print(id(i),id(i1))
'''

'''
03 编码二
    asicc:数字，字母，特殊字符
    字节：8位表示一个字符
    字符：内容的最小组成单位
        abc:a 一个字符
        中国:中一个字符
        a: 0000 1111
    unicode:万国码
        1.初期 用两个字节表示任意字符，2**16=65535，只能表示6万多个数字，不够用
        2.升级 使用四个字节表示任意字符  2**32 约等于42亿 
    utf-8:最少用8位表示一个字符
        a : 0000 1111
        欧洲：16位
        亚洲：24位
    gbk:国标码（只有中文和英文）
        a:0000 1111
        中: 0000 1111 0000 1011 两个字节
    gbk，utf-8 对于英文是可以识别的，因为他们基于asicc码识别英文
    1.每一个编码相当于一个密码本，不能直接相互转换
    2.对于文件存储及传输，绝对不能使用unicode，可以使用其他编码类型
    
    python3 
        字符串在内存中编码方式为unicode,其他为utf-8
        字符串不能直接用于文件存储传输
        int 
        bool
        bytes:拥有str的所有操作方法，区别在于bytes的内部编码方式（非unicode,utf-8,gbk）
        str: 内部编码方式unicode
        list
        dict
        tuple
    bytes:拥有str的所有操作方法，区别在于bytes的内部编码方式（非unicode,utf-8,gbk）
    str: 内部编码方式unicode
        字母：
            str:表现形式：s1 = 'alex'
                内部表现：unicode
            bytes:表现形式 s2 = b'alex'
                内部表现：非unicode
        中文：
            str:表现形式：s1 = '中国'
                内部表现：unicode
'''
# bytes:表现形式 s2 = b"\xe\xb8\xad\xe5\x9b\xbd"
'''
                内部表现：非unicode
            print('中国'.encode())
        
    str = '素还真'
    str ---> bytes encode
    b1 = str.encode('utf-8')
    b2 = str.encode('gbk')
    
    bytes ---> str decode 默认转换成utf-8
    str1 = b1.decode('utf-8')
    str2 = b2.decode('gbk')
    
    str = 'abc'
    b1 = str.encode('utf-8')
    b2 = b1.decode('gbk')
    不会报错
    但是对于中文
    str = '中国'
    b1 = str.encode('utf-8')
    b2 = b1.decode('gbk')
    会报错
    utf-8 转换为 gbk,需要通过unicode中间转换
04.集合
    1.集合 要求它里面的数据，是可哈希，元素不重复，无序，
        集合本身是不可哈希的，利用二分查找
    set1 = {}
        功能
            1.关系测试
            2.去重（自动）
    set1 = {1,1,2,2,3,3,4,4,5}
    列表去重
        方法1：列表转换为集合
        list = [1,1,2,2,3,3,4,4,5]
        set1 =set(list)
        list1 = list(set1)
        方法2：使用算法
    增
        set1.add('1') #增加元素
        set.update('abc') #迭代增加元素
    删
        set1.pop() #随机删除
        set1.remove('1') #按元素删除
        set1.clear() #清空列表
        del set1 #删除整个集合
    查 
        for i in set1:
            print(i)
    关系测试
        set1 = {1,2,3,4,5}
        set2 = {4,5,6,7,8}
        交集
            print(set1 & set2)
            print(set1.intersection(set2))
        并集
            print(set1 | set2)
            print(set1.union(set2))
        差集
            print(set1 - set2) #set1独有的元素
            print(set1.different(set2))        
        反交集
            print(set1 ^ set2)
            print(set1.symmetric_difference(set2))
        子集
            set1 = {1,2,3}
            set2 = {1,2,3,4}
            print(set2>set1)
            print(set1.issubset(set2))
        超集
            print(set2 > set1)
            print(set2.issuperset(set1))
    动集合
        set1 = {1,2,3}
        print(frozenset(set1))
# 05.深浅拷贝
    # s1 s2 共用了一个内存地址
        s1 = [1,2,3]
        s2 = s1
        s1.append(6666)
        print(s1,s2)
    
# 浅copy
s1 = [1, 2, 3]
s2 = s1.copy()
s1.append(4)
print(s1, s2)
# 浅copy2
s1 = [1, 2, 3, [1, 2, 3]]
s2 = s1.copy()
s1[-1].append(4)
print(s1, s2)
# 浅拷贝 第一层各自独立，从第二层开始，共用一个内存地址

# 深拷贝
import copy
s1 = [1, 2, 3, [1, 2, 3]]
s2 = copy.deepcopy(s1)
s1[-1].append(4)
print(s1, s2)
# 深copy 无论多少层，都是相互独立的
'''

'''
# 面试题
# 切片是浅copy
s1 = [1,2,3,[11,22]]
s2 = s1[:]
s1[-1].append(666)
print(s1,s2)
'''
'''
06 文件操作
    filename.txt
    文件路径：path,
    编码方式: encoding,
    打开方式: mode 读，写，读写，写读，追加，改
file_handle = open('test.txt',encoding='utf-8',mode='r')
print(file_handle.read())
file_handle.close()
file_handle 文件句柄，任意定义，根据文件句柄进行操作
open() 是python的内置函数，内置函数调用的是操作系统的api
一切对文件进行的操作都是基于文件句柄file_handle
file_handle.close() 关闭文件句柄
执行流程：
    1.打开文件，产生文件句柄
    2.对文件句柄进行操作
    3.关闭文件句柄
# 编码错误
    UnicodeDecodeEroor:'bgk' codec can't byte .....
    表明用户文件编码与与程序打开编码不致造成的
# 路径错误
    1.r'd:/xxxxx.txt' #表示 / 只表示路径 
    2.使用两个反斜线表示
        'd://xxxxx.txt' #绝对路径
        './test.txt'    #相对路径

file_handle = open('test.txt',encoding='utf-8',mode='r')
print(file_handle.read())
file_handle.close()
'''
# 文件操作
#   读
#     r rb r+ r+b
#   写
#     w wb w+ w+b
#   追加
#     a ab a+ a+b

# 读 r 默认读模式
# file_handle = open('test.txt',encoding='utf-8',mode='r')
# 读 rb 操作非文字类文件
# file_handle = open('test.txt',mode='rb')
# 读取图片
# file_handle = open('a.png',mode='rb')
# 2.read(n) r模式的 n 是字符
# 2.read(n) rb模式的 n 是字节
# print(file_handle.read(10))

# 3.readline() 按行读取
# print(file_handle.readline())
# 4.readlines() 将读取的每一行，写入到列表的元素中
# print(file_handle.readlines())
# 5.循环文件句柄
#   优势始终只占一条句柄，几乎不占内存
# for line in file_handle:
#     print(line)

# file_handle.close()
# read 全部读出

# w 模式
# 没有文件，创建文件写入，
# 有原文件，先清空文件，再写入
# file_handle = open('test.txt',encoding='utf-8',mode='w')
# file_handle.write("三非焉罪，无梦制胜")
# file_handle.close()

# 图片读取及写入
# wb 模式 ,只要使用w 没有文件创建文件，
# 有文件清空文件，写入内容
# file_handle = open('a.png',mode='rb')
# content = file_handle.read()
# file_handle_2 = open('b.png',mode='wb')
# file_handle_2.write(content)
# file_handle_2.close()
# file_handle_2.close()
# file_handle.close()

# 追加 a
# 没有源文件，创建源文件，写入
# 有源文件，追加源文件

'''
file_handle = open('test.txt',encoding='utf-8',mode='a')
file_handle.write('三年寻龙，十年点穴,')
file_handle.write('\n三年寻龙，十年点穴,')
file_handle.close()
'''

# r+ 表示 r + 加了w功能
# 表示读写模式 ,先读后写,将内容写入到读到的光标
# 先写后读，将内容写入到文件头
# 推荐先读后写，将内容写入文件尾
'''
file_headle = open("test.txt",encoding='utf-8',mode='r+')
# print(file_headle.read())
file_headle.write('666')
print(file_headle.read())
file_headle.close()
'''
# w+ 先写后读 用的不多
# 指针移动到文件尾，移动光标到文件头
# seek()
'''
file_handle = open('test.txt',encoding='utf-8',mode='w+')
file_handle.write('无梦制胜')
file_handle.seek(0)
print(file_handle.read())
file_handle.close()
'''
# a+
'''
file_handle = open('test.txt',encoding='utf-8',mode='a+')
file_handle.write('三年寻龙，十年点穴')
file_handle.seek(0)
print(file_handle.read())
file_handle.close()
'''
# 其他方法
'''
read readline readlines write
close 
fileno # 文件描述符
flush  #刷新文件内部缓冲区
readable #是否可读
writeable #是否可写
seek 指定文件指针
tell 当前文件光标位置 tell(0,2)将光标调整到结尾 tell(0)是将光标调整文件头
上两个函数，可以组成断点续传功能点
truncate() 只在a或a+模式下使用，对源文件按照字节截取
'''
# file_handle = open('test.txt',encoding='utf-8',mode='a+')
# print(file_handle.readable())
# print(file_handle.writable())
# print(file_handle.read(3))
# print(file_handle.tell())
# print(file_handle.seek(0))
# print(file_handle.seek(0,2))
# file_handle.truncate(3)
# file_handle.close()

# with open()
# 好处：
#       1.不用主动关闭文件句柄
#       2.一个with语句可以操作多个文件句柄
#       3.推荐使用文件随时关闭文件file_handle.close()
'''
with open('test.txt',encoding='utf-8',mode='r') as file_handle,open('test2.txt',encoding='utf-8',mode='r+') as file_handle_2:
    content = file_handle.read()
    print(content)
    file_handle_2.write("真的猛")
    file_handle_2.seek(0)
    print(file_handle_2.read())
'''
# 文件改 操作
# 1.以读模式打开源文件
# 2.以写模式打开新文件
# 3.将原文件修改后的内容写入到新文件
# 4.删除原文件
# 5.将新文件重命名原文件
'''
import os
with open('test.txt',encoding='utf-8',mode='r') as file_h1,open('tmp_test.txt',encoding='utf-8',mode='w') as file_h2:
    content_file_h1 = file_h1.read()
    content_file_h2 = content_file_h1.replace('无','有')
    file_h2.write(content_file_h2)
os.remove('test.txt')
os.rename('tmp_test.txt','test.txt')
'''
# 07 函数
# 初识函数
# 函数的返回值
# 函数的传参

'''
def my_len(x):
    i = 0
    for item in x:
        i += 1
    return i
my_list = ['三余无梦生','鷇音子','天踦爵']
print(my_len(my_list))

'''
# 重复代码多
# 可读性差
'''
def 关键字 函数名():
    函数体
    函数执行,函数名
函数以功能为导向
return 
#       终止函数
#       给函数的执行者返回值
#       return  或 return None 什么都不返回
#       return 0 返回单个值 返回什么，得到什么
#       return '素还真','天踦爵','无梦生' 返回的是一个元组，
'''

# 函数传参
# 实参 实际参数
# 形参 形式参数

'''
def my_max(x,y):
    if x > y:
        return x
    else:
        return y
print(my_max(3,4))
'''
# 默认参数

# 动态参数，万能参数,*args,**kwargs
# args ：所有位置参数，放在一个元组中
# kwargs ：所有的关键字参数，放在一个字典中
# 函数定义的时候，* 代表聚合
# 在函数执行时，*代表离散 ，多个参数添加到一个args元组中
# 在函数执行时，**代表离散，多个字典参数添加到一个字典中

# 参数顺序
# 形参顺序，位置参数*args,默认参数，**kwargs













