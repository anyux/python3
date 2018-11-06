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
def shz(url):
    res = '素还真'
    return bytes(res,encoding='utf-8')
def yxc(url):
    res = '叶小钗'
    return bytes(res,encoding='utf-8')
def f404(url):
    res = '404 not found <hr>'
    return bytes(res,encoding='utf-8')
url_func = [
    ('/shz',shz),
    ('/yxc',yxc),
]
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
    # print(url_path)
    # 发送http协议头
    conn.send(b'http/1.1 200 ok \r\n content-type:text/html;\r\n charset:gbk\r\n\r\n')
    # 通过列表元组对比url
    for i in url_func:
        if i[0] in url_path:
            # 赋值函数名
            func = i[1]
            break
    else:
            # 没有找到对应url,执行f404函数
            func = f404
    # 获取bytes类型
    response = func(url_path)
    # 设置html字符编码
    conn.send(bytes('<head><meta charset=utf-8></head>',encoding='utf-8'))
    # 发送html内容
    conn.send(response)
    # 关闭链接
    conn.close()

# 关闭 服务
