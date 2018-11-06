#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 16:23
# @Author  : anyux
# @FileName: udp_test_client.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket
ip_port=('127.0.0.1',9000)
udp_sk=socket.socket(type=socket.SOCK_DGRAM)
str = '我是你姐夫'
bb = str.encode('utf-8')
udp_sk.sendto(b'hello,' + bb,ip_port)
back_msg,addr=udp_sk.recvfrom(1024)
print(back_msg.decode('utf-8'),addr)