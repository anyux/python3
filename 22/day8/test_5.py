#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 11:01
# @Author  : anyux
# @FileName: test_5.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import re
import functools

# user = input(">>>请输入要运算的数据:")
str = '1.5 - 2.4 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

def formatInput(str):
    """标准化输入表达式，去除多余空格等"""
    str = str.replace(' ','')
    str = str.replace('++', '+')
    str = str.replace('+-', '-')
    str = str.replace('-+', '-')
    str = str.replace('--', '+')
    return str


def checkInput(str):
    """检测输入合法与否,是否包含字母等非法字符"""
    str = formatInput(str)
    ret = re.search('[^\d+\-*/\.()\s]',str)
    return not ret
def compute(str):
    pass

def calc(str):
    ''' 计算程序入口 '''
    # 检查是否有括号
    has_parenthesise = str.count('(')
    # 检查格式是否正确
    if checkInput(str):
        # 格式化 字符串
        str = formatInput(str)
        while has_parenthesise:
            # 匹配最内层括号
            sub_str = re.search('\([^()]*\)', str)
            if sub_str:
                str = str.replace(sub_str.group(),compute(sub_str.group()[1:-1]))
            else:
                pass
        else:
            print("没有括号了。。。。。")
            has_parenthesise = False
    else:
        exit(1)

calc(str)

import string
