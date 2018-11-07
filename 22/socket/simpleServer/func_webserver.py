#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 10:08
# @Author  : anyux
# @FileName: func_webserver.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
def _index():
    return b'/'
def index():
    return bytes('素还真','utf-8')
def _404():
    return bytes('404 not found','utf-8')
while 1:
    addr,_ = sk.accept()
    data = addr.recv(8096)
    data = str(data).split("\r\n")[0].split()[1]
    print(data)
    addr.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    if data == "/":
        response = _index()
    elif data == "/index":
        response = index()
    else:
        response = _404()
    addr.send(response)
    addr.close()