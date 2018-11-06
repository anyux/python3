#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.conf.urls import url,include
from crm.views import home
from crm.views import depart
from crm.views import user


urlpatterns = [
    url(r'^index/',home.index),
    url(r'^depart_list/',depart.index),
    url(r'^depart/list/',depart.index),
    url(r'^depart/add/',depart.add),
    url(r'^depart/del/(\d)/$',depart.delete),
    url(r'^depart/edit/(\d)/$',depart.edit),
    url(r'^user_list/',user.index),
    url(r'^user/list/',user.index),
    url(r'^user/add/',user.add),
    url(r'^user/del/(\d)/$',user.delete),
    url(r'^user/edit/(\d)/$',user.edit),
]
