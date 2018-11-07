#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/14 9:58
# @Author  : anyux
# @FileName: goods.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998},
         ]
key_goods = []
is_add = False
for key in goods:
    key_goods.append(key['name'])
# print(key_goods)
user_goods = []
shopping_continue = 'y'
user_money = input("请输入你的帐户资产:")
if not user_money.isdigit():
    print("请输入数字")
while True:
    if shopping_continue.lower() == 'n':
        break
    user_money = int(user_money)
    # print goods info
    print("商品信息".center(30, '*'))
    for item in goods:
        print("商品编号:{}  商品名:{}  价格:{}".format(goods.index(item) + 1, item['name'], item['price']))
    print("商品信息".center(30, '*'))  # user_goods
    # get good_number
    while True:
        if shopping_continue.lower() == 'n':
            break
        good_number = input("请输入你要购买的商品编号:")
        my_range = []
        for i in range(1, len(goods) + 1):
            my_range.append(i)
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
        # print(int(goods[good_number - 1]['price']) > user_money)
        # print(goods[good_number - 1]['price'])
        # print(user_money)
        if int(goods[good_number - 1]['price']) > user_money:
            print("您的余额不足，不能购买")
            is_add = True

        else:
            tmp_name = goods[good_number - 1]['name']
            tmp_price = goods[good_number - 1]['price']
            print('当前购买商品为:{} 价格为：{} '.format(tmp_name,tmp_price))
            user_money -= tmp_price
            tmp_key_goods = []
            for item in user_goods:
                tmp_key_goods.append(item['name'])
            if tmp_name in tmp_key_goods:
                for i in user_goods:
                    if tmp_name == i['name']:
                        i['count'] +=1
            else:
                 user_goods.append({'name':tmp_name,'price':tmp_price,'count':1})
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


# print(user_goods)
sum = 0;
print()
print("用户商品信息".center(30,'*'))
print('-'*30)
for item in user_goods:
    print("商品名{} 价格{} 数量{} ".format(item['name'],item['price'],item['count']))
print('-'*30)
print("用户商品信息".center(30,'*'))
print()
for item in user_goods:
    sum += item['count'] * item['price']
print("共花费：",sum,"元")
print("剩余:",user_money,"元")
