#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:07
# @Author  : anyux
# @FileName: write.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/

with open('wirte.txt',encoding='utf-8',mode='a') as file_hand:
    file_hand.write("十步杀一人\n,千里不留行\n。-------李白\n------杜甫")
    file_hand.close()
