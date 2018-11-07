#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 18:35
# @Author  : anyux
# @FileName: test_client_2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import struct
import socket

sk = socket.socket()

sk.connect(('127.0.0.1',8090))

num = struct.unpack('i',sk.recv(4))[0]
print(sk.recv(num).decode('utf-8'))

num = struct.unpack('i',sk.recv(4))[0]
print(sk.recv(num).decode('utf-8'))

sk.close()

