#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 16:16
# @Author  : anyux
# @FileName: test2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# # 格式化输出 % 占位符 s d
# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# job = input('请输入你的职业：')
# hobbie = input('请输入爱好：')
# msg = '''--------------info of %s----------------------
# Name : %s
# age : %d
# job : %s
# hobbie : %s
# --------------end of %s----------------------
# ''' % (name,name,int(age),job,hobbie,name)
# print(msg)

# 前后都是比较运算
# 优先级：() > not > and > or
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)

# 2, 前后都是数值
# 0 是False 其他都是True
# x or y
# if x is True:
#     return y

# print(3 or 4)
# print(1 or 4)
# print(0 or 4)
# print(-1 or 4)
# print(3 and 5)
# print(3 or 4 and 5)

# 按照索引取值，与元素本身的数据类型一致
# 按照切片取值，取出来的是小列表
user_list = ['素还真',('墨渊水莲','业火红莲','耀世白莲'),'天踦爵','三余无梦生','鷇音子','解锋镝']
user_chice = user_list[:3]
print(user_chice,type(user_chice))
# 增
# append() 追加
user_list.append('千叶传奇')
print(user_list)
# insert() 插入
# insert(索引位置，内容)
user_list.insert(1,'天官赐福')
print(user_list)

# extend 将对象迭代地追加到列表中
# 提示：字符串会被拆分成单个字符追加到列表
# 列表会被拆分成单个元素追加到列表
# 元组会被拆分成单个元素追加到列表
# 字典会被拿出键名做为元素追加到列表
user_list.extend(['素续缘','风彩铃'])
user_list.extend(('原无乡','芳天秀'))
user_list.extend({"name":"四智武童"})
print(user_list)

# 删除
# 按照索引删除 pop(索引) 默认删除最后一个元素 且返回删除元素的内容
ret = user_list.pop()
print(ret)
print(user_list)

# 按照元素删除 remove
user_list.remove("原无乡")
user_list.remove("芳天秀")
print(user_list)

# clear 清空列表
user_chice.clear()
print(user_chice)

# del 删除元素  删除列表  这个变量就消失了
# 1.删除列表
# 2.按照索引删除
# 3.按照切片删除
del user_chice

# 验证变量是存在
try:
    user_chice
except NameError:
    var_exists = False
else:
    var_exists = True
print(var_exists)

# 改
# 按照索引改
user_list[0] = '素还真-风彩铃'
print(user_list)

# 按照切片去改
# 切片方式修改，会是以迭代的方式插入到列表的指定位置，并且列表索引会重新排列
user_list[0:3] = ['无计先生']
user_list[:3] = ['叶小钗','一页书','剑子仙迹','佛剑分说','疏楼龙宿']
user_list[0:3] = '人也好，魂也罢,不过一抹塘荷影'
print(user_list)

# 提示如果加了步长，则修改的索引必须与插入元素一一对应，否则出错
user_list[:15:5] = ['叶小钗','一页书','秦假仙']
print(user_list)

# 查
# 按照索引，切片（步长）
# for 循环遍历
for item in user_list:
    print(item)

# 其他方法

print(user_list.__len__())
print(len(user_list))
print(user_list.count('，'))

# 排序
int_list = [1,3,2,9,8,4,5]
int_list.sort()
print(int_list)
# 反向排序
int_list.sort(reverse=True)
print(int_list)
# 翻转
int_list.reverse()
print(int_list)





