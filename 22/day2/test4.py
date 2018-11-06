#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 11:07
# @Author  : anyux
# @FileName: test4.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

user_dict = {
    'name':'素还真',
    'age':'180',
    'desc':'半神半圣亦半仙,全儒全道是全贤。脑中真书藏万卷,掌握文武半边天'
}

# 增
user_dict['hobby'] = '风彩铃'
print(user_dict)
# setdefault 有key 则不修改，无key则添加
user_dict.setdefault('hobby','素续缘')
print(user_dict)

# 随机删除 popitem 有返回值
ret = user_dict.popitem()
print(ret)
print(user_dict)

# clear 清空字典
user_dict.clear()

# del 删除字典
# 1,删除整个字典
# 2，按照键去删除键值对

del user_dict
try:
    user_dict
except NameError:
    user_dict_exit = False
else:
    user_dict_exit = True
print(user_dict_exit)

user_dict = {
    'name':'素还真',
    'age':'180',
    'desc':'半神半圣亦半仙,全儒全道是全贤。脑中真书藏万卷,掌握文武半边天'
}
new_user_dict = {
    'name':'三余无梦生',
    'age':180,
    'student':['小鬼头','小狐','灵凶','奉丹']
}
# 改
user_dict['age'] = 200
print(user_dict['age'])

# update 更新字典
user_dict.update(new_user_dict)
print(user_dict)

# 查
print(user_dict.get('name','未找到这个键名'))
print(user_dict.keys())
print(user_dict.values())
# 下面两个操作等价
for item in user_dict.keys():
    print(item)
for item in user_dict:
    print(item)

print(user_dict.items())

# 分别赋值
a,b = 1,3
print(a,b)
a,b = [22,33]
print(a,b)
for k,v in user_dict.items():
    print(k,v)
