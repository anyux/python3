#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3
from django.shortcuts import redirect,render,HttpResponse
from crm.forms.user import UserModelForm
from crm import models
from crm.utils.pager import Pagination

def index(request):
    my_list = models.user.objects.all()
    for item in my_list:
        print(item)
    page = request.GET.get('page', 1)  # 要查看的页码
    total_count = models.user.objects.all().count()  # 数据库中数据总条数
    pager = Pagination(page, total_count, '/crm/user/list/',5)
    my_list = models.user.objects.all()[pager.start:pager.end]
    return render(request,'user_list.html',locals())


def add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request,'user_add.html',locals())
    else:
        print(request.POST)
        form = UserModelForm(data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/crm/user/list/')
        else:
            print(form.errors)
        #     return HttpResponse("。。。")
    return render(request,'user_add.html',{'form':form})


def edit(request,nid):
    '''
    修改操作
    :param request:
    :param nid:  部门id
    :return:
    '''
    obj = models.user.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=obj)
        return render(request,'user_edit.html',locals())

    form = UserModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/user/list/')
    return render(request,'user_edit.html')

def delete(request,nid):
    print(nid)
    models.user.objects.filter(id=nid).delete()
    return redirect('/crm/user/list/')


