#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 15:46
# @Author  : anyux
# @FileName: test_client.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import socket
sk = socket.socket()           # 创建客户套接字

sk.connect(('127.0.0.1', 8080))  # 尝试连接服务器
sk.send(b'hello!')
ret = sk.recv(1024)  # 对话(发送/接收)
print(ret)
sk.close()  # 关闭客户套接字
