#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 10:48
# @Author  : anyux
# @FileName: Tclntss.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from socket import *

HOST = 'localhost'; PORT = 21567; BUFSIZ = 1024 ; ADDR = (HOST,PORT)

while True:
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    # print(data)
    if not data:
        break
    tcpCliSock.send((data+'\r\n').encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()


