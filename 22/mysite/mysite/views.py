#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:34
# @Author  : anyux
# @FileName: views.py.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import pymysql
from django.shortcuts import render_to_response


def index(request):
    context = '搞快点'
    mylist = range(10)
    return render_to_response('index.html',locals())
def current_datetime(request):
    db = pymysql.connect(host='localhost',user='root',password='',database='mysql')
    cursor = db.cursor()
    cursor.execute('SELECT user FROM user')
    users = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('time/current_datetime.html',locals())
# def hours_ahead(request,offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
#     assert False
#     html = "<html><body>In %s hour(s),it will be %s.</body></html>" %(offset,dt)
#     return HttpResponse(html)