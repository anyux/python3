#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/10/29

from socket import *
from time import ctime


while True:
    sk = socket(AF_INET,SOCK_STREAM)
    sk.connect(('127.0.0.1',21567))
    data = input('> ')
    if not data:
        break
    data = (data+'\r\n').encode("utf-8")
    sk.send(data)
    sk.close()



