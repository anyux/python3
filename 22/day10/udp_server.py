#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 14:56
# @Author  : anyux
# @FileName: udp_server.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from socket import * #导入socket 模块
import subprocess #导入suprocess模块

ip_port = ('127.0.0.1',9000) #设定ip_port
bufsize = 1024 #设置缓冲区大小

udp_server = socket(AF_INET,SOCK_DGRAM) #设置地址系统，及套接字类型
udp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #用于任意类型、任意状态套接口的设置选项值
udp_server.bind(ip_port) #绑定ip_port

while True:
    #收消息
    cmd,addr = udp_server.recvfrom(bufsize) #接收参数
    print('用户命令------>',cmd) #打印用户输入

    #逻辑处理
    res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE
                           )  # 执行命令，并获取返回结果
    stderr = res.stderr.read()  # 获取标准错误
    stdout = res.stdout.read()  # 获取标准输出
    #发消息
    udp_server.sendto(stderr,addr)
    udp_server.sendto(stdout,addr)

udp_server.close()

