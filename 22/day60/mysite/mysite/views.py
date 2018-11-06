#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 10:45
# @Author  : anyux
# @FileName: views.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
from django.shortcuts import HttpResponse,render,redirect
def index(request):
    return render(request,"index.html")
def weibo(request):
    return HttpResponse("叶小钗")
def login(request):
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get('email',None)
        pwd = request.POST.get('pwd',None)
        if email == "1@1" and pwd == "1":
            return redirect("http://www.baidu.com/s?wd=素还真")
        else:
            error_msg = "邮箱或密码错误"
    return render(request,"login.html",{"error_msg":error_msg})

