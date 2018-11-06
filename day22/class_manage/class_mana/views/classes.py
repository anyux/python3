#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/6

from django.shortcuts import redirect,render,HttpResponse

def index(request):

    return HttpResponse("素还真")
