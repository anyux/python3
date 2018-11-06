#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 10:28
# @Author  : anyux
# @FileName: TservSS.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''; PORT = 21567; ADDR = (HOST,PORT);

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:',self.client_address)
        # self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))
        self.wfile.write(b'1234\r\n')

tcpServ = TCP(ADDR,MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()


