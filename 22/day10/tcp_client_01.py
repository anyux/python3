#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 10:54
# @Author  : anyux
# @FileName: tcp_client_01.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import socket #导入socket模块
import subprocess #导入subprocess模块

sk = socket.socket() #创建socket实例
ip_port = ('127.0.0.1',8080) #服务端ip_port

sk.connect(ip_port) #连接服务端ip_port

while True: #阻塞当前连接
    res = sk.recv(1024).decode('gbk')
    print("执行的命令是: "+ str(res))
    if res == 'q':
        break
    res = subprocess.Popen(res,shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE
                           )
    err = res.stderr.read()
    out = res.stdout.read()
    sk.send(out)
    sk.send(err)
sk.close()