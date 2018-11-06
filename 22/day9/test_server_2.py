#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 18:31
# @Author  : anyux
# @FileName: test_server_2.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import struct
import socket

sk = socket.socket()

sk.bind(('127.0.0.1',8090))
sk.listen(1)

conn,addr = sk.accept()

a = input('>>>').encode('utf-8')
b = input('>>>').encode('utf-8')

lena = struct.pack('i',len(a))
lenb = struct.pack('i',len(b))

conn.send(lena+a)
conn.send(lenb+b)
conn.close()
sk.close()
