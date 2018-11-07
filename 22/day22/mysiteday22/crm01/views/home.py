#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.shortcuts import HttpResponse,redirect,render

def index(request):
    # return HttpResponse("素还真")
    return redirect(request,'index.html')
