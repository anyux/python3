#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 9:35
# @Author  : anyux
# @FileName: webserver.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket

sk = socket.socket()

sk.bind(('127.0.0.1',8000))
sk.listen()

while 1:
    addr,_ = sk.accept()
    data = addr.recv(8096)
    print(data)
    addr.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    addr.send(bytes('素还真','utf-8'))
    addr.close()
sk.close()