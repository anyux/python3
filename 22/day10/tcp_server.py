#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 11:35
# @Author  : anyux
# @FileName: tcp_server.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from socket import *  #导入socket类
import subprocess     #导入subprocess工具

ip_port = ('127.0.0.1',8888) #设定ip_port
BUFSIZE = 1024 #设置缓冲大小

tcp_socket_server = socket(AF_INET,SOCK_STREAM) #设定地址系统，及套接字类型
tcp_socket_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #用于任意类型、任意状态套接口的设置选项值
tcp_socket_server.bind(ip_port) #绑定ip_port
tcp_socket_server.listen(5) #开启监听

while True:
    conn,addr = tcp_socket_server.accept() #接受用户链接
    print('客户端ip地址： ',addr) #打印ip地址

    while True:
        cmd = conn.recv(BUFSIZE) #获取指定缓冲区大小的内容
        if len(cmd) == 0 :break  #没有参数，退出当前循环

        res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE
        ) #执行命令，并获取返回结果

        stderr = res.stderr.read() #获取标准错误
        stdout = res.stdout.read() #获取标准输出

        conn.send(stdout) #发送标准输出
        conn.send(stderr) #发磅标准错误


