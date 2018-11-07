#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.shortcuts import redirect,render,HttpResponse
from crm.forms.depart import DepartModelForm
from crm import models
from crm.utils.pager import Pagination

def index(request):
    # my_list = models.depart.objects.all()
    page = request.GET.get('page', 1)  # 要查看的页码
    total_count = models.depart.objects.all().count()  # 数据库中数据总条数
    pager = Pagination(page, total_count, '/crm/depart/list/',5)
    my_list = models.depart.objects.all()[pager.start:pager.end]
    return render(request,'depart_list.html',locals())


def add(request):
    if request.method == "GET":
        form = DepartModelForm()
        return render(request,'depart_add.html',locals())
    else:
        form = DepartModelForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('/crm/depart/list/')
    return render(request,'depart_add.html',locals())


def edit(request,nid):
    '''
    修改操作
    :param request:
    :param nid:  部门id
    :return:
    '''
    obj = models.depart.objects.filter(id=nid).first()
    if request.method == "GET":
        form = DepartModelForm(instance=obj)
        return render(request,'depart_edit.html',locals())

    form = DepartModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list/')
    return render(request,'depart_edit.html')

def delete(request,nid):
    models.depart.objects.filter(id=nid).delete()
    return redirect('/crm/depart/list/')

