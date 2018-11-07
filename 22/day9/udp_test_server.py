#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 16:22
# @Author  : anyux
# @FileName: udp_test_server.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket
udp_sk = socket.socket(type=socket.SOCK_DGRAM)   #创建一个服务器的套接字
udp_sk.bind(('127.0.0.1',9000))        #绑定服务器套接字
while True:
    msg,addr = udp_sk.recvfrom(1024)
    print(msg.decode('utf-8','ignore'))
    udp_sk.sendto(b'hi',addr)                 # 对话(接收与发送)
udp_sk.close()                         # 关闭服务器套接字