#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 9:51
# @Author  : anyux
# @FileName: url_webserver.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket
sk = socket.socket()

sk.bind(('127.0.0.1',8000))
sk.listen()

while 1:
    addr,_ = sk.accept()
    data = str(addr.recv(8096),"utf-8")
    # print(data)
    url_path = data.split('\r\n')[0].split()[1]
    print(url_path)
    addr.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    if url_path == "/index":
        response = (bytes('<h1>素还真 index</h1>',encoding='utf-8'))
    elif url_path == "/weibo":
        response = (bytes('<h1>微薄 index</h1>',encoding='utf-8'))
    else:
        response = (bytes('<h1>404 not found</h1>',encoding='utf-8'))
    addr.send(response)
    addr.close()
sk.close()
