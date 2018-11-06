#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 11:52
# @Author  : anyux
# @FileName: tcp_client_02.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket #引入socket模块

sk = socket.socket()
ip_port = ('127.0.0.1',8080)
sk.connect(ip_port)

sk.send(b'hello')
sk.send(b'abc')
sk.close()