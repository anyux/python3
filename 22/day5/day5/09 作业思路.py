#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
id，name，age，phone，job
1,Alex,22,13651054608,IT
2,Egon,23,13304320533,Tearcher
3,nezha,25,1333235322,IT
'''
def get_id():
    """始终获得最后一个id 动态记录到一个文件中"""
    pass

def add():
    """输入name，age，phone，job信息，写入文件"""

    pass

def pop():
    """只要输入id 删除整条，两个情况：删除最后一条id 删除非最后一个条"""
    pass

def update():
    pass

list_name = ['id', 'name','age', 'phone', 'job']
condiction = ['>', "<", '=' 'like']
def check():
    """
    select name, age where age>22
    select * where job=IT
    select * where phone like 133
    利用where 分隔：age > 22
    利用select分隔：单行， 多行name, age  全部*
    循环 文件句柄
        筛选出符合条件 每行
    :return:
    """
    pass

while True:
    print('''
    1,增加员工信息，
    2，删除员工信息,
    .....
    
    ''')