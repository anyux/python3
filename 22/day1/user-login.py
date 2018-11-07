#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 9:32
# @Author  : anyux
# @FileName: user-login.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

# 用户登录（三次错误机会）

user_list = [
    {'username': 'alex', 'password': '123'},
    {'username': 'eric', 'password': '123'},
    {'username': 'tony', 'password': '123'},
    {'username': 'oldboy', 'password': '123'},
]

flag = False #用户状态
i = 0 #登录阀值
while flag == False:
    user_name = input("请输入你的用户名：")
    user_pass = input("请输入你的密码：")
    for item in user_list:
        if item['username'] == user_name and item['password'] == user_pass:
            flag = True
    if flag == True:
        print("登录成功")
        break
    elif i == 2:
        print("登录失败")
        break
    else:
        i+=1
        print("您输入的帐号或密码不正确，您还有{}次机会".format( 3 - i))
