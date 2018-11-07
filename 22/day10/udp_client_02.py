#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 15:07
# @Author  : anyux
# @FileName: udp_client_02.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket #导入socket 模块

sk = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8080)
msg='cc'
while True:
    sk.sendto(msg.encode('utf-8'),ip_port)
    res,addr = sk.recvfrom(1024)
    print(res.decode('utf-8'))
    msg = input(">>>:")
sk.close()

