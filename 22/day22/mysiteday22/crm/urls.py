#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.conf.urls import url,include
from django.contrib import admin
from crm.views import home

urlpatterns= [
    url(r'index/', home.index),
]