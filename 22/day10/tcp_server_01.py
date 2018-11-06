#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 10:47
# @Author  : anyux
# @FileName: tcp_server_01.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import socket #引入socket 模块

sk = socket.socket() #创建socket实例
ip_port = ('127.0.0.1',8080) #设置ip_port
sk.bind(ip_port) #绑定ip_port
sk.listen() #监听ip_port

conn,addr = sk.accept() #接收客户端连接

while True: #开启对单个客户端的阻塞
    cmd = input('>>>:').strip() #服务端输入命令
    if cmd == 'q': #检测退出指令
        conn.send('q')
        break
    conn.send(cmd.encode('gbk')) #发送命令

    res = conn.recv(1024).decode('gbk') #接收客户端返回值
    print(res) #打印返回结果
conn.close() #关闭客户端链接
sk.close()  #关闭服务端进程

