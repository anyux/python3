#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 10:18
# @Author  : anyux
# @FileName: super_func_webserver.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
def _index(url):
    return bytes('%s 素还真' % format(url),'utf-8')
def index(url):
    return bytes('%s 素还真' % format(url),'utf-8')
def _404(url):
    return bytes('404 not found','utf-8')

url_partens = [
    ('/',_index),
    ('/index',index),
]

while 1:
    addr,_ = sk.accept()
    data = addr.recv(8096)
    data = str(data).split("\r\n")[0].split()[1]
    print(data)
    addr.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    for i in url_partens:
        print(i)
        if data == i[0]:
            response = i[1](data)
            break
    else:
        response = _404(data)
    addr.send(response)
    addr.close()