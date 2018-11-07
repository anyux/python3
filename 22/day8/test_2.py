#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 9:04
# @Author  : anyux
# @FileName: test_2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# '1 - 2 * ( (60-30 +-8 * 1024) - (-4*3)/ (16-3*2) )'
# while 循环
# 从这个字符串中先匹配出一个小括号
# 这个小括号里面不再有新的小括号了
# 从左到右依次匹配 乘除法
# '7.4*3'
# 首先要判断一下是除法还是乘法
# 21

import re

str = '1 - 2 * ( (60-30 +-8 * 1024) - (-4*3)/ (16-3*2) )'
str = str.replace(' ','')
str = str.replace('+-','-')
str = str.replace('-+','-')
str = str.replace('--','+')

# pattern = '(\d+)*([-+/*])?(\()?(\))?'
pattern = '(\((\w*[-+*/]?)*\))'
ret = re.finditer(pattern,str)
str = next(ret).group()
pattern = '(\d*)([*/])(\d*)'
ret = re.findall(pattern,str)
print(eval(ret[0][0]+ ret[0][1] + ret[0][2]))


# str = ret[4]
# print(str)
# ret = re.findall(pattern,str)
# print(ret)

