#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 15:08
# @Author  : anyux
# @FileName: udp_client.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from socket import *
ip_port = ('127.0.0.1',9000)
bufsize = 1024

udp_client = socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input('>>:').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    err,addr = udp_client.recvfrom(bufsize)
    out,addr = udp_client.recvfrom(bufsize)
    if err:
        try:
            print('error: %s' %err.decode('utf-8'),end='')
        except:
            print('error: %s' %err.decode('gbk'),end='')
    if out:
        try:
            print(out.decode('gbk'),end='')
        except:
            print(out.decode('utf-8'),end='')




