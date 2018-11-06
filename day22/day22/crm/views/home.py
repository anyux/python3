#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.shortcuts import redirect,render

def index(request):
    return render(request,'index.html')
