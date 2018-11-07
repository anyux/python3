#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 10:39
# @Author  : anyux
# @FileName: test_7.py.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import os
import sys

class Base:
    def __getitem__(self,item):
        return self.__dict__[item]

class School(Base):
    '''学校类：所在地区 学校名'''
    def __init__(self,address,name):
        self.address = address
        self.name = name

class Teacher(Base):
    ''' 教师类： 名称，课程，班级 权限'''
    def __init__(self,name,course,classes,passwd,cardid=1):
        self.name = name
        self.course = course
        self.classes = classes
        self.passwd = passwd
        self.cardid = cardid
class Course(Base):
    ''' 课程类：名称，价格，周期，校区，教师 '''
    def __init__(self,name,price,cycle,address,teacher):
        self.name = name
        self.price = price
        self.cycle = cycle
        self.address = address
        self.teacher =teacher
    def __getitem__(self,item):
        return self.__dict__[item]

class Admin(Base):
    ''' 管理员：名称，密码，权限 '''
    def __init__(self,name,passwd,cardid=0):
        self.name = name
        self. passwd = passwd
        self. cardid = cardid

class Student(Base):
    ''' 学生类： 名称，密码，班级 权限'''
    def __init__(self,name,passwd,course,cardid=2):
        self.name = name
        self.passwd = passwd
        self.course = course
        self.cardid = cardid

class Classes(Base):
    ''' 班级类：班级名，课程名称 '''
    def __init__(self,name,course):
        self.name = name
        self.course = course

class Manage:
    def create_school(self):
        name = input("请输入学校名称").strip()
        address = input("请输入学校地址").strip()
        school = School(address,name)
        Save.save_school(name,address)
        return school

    def create_teacher(self):
        name = input("请输入教师名称").strip()
        Save.print_school()
        school = input("请输入学校名称").strip()
        teacher = Teacher(name,school)
        Save.save_teacher(name,school)

        return teacher

    def create_course(self):
        name = input("请输入课程名称").strip()
        price = input("请输入课程价格").strip()
        cycle = input("请输入课程周期").strip()
        address = input("请输入所在校区").strip()
        teacher = input("请输入教师名称").strip()
        course = Course(name,price,cycle,address,teacher)
        Save.save_course(name,price,cycle,address,teacher)
        return course

    def create_admin(self):
        name = input("请输入管理员名称").strip()
        passwd = input("请输入管理员密码").strip()
        admin = Admin(name,passwd)

    def create_student(self):
        name = input("请输入学员名称").strip()
        passwd = input("请输入学员密码").strip()
        # 读取课程名称
        Save.print_course()
        course = input("请输入课程名称").strip()
        student = Student(name,passwd,course)
        return student

    def create_classes(self):
        name = input("请输入班级编号").strip()
        # 读取课程名称
        Save.print_course()
        course = input("请输入关联的课程名称").strip()
        classes = Classes(name,course)
        Save.save_classes(name,course)
        return classes



class Save:
    save_school_file = "school_file.txt"
    save_course_file = "course_file.txt"
    save_student_file = "student_file.txt"
    save_classes_file = "classes_file.txt"

    @staticmethod
    def save_school(name, address):
        name = name
        address = address
        if os.path.exists(Save.save_school_file):
            with open(Save.save_school_file, encoding='utf-8', mode='a') as file_h:
                file_h.writelines("%s %s" % (name, address))
        else:
            with open(Save.save_school_file, encoding='utf-8', mode='w') as file_h:
                file_h.writelines("%s %s" % (name, address))
            return 0

    @staticmethod
    def save_course(name, price, cycle, address, teacher):
        if os.path.exists(Save.save_course_file):
            with open(Save.save_course_file, encoding='utf-8', mode='a') as file_h:
                file_h.writelines("%s %s %s %s %s " % (name, price, cycle, address, teacher))
        else:
            with open(Save.save_course_file, encoding='utf-8', mode='w') as file_h:
                file_h.writelines("%s %s %s %s %s " % (name, price, cycle, address, teacher))
        return 0

    @staticmethod
    def save_student(name,passwd,course):
        if os.path.exists(Save.save_student_file):
            with open(Save.save_student_file, encoding='utf-8', mode='a') as file_h:
                file_h.writelines("%s %s %s" % (name,passwd,course))
        else:
            with open(Save.save_student_file, encoding='utf-8', mode='w') as file_h:
                file_h.writelines("%s %s %s" % (name,passwd,course))
        return 0

    @staticmethod
    def save_classes(name,course):
        if os.path.exists(Save.save_student_file):
            with open(Save.save_student_file, encoding='utf-8', mode='a') as file_h:
                file_h.writelines("%s %s" % (name,course))
        else:
            with open(Save.save_student_file, encoding='utf-8', mode='w') as file_h:
                file_h.writelines("%s %s" % (name,course))
        return 0
    @staticmethod
    def save_teacher(name,school):
        if os.path.exists(Save.save_teacher_file):
            with open(Save.save_teacher_file, encoding='utf-8', mode='a') as file_h:
                file_h.writelines("%s %s" % (name,school))
        else:
            with open(Save.save_teacher_file, encoding='utf-8', mode='w') as file_h:
                file_h.writelines("%s %s" % (name,school))
        return 0
    @staticmethod
    def print_course():
        if os.path.exists(Save.save_course_file):
            with open(Save.save_course_file, encoding='utf-8', mode='r') as file_h:
                for line in file_h:
                    print(line)
        else:
            print("课程文件不存在，请添加课程文件")
            exit(1)
        return 0
    @staticmethod
    def print_school():
        if os.path.exists(Save.save_course_file):
            with open(Save.save_school_file, encoding='utf-8', mode='r') as file_h:
                for line in file_h:
                    print(line)
        else:
            print("学校文件不存在，请添加学校文件")
            exit(1)
        return 0



# 初始化信息
manage = Manage()


# '''
# # 创建学校
# manage = Manage()
# school = manage.create_school()
# print(school['address'],school['name'])
# '''
'''
创建课程
course = manage.create_course()
print(course['name'],course['price'],course['cycle'],course['cycle'],course['teacher'])
'''
'''
# 创建班级
classes = manage.create_classes()
print(classes['name'],classes['course'])
'''

