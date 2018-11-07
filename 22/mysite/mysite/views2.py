#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 10:34
# @Author  : anyux
# @FileName: views.py.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import datetime
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render


def anyux(request):
    t = get_template('index.html')
    # return HttpResponse('hello anyux,你好')
def index(request):
    context = {'context':'搞快点'}
    return render(request,'index.html',context)
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now: %s</body></html>" % now
    return HttpResponse(html)
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    assert False
    html = "<html><body>In %s hour(s),it will be %s.</body></html>" %(offset,dt)
    return HttpResponse(html)