#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 15:42
# @Author  : anyux
# @FileName: mysql_webserver.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import time
from wsgiref.simple_server import make_server
from jinja2 import Template
import pymysql
def _index(url):
    with open('mysql_jinjia2.html', 'r',encoding="utf-8") as f:
        res = f.read()
    template = Template(res)
        # res = res.replace("{time}",str(time.time()))
    conn = pymysql.connect(
        host='127.0.0.1',
        port = 3306,
        user = 'root',
        password = '',
        database = "day59",
        charset = "utf8",
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from userinfo")
    userlist = cursor.fetchall()
    # res = template.render({"time":time.time(),"myfirends":myfirends})
    res = template.render({"userlist":userlist})
    return bytes(res,'utf-8')

def index(url):
    with open('index.html', 'rb') as f:
        res = f.read()
    return res


def _404(url):
    with open('404.html', 'rb') as f:
        res = f.read()
    return res


url_partens = [
    ('/', _index),
    ('/index', index),
]

def run_server(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html;charset=utf-8'),])
    url = environ['PATH_INFO']
    func = None
    for i in url_partens:
        if url == i[0]:
            response = i[1](url)
            break
    else:
        response = _404(url)
    return [response,]
def main():
    httpd = make_server('127.0.0.1',8000,run_server)
    print("已启动webserver服务")
    httpd.serve_forever()
if __name__ == "__main__":
    main()