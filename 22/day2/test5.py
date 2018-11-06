#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 14:07
# @Author  : anyux
# @FileName: test5.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

user_dict = {
    'name_list':['素还真','叶小钗'],
    1:{
        'age':180,
        'height':180
    }
}

# 向 user_dict['name_list']中追加一个元素'一页书'
user_dict['name_list'].append('一页书')
for k,v in user_dict.items():
    print(k,v)
# 向user_dict[1] 添加键值对 'sex':'man'
user_dict[1].setdefault('sex','man')
for k,v in user_dict.items():
    print(k,v)

int_list = [11,22,33,44,55]
# 将索引为奇数对应的元素删除
del int_list[1:-1:2]
print(int_list)

# 提示，在循环一个列表时，不要改列表的大小，这样会影响结果
int_list = [11,22,33,44,55]
for i in range(0,len(int_list)+1):
    if i % 2 == 0:
        print(int_list[i])
# 反向思维，从后向前删除元素，不会影响元素顺序，非常规用法
int_list = [11,22,33,44,55]
# range(4,-1,-1) 相当于数学区间[4,-1)表明可以取到的值为 4-0，即可以取到的索引值
print(range(len(int_list)-1,-1,-1))

for i in range(len(int_list)-1,-1,-1):
    if i % 2 == 1:
        del int_list[i]
print(int_list)

# dictionary changed size during iteration
# 在循环一个字典时，不要改变字典的大小，这样的影响结果或报错
# 删除dic 字典中包含k的键名
dic = {'k1': 'v1', 'k2': 'v2', 'k3':'v3', 'name':'素还真'}
for key in list(dic.keys()):
    if 'k' in key:
        del dic[key]
print(dic)

dic = dict.fromkeys('abc','666')
print(dic)
dic['a'] = '777'
print(dic)
dic = dict.fromkeys('abc',[])
print(dic)
dic['a'] = 'bbb'
print(dic)
dic['c'].append('888')
print(dic)

