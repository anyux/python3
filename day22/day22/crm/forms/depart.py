#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/3

from django.forms import ModelForm
from django import forms
from crm import models

class DepartModelForm(ModelForm):

    class Meta:
        model = models.depart
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control","placeholder":"部门名称"})
        }
        error_messages = {
            'title':{
                'required':'部门名称不能为空'
            }
        }

