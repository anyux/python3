#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 10:41
# @Author  : anyux
# @FileName: html_webserver.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen()


def _index(url):
    with open('_index.html', 'rb') as f:
        res = f.read()
    return res


def index(url):
    with open('index.html', 'rb') as f:
        res = f.read()
    return res


def _404(url):
    with open('404.html', 'rb') as f:
        res = f.read()
    return res


url_partens = [
    ('/', _index),
    ('/index', index),
]

while 1:
    addr, _ = sk.accept()
    data = addr.recv(8096)
    data = str(data).split("\r\n")[0].split()[1]
    addr.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    for i in url_partens:
        print(i)
        if data == i[0]:
            response = i[1](data)
            break
    else:
        response = _404(data)
    addr.send(response)
    # addr.close()
