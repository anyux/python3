#!/usr/bin/env python
# -*- conding:utf-8 -*-
alert = "欢迎致电10086"
message1 = "查询话费"
message2 = "查水表"
message3 = "人工服务"
msg = """
{}
			1. {}
			2. {}
			3. {}
			""" .format(alert,message1,message2,message3)
print(msg)
choice = input("请输入你要使用的服务")
if choice == "1":
    print("1.查询本机 2.查询他人手机 3.查询座机")
    select = input("请输入你要查询的业务")
    if select == "1":
        print("查询本机")
    elif select == "2":
        print("查询他人手机")
    elif select == "3":
        print("查询座机")
    else:
        print("输入错误")
elif choice == "2":
    print("查水表")
elif choice == "3":
    print("人工服务")
else:
    print("输入错误")
