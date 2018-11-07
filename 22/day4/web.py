#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 20:52
# @Author  : anyux
# @FileName: web.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

import os, datetime, time, socket

welcome_title = '''
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序
    请输入数字编号进行操作
'''
login_dict = {
    'login_status': False,
    'login_user': ''
}
register_file = {
    "file": "register.txt"
}
log_file = {
    "file": "user_info.log"
}

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('223.5.5.5',53))
        ip = s.getsockname()[0]
    finally:
        s.close()
    # print(ip)
    return ip


def write_log(log, info):
    # print('%s %s %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),log,info))
    if not login_dict['login_user']:
        login_dict['login_user'] = get_host_ip()
    if os.path.exists(log_file['file']):
        with open(log, encoding='UTF-8', mode='a') as file_log_a:
            file_log_a.write('\n%s %s 访问了 %s 函数' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), login_dict['login_user'], info))
    else:
        with open(log, encoding='UTF-8', mode='w') as file_log_w:
            file_log_w.write('%s %s 访问了 %s 函数' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), login_dict['login_user'], info))
    with open(log, encoding='UTF-8') as file_log_r:
        for line in file_log_r:
            if info == line:
                print("用户信息写入成功")
                return True


def outer(func):
    def inner():
        if not login_dict['login_status']:
            print("请先登录")
            res = login()
            return res
        else:
            write_log(log_file['file'], func.__name__)
            func()
            time.sleep(0.6)

    return inner


def login():
    if login_dict['login_status']:
        print("你已登录，请不要重复登录")
        return False
    user = input('请输入你的用户名称:').strip()
    passwd = input('请输入你的密码:').strip()
    if not os.path.exists(register_file['file']):
        print("请先注册此用户")
        register()
    else:
        with open(register_file['file'], encoding='utf-8') as file_headle_r:
            for line in file_headle_r:
                # print(line)
                user_info = line.split(',')
                if user == user_info[0] and passwd == user_info[1]:
                    login_dict['login_user'] = user
                    login_dict['login_status'] = True
                    chek_login_status(login_dict)
                    return True
            else:
                print("请先注册此用户")
                register()


# noinspection PyAssignmentToLoopOrWithParameter
def register():
    if login_dict['login_status']:
        print("你已登录，请退出后再次注册用户")
        time.sleep(0.6)
        return False
    i = 1
    print("您正在进行用户注册，\t")
    # print(type(user_info),user_info) 确实返回数据类型为元组
    if not os.path.exists(register_file['file']):
        file = open(register_file['file'], encoding='UTF-8', mode='w')
        file.close()
    while True:
        user = get_user_register_info()
        if i >= 3:
            print("您已重复注册 %s 次，请重新选择你的操作" % i)
            break
        with open(register_file['file'], encoding='utf-8') as file_headle_r:
            for line in file_headle_r:
                # print(line)
                user_info = line.split(',')
                print(user_info)
                if user[0] == user_info[0]:
                    print("用户名已被注册，请更换一个用户名")
                    i += 1
                    break
            else:
                with open(register_file['file'], encoding='utf-8', mode='a') as file_headle_a:
                    file_headle_a.write("\n%s,%s" % (user[0], user[1]))
                with open(register_file['file'], encoding='utf-8') as file_inner_headle_r:
                    for line in file_inner_headle_r:
                        # print(line)
                        user_info = line.split(',')
                        if user[0] == user_info[0] and user[1] == user_info[1]:
                            print("注册成功")
                            login_dict['login_status'] = True
                            login_dict['login_user'] = user[0]
                            chek_login_status(login_dict)
                            return True


@outer
def article():
    print("欢迎进入文章页面")

@outer
def acount():
    print("欢迎进入日记页面")


@outer
def comment():
    print("感谢您的评论")


@outer
def review():
    print("欢迎收藏本页")


def logout():
    login_dict['login_status'] = False
    login_dict['login_user'] = ''
    print("您已成功注销当前用户")
    main()



def quit():
    print("退出程序")
    exit(1)
    pass


# 定义8个元素的字典每个元素匹配一个函数

num_dict = {
    1: login,
    2: register,
    3: article,
    4: acount,
    5: comment,
    6: review,
    7: logout,
    8: quit
}


def main():
    while True:
        print(welcome_title)
        ret = get_input()
        for item in num_dict:
            if item == ret:
                # print("你正的访问的是 %s() 函数" % (num_dict[item].__name__))
                write_log(log_file['file'], num_dict[item].__name__)
                num_dict[item]()



def get_input():
    number = input("请输入数字编号").strip()
    if number.isdigit() and int(number) >= 1 and int(number) <= 8:
        return int(number)
    else:
        print("请输入提示内的数字")
        exit(0)


def get_user_register_info():
    user_name = input("请输入你注册的用户名：").strip()
    user_passwd = input("请输入你注册的密码：").strip()
    if user_name.__len__() == 0 or user_passwd.__len__() == 0:
        print("提示：用户名或密码不能为空")
        exit(1)
    else:
        return user_name, user_passwd


def chek_login_status(login_status):
    if login_dict['login_status']:
        print("你已成功登录")
        return True


main()

