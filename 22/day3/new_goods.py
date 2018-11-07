#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 10:11
# @Author  : anyux
# @FileName: new_goods.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

user_file = 'user_file.txt'
good_file = 'good_file.txt'
is_shop = False
import os


def get_user(error_count=0):
    # check login error_count
    ec = error_count
    if ec >= 3:
        print("你已连续3次登录失败,请重新登录")
        exit()
    # check user_file
    if not os.path.exists(user_file):
        print("ERROR: '%s' No Such file or diceotry" % user_file)
        print("please register ")
        exit()
    user = input('请输入用户名：').strip()
    passwd = input('请输入密码：').strip()
    # read user_file
    user_list = []
    with open(user_file, encoding='UTF-8', mode='r') as get_user_file:
        for item in get_user_file:
            tmp = item.split(' ')
            tmp_user = tmp[0]
            tmp_passwd = tmp[1].replace('\n', '')
            user_list.append([{'name': tmp_user, 'passwd': tmp_passwd}])
        get_user_file.close()
        # check login user and passwd
        print(user_list)
        for item in user_list:
            if user == item[0]['name'] and passwd == item[0]['passwd']:
                global  is_shop
                is_shop = True
                print("登录成功")
                print(is_shop)
            else:
                print("登录失败")
                ec += 1
                get_user(error_count=ec)


def register_user():
    user = input('请输入用户名：').strip()
    passwd = input('请输入密码：').strip()


        #     check user_list from user input
    if os.path.exists(user_file):
        user_list = []
        # get user_file and append to user_list
        with open(user_file, encoding='UTF-8', mode='r') as get_user_file_r:
            for item in get_user_file_r:
                tmp_user = item.split(' ')
                user_list.append(tmp_user[0])
            get_user_file_r.close()
        print(user_list)
        with open(user_file, encoding='UTF-8', mode='a') as get_user_file:
            print(user_list)
            for tmp_user in user_list:
                print('a')
                if user != tmp_user:
                    print('a')
                    get_user_file.write(user + ' ' + passwd + '\n')
                    print("用户名已写入")
                    break
                else:
                    print("用户名冲突，请重新注册")
                    exit()
            get_user_file.close()
    else:
        with open(user_file, encoding='UTF-8', mode='w') as get_user_file:
            get_user_file.write(user + ' ' + passwd + '\n')
            get_user_file.close()


# register_user()
# get_user()

def shop():
    global is_shop
    if not is_shop:
        print("请登录后再购买商品")
        exit()
    user_goods = []
    shopping_continue = 'y'
    goods = [{"name": "电脑", "price": 1999},
             {"name": "鼠标", "price": 10},
             {"name": "游艇", "price": 20},
             {"name": "美女", "price": 998},
             ]

    user_money = input("请输入你的帐户资产:")
    if not user_money.isdigit():
        print("请输入数字")
        exit()
    user_money = int(user_money)
    while True:
        if shopping_continue.lower() == 'n':
            break
        # print goods list
        print("选择下面的商品编号，来购买商品")
        print('商品信息'.center(30, '*'))
        for item in goods:
            print("商品编号%d,商品名称 %s,商品价格 %d" % (goods.index(item) + 1, item['name'], item['price']))
        print('商品信息'.center(30, '*'))
        while True:
            good_number = input("请输入你要购买的商品编号:")
            my_range = []
            for i in range(1, len(goods) + 1):
                my_range.append(i)
            print(my_range)
            if not good_number.isdigit():
                print("请输入只属于商品编号的数字")
                break
            flag = False
            for item in my_range:
                if item == int(good_number):
                    flag = True
            if not flag:
                print("请输入只属于商品编号的数字")
                break
            else:
                good_number = int(good_number)
            if int(goods[good_number - 1]['price']) > user_money:
                print("您的余额不足，不能购买")
                is_add = True

            else:
                tmp_name = goods[good_number - 1]['name']
                tmp_price = goods[good_number - 1]['price']
                print('当前购买商品为:{} 价格为：{} '.format(tmp_name, tmp_price))
                user_money -= tmp_price
                tmp_key_goods = []
                for item in user_goods:
                    tmp_key_goods.append(item['name'])
                if tmp_name in tmp_key_goods:
                    for i in user_goods:
                        if tmp_name == i['name']:
                            i['count'] += 1
                else:
                    user_goods.append({'name': tmp_name, 'price': tmp_price, 'count': 1})
                is_add = False
                # print(user_goods)
            shopping_continue = input("是否继续购买Y/N")
            if shopping_continue.lower() == 'n':
                break
            if is_add:
                shopping = input("是否充值Y/N:")
                if shopping.lower() == 'y':
                    while True:
                        get_money = input("请充值你的帐户资产:")
                        if not get_money.isdigit():
                            print("请输入数字")
                            break
                        user_money += int(get_money)
                        print("你现在资产为：", user_money)
                        get_money_update = input("是否继续充值Y/N:")
                        if get_money_update.lower() == 'n':
                            break
    sum = 0;
    print()
    print("用户商品信息".center(30, '*'))
    print('-' * 30)
    write_line = ''

    for item in user_goods:
        tmp_write_line = "商品名{} 价格{} 数量{} ".format(item['name'], item['price'], item['count'])
        print(tmp_write_line)
        write_line += tmp_write_line + '\n'
    print('-' * 30)
    print("用户商品信息".center(30, '*'))
    print()
    if not os.path.exists(good_file):
        with open(good_file, encoding='UTF-8', mode='w') as good_file_handle:
            good_file_handle.write(write_line)
            good_file_handle.close()
    else:
        with open(good_file, encoding='UTF-8', mode='a') as good_file_handle:
            good_file_handle.write(write_line)
            good_file_handle.close()
    for item in user_goods:
        sum += item['count'] * item['price']
    print("共花费：", sum, "元")
    print("剩余:", user_money, "元")


def main():
    title = '''
请输入以下编码，确定你要执行的动作
1,注册
2，登录
3，购物车。
4,退出
'''
    print(title)
    while True:
        get_titile_number = input('请输入以下编号:').strip()
        if not get_titile_number.isdigit():
            print("请按提示输入正确的数字")
            exit()
        get_titile_number = int(get_titile_number)
        if get_titile_number not in [1, 2, 3]:
            print("请按提示输入正确的数字")
            exit()
        else:
            get_titile_number = int(get_titile_number)
            if get_titile_number == 1:
                register_user()
            elif get_titile_number == 2:
                get_user()
            elif get_titile_number == 3:
                shop()
            elif get_titile_number == 4:
                print("退出")
                exit()
            else:
                print("请输入正确的数字")
                exit()


main()
