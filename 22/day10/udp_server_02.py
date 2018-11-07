#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 15:05
# @Author  : anyux
# @FileName: udp_server_02.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket #引入socket模块

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8080)
sk.bind(ip_port)

while True:
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    print(addr)
    msg = input(">>>")
    sk.sendto(msg.encode('utf-8'),addr)
sk.close()