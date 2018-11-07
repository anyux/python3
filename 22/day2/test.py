#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/12 9:56
# @Author  : anyux
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# 字典基于二分查找 可hash的内容
# 切片
# print(user_dict["desc"][:])
# print(user_dict['desc'][:5])
# print(user_dict['desc'][:15:2])
# print(user_dict['desc'][-1:-15:-2])
# print(bool('0'))
# print(bool(''))
# print(bool(int('0')))

# list = ['1','2','3']
# print(list[1:2],type(list[1:2]))

'''
list = ['三余无梦生','天踦爵','鷇音子','解锋镝']

# append追加到列表末尾
list.append('四智武童')
# 指定索引增加
list.insert(5,'千叶传奇')
# 指定索引删除,返回删除元素
# extend() 通过迭代对象，追加到列表末尾
list.extend(['叶小钗','一页书','叶途灵'])
print(list.pop(5))
# 按元素值删除
list.remove('四智武童')
# del 删除
#   按索引删除
#   按切片删除
#   删除整个列表,这个列表就消失在内存中
# del list[3]
# del list[1:2]
# del list
#  clear() 列表改为空列表
# list.clear()

# list[0] = '末世妖莲'
list[0] = '末世妖莲'
# 切片修改
list[:1] = ['三余无梦生','素还真']

# index 返回索引
# print(list.index('素还真'))

# sort 排序 正向排序
list_number = [1,9,3,7,5,8]
list_number.sort()
print(list_number)
# sort(reverse=True) 反向排序
list_number.sort(reverse=True)
print(list_number)

# 列表首尾反转
list.reverse()
# count 统计列表元素数量
# print(list.__len__())
# print(len(list))
# print(list.count('素还真'))

for item in list:
    print(item)
print(list)
'''

'''
list = [1,2,'alex',['wusir','99'],3]
list[2] = list[2].title()
list[2] = list[2].capitalize()
list[3][0] = list[3][0].upper()
list[3][1] = str(int(list[3][1])+1)
print(list)
list = [1,2,3,4,5]
for item in range(0,len(list)):
    print(item)

# print("this is a title".title())
# print("this is a title".capitalize())
'''

user_dict = {"name":"天踦爵","age":18,"desc":"三年寻龙，十年点穴,肩负青囊走南北,三寸知心，十面洞心,掌握乾坤通天阙"}

# 增
user_dict['title'] = '齐烟九点'
user_dict.setdefault('title','遥望齐州九点烟,一泓海水杯中泻')
# 删除 clear 清空列表
# user_dict.clear()
# user_dict.pop('title')
# user_dict.popitem()
# del
# 删除列表元素
# 删除列表
# del user_dict['title']
# del user_dict

# 查询
# print(user_dict.get('name'))
# print(user_dict.get('name1','素还真'))

# print(user_dict.keys())
# print(user_dict.values())
# print(user_dict.items())
# for item in user_dict.items():
#     print(item)
# for k,v in user_dict.items():
#     print(k,v)
# print(user_dict)

user_dict = {
    'name_list':['三余无梦生','天踦爵'],
    1:{
        'name':'素还真',
        'height':185,
    }
}

# print(user_dict)
user_dict['name_list'].insert(2,'鷇音子')
user_dict[1].setdefault('desc','看莽莽红尘,谁将韶光偷换,人也罢，魂也好,不过是一抹塘荷影')
# print(type(user_dict))
'''
for item in user_dict:
    if type(user_dict[item]) == "<class 'user_dict'>":
        for i in item:
            print(i,item(i))
    elif type(user_dict[item]) == "<class 'user_dict'>":
        for i in item:
            print(i)
    else:
        print(item)

list = [11,22,33,44,55]
for i in range(0,len(list),2):
    print(list[i])

for i in list:
    if int(list.index(i))%2 == 0:
        print(i)
dic = {'k1': 'v1', 'k2': 'v2', 'k3':'v3', 'name':'alex'}
for item in tuple(dic):
    if 'k' in item:
        del dic[item]
print(dic)

'''

boy = '素还真'
girl = "风采铃"
msg = "半神半圣亦半仙,全儒全道是全贤,脑中真书藏万卷,掌握文武半边天."

#list 列表存储大量的数据。
list_user=["业火红莲",'风莲','墨渊水莲','三莲归真','正官赐福','天踦爵','三余无梦生','鷇音子','解锋镝']
#tuple 只读列表
tuple_user = ("业火红莲",'风莲','墨渊水莲','三莲归真','天官赐福','天踦爵','三余无梦生','鷇音子','解锋镝')

# user_dict 字典 查询速度快，存储的是关系型数据
user_dict_user = {
    'name':"素还真",
    'age':180,
    'title':"半神半圣亦半仙,全儒全道是全贤,脑中真书藏万卷,掌握文武半边天",
}
set = {1,2,3}

# msg ='''
# 半神半圣亦半仙，
# 全儒全道是全贤。
# 脑中真书藏万卷，
# 掌握文武半边天
# '''
# print(msg)

# boy = '素还真'
# girl = '风彩铃'
# print(boy + ' ' + girl)

# # 字符串批量打印
# title_time = '看莽莽红尘，谁将韶光偷换，人也好，魂也罢，不过是一抹塘荷影\n'
# print(title_time*8)

# 打印第一个字符
# title = '玄歌浪蹈，幻中道真，太游方外睨红尘。'
# title_first = title[0]
# print(title_first,type(title_first))
# print(title[-1])

# #切片 格式为：[0:3],类似数学中的区间，数学形式为[0,3) #取值范围是>=0 <3
# title = '非吾小天下，才高而已；非吾纵古今，时赋而已；非吾睨九州，宏观而已；三非焉罪？无梦至胜。'
# print(title[0:3])
# # 提示：如果字符取值想从末尾开始，需要使用-1,并且步长也需要使用负数表示
# print(title[-1:-5:-1])
# # 反向打印字符
# print(title[-1::-1])

title = 'Today,I consider myself the luckiest man on the face of the earth. 现在,我想我是这个世界上最幸运的人。(《扬基的骄傲》'
# ** capitalize 首字母大写其余字母小写
print(title.capitalize())
# 大小写反转
print(title.swapcase())
# 非字母隔开的每个单词的首字母大写
print(title.capitalize().title())
# center 设置总长度，并居中
print(title.center(190,'*'))
# upper() lower() 全部大写，全部小写
print(title.upper())
print(title.lower())

# 使用upper(),lower()可以用于常规验证码对比
code = 'QwErDf'
input_code = input("请输入验证码:")
if input_code.lower() == code.lower():
    print("验证成功")
else:
    print("验证失败")

# startswith 以什么开头 endswith 以什么结尾 返回布尔值
title = '时间从来只留恨，不留人'
print(title.startswith("时间"))
print(title.endswith('人'))

# strip 默认删除字符串左右两侧的空格，换行符，制表符
# lstrip 删除左侧空格
# rstrip 删除右侧空格
title = '    吾用一生,写一首诗,盲目寻添,只找一字,直至此刻,诗成一字,早已铭心。    '
print(title.strip())
print(title.lstrip())
print(title.rstrip())

#适用场景，用于用户输入内容时，删除误操作产生的空格
user_name = input("请回答霹雳主角的名字").strip() #输入内容：    素还真
if user_name == "素还真":
    print("回答正确")
else:
    print('回答错误')

# replace 替换 replace("源字符串","目标字符串",[替换次数])
title = '初遇倾心，再见痴心，用尽苦心，不顾良心，终生费心，欲得芳心，难道你心，不懂孤心？'
print(title.replace("心","情",3))
print(title.replace("心","情"))

# split 分隔，str --> list 字符串 转 列表 默认以空格分隔
# split 语法格式 split(分隔字符[,分隔次数])
title = '初遇倾心，再见痴心，用尽苦心，不顾良心，终生费心，欲得芳心，难道你心，不懂孤心？'
list_title = title.split('，')
list_title = title.split('，',2)
print(list_title)
# join list --> str 列表 转 字符串
print(','.join(list_title))

# 通过元素找索引 找多个字符，以第一个找到的字符索引为标记
# find 找不到返回 -1 find(目标字符串[,开始查找索引位置])
# index 找不到会报错  index(目标字符串[,开始查找索引位置])

title = '人心最可怕的，不是无情，而是利用感情'
print(title.find('人'))
print(title.find('可怕'))
print(title.find('情',15))
print(title.index('人'))
print(title.index('可怕'))
print(title.index('情',15))

# format 三种格式化打印方式
# 第一种用法
user = "{},{},{}"
user_print = user.format('三年寻龙，十年点穴，肩负青囊走南北;三寸知心,十面洞息,掌握乾坤通天阙','齐烟九点-天踦爵','名称来源,遥望齐州九点烟，一泓海水杯中泻')
print(user_print)
# 第二种用法
title = '{0}神{0}圣亦{0}仙,{1}儒{1}道是{1}贤,脑中真书藏万卷,掌握文武{2}'
user_title = title.format('半','全','半边天')
print(user_title)
# 第三种用法
title = '{first}？{second}，{thrid}'
user_title = title.format(first='冷灯看剑，剑上几番功名',second='炉香无需计苍生，纵一川烟逝',thrid='万丈云埋，孤阳还照古陵')
print(user_title)

# 公共方法
# len 测量字符个数
# count 统计某个字符（串）出现的次数
title = '多情楼上月徘徊，独照离人妆镜台。皎皎空中霜色影，凛如寒魄绝尘埃'
print(len(title))
print(title.count('皎'))

# 判断数字或数字,返回布尔值
# isalnum 字符串由字母或数字组成
# isalpha 字符串由字母组成
# isdigit 字符串由数字组成
user_int = '123'
print(user_int.isalnum())
print(user_int.isalpha())
print(user_int.isdigit())

# 数据类型转换
# str ---> int 字符串全部由数字组成 int('123')
# int ---> str str(1)
# int ---> bool 0--->False 非0 --->True bool(1)
print(bool(100))
print(bool(-1))
print(bool(0))
# bool --> int True 1 False 0
print(int(True))
print(int(False))
# str ---> bool 非空True 空字符串 False
print(bool(''))
print(bool('素还真'))
# bool ---> str
print(str(True),type(str(True)))

# str ---> list split
# list ---> str jion

