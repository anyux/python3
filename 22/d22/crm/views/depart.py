#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.shortcuts import HttpResponse,redirect



def depart_list(request):
    return redirect(request,'depart_list.html')
