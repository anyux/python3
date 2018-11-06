#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 11:50
# @Author  : anyux
# @FileName: tcp_server_02.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import socket #引入socket 模块

sk = socket.socket()
ip_port = ('127.0.0.1',8080)
sk.bind(ip_port)
sk.listen()

conn,addr = sk.accept()

res1 = conn.recv(2)
res2 = conn.recv(10)
print(res1)
print(res2)
conn.close()
sk.close()
