# 序列化模块
# json
# pickle
# shelve


# 什么是序列：一个有序的结构
# 列表、元组、字符串
# 什么是序列化
# 实例化、结构化，序列化
# 数据结构 —序列化—> 字符串
# 字符串 -反序列化-〉数据结构
# lst = [1,2,3]
# s = str(lst)
# print(list(s))
# print(repr(eval(s)))

# 为什么需要序列化？？？
# 1.文件存储
# 2.网络传输

# 1.不能操作其他对象
# 2.安全性

import json
# dump
# load
# dumps 将数据类型转字符串
# loads 凡序列化过程
# lst = [1,2,3,4,"bbb"]
# dic = {'a':1,2:3,}
# ret1 = json.dumps(lst)
# ret2 = json.dumps(dic)
# print(lst,dic)
# print(ret1,ret2)
# print(type(ret1),type(ret2))
# res1 = json.loads(ret1)
# res2 = json.loads(ret2)
# print(res1,type(res1))
# print(res2,type(res2))

# t1 = (1,2,3)
# s1 = json.dumps(t1)
# print(json.loads(s1))
# d1 = {'(1,2,3)':123}
# json.dumps(d1)

# json 只支持有限的数据类型 字典 列表 数字类型
# json 字典的key只能是字符串
# f = open('json_file','w')
# json.dump([1,2,3],f)   # 只和文件相关
# json.dump({'a':4,'b':5,'c':6},f)   # 只和文件相关
# f.close()

# f = open('json_file','r')
# content = json.load(f)   # 只和文件相关
# f.close()
# print(content,type(content))


# 需要连续dump，使用dumps
# 10个字典
# 分别对每一个字典进行dumps转成字符串
# 写到文件+\n

# 反序列化的时候
# 先按行读"{}\n"
# 去掉换行符之后使用loads反序列化


# import json
# data = {'username':['李华','二愣子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data)
# json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
# print(json_dic2)


import pickle
# dump load
# dumps loads

# pickle 支持几乎所有数据类型 包括自定义的类和对象

# class A:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# file = open('pickle_file','wb')
# alex = A('alex',83)
# pa = pickle.dump(alex,file)
# file.close()
# del alex
# file = open('pickle_file','rb')
# pal = pickle.load(file)
# print(pal.name,pal.age)

import pickle
# file = open('pickle_file','wb')
# pickle.dump({1,2,3},file)
# pickle.dump({(1,2,3):456},file)
# file.close()

# file = open('pickle_file','rb')
# while True:
#     try:
#         print(pickle.load(file))
#     except EOFError:
#         break

# json
    # 结果可读
    # 所有的语言都通用
    # 数据类型有限

# pickle —— 游戏退出的存档
    # 结果是bytes
    # 只支持python语言
    # 几乎支持所有数据类型

# shelve
# import shelve
# f = shelve.open('shelve_file')
# f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
# f.close()
#
# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)








