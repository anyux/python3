#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.forms import ModelForm
from django import forms
from crm import models

class UserModelForm(ModelForm):

    class Meta:
        model = models.user
        fields = "__all__"
        widgets = {
            'username': forms.TextInput(attrs={"class":"form-control","placeholder":"名称"}),
            'password': forms.TextInput(attrs={"class":"form-control","placeholder":"密码"}),
            'email': forms.TextInput(attrs={"class":"form-control","placeholder":"邮箱"}),
            'gender': forms.Select(attrs={"class":"form-control","placeholder":"性别"}),
            'depart': forms.Select(attrs={"class":"form-control","placeholder":"部门名称"}),
        }
        error_messages = {
            'username':{
                'required':'用户名称不能为空'
            },
            'password':{
                'required':'密码不能为空'
            },
            'email':{
                'required':'emial格式不正确'
            },
            'gender':{
                'required':'性别不正确'
            },
            'depart':{
                'required':'部门名称不能为空'
            },
       }

