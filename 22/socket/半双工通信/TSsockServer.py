#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/10/29

from socket import *
from time import ctime

sk = socket(AF_INET,SOCK_STREAM)
sk.bind(('127.0.0.1',21567))
sk.listen()

while True:
    addr,_ = sk.accept()

    data = addr.recv(8064)
    data = str(data)
    print(data)
    if not data:
        break
    new_data = bytes(data + ctime(),'utf-8')
    addr.send(new_data)
    addr.close()
sk.close()


