#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 15:35
# @Author  : anyux
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from socket import *
# 生成socket实例对象
sock = socket(AF_INET,SOCK_STREAM)
# 绑定ip和端口
sock.bind(('localhost',8001))
# 监听
sock.listen()

# 死循环，等待用户链接
while True:
    # 获取用户链接
    conn,_ = sock.accept()
    # 接收客户端发来消息
    data = conn.recv(8096)
    # 把收到的数据转换成字符类型
    str_data = str(data,encoding='utf-8') #bytes("str",encoding="utf-8")
    # 根据http协议 以\r\n分割字符串
    str_data = str_data.split('\r\n')
    # 获取请求的url段
    url_path = str_data[0].split(' ')[1]
    print(url_path)
    # 发送http协议头
    conn.send(b'http/1.1 200 ok \r\n content-type:text/html;\r\n charset:gbk\r\n\r\n')
    # 发送实例内容
    if url_path == "/abc":
        conn.send(bytes('<head><meta charset=utf-8></head>素还真',encoding='utf-8'))
        conn.send(bytes('素还真',encoding='utf-8'))
    print('素还真')
    conn.send(b'123')
    # 关闭链接
    conn.close()

# 关闭 服务
