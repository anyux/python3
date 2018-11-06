#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 14:01
# @Author  : anyux
# @FileName: tcp_client.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket #导入socket 模块

BUFSIZE = 1024 #设置缓冲区大小
ip_port = ('127.0.0.1',8888) #设置ip_port

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #设定地址系统，及套接字类型
res = s.connect(ip_port) #连接服务器

while True:
    msg = input('>>:').strip() #获取用户输入
    if len(msg) == 0:continue #没有输入，则循环
    if msg == 'quit':break #设置退出功能

    s.send(msg.encode('utf-8')) #发送msg
    act_res = s.recv(BUFSIZE) #获取服务端返回值

    print(act_res.decode('gbk'),end='')