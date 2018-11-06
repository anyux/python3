#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 14:36
# @Author  : anyux
# @FileName: test_4.py
# @Software: PyCharm
# @Blog    ：http://www.cnblogs.com/anyux/
import re
import collections
'''
ret = re.search('a', 'eva egon yuan').group()
print(ret)
ret = re.finditer(' ?[a-z]+ ?', 'eva egon yuan')
print(next(ret).group())
print(next(ret).group())
print(next(ret).group())

str = "9-3.3333333333333335+2.3333333333333335*99/4*2998+10*568/14"
ret = re.finditer('\d+\.\d+[*]\d+', str)
print(next(ret).group())
'''
import json
f = open('file','w')
json.dump({'国籍':'中国'},f)
ret = json.dumps({'国籍':'中国'})
f.write(ret+'\n')
json.dump({'国籍':'美国'},f,ensure_ascii=False)
ret = json.dumps({'国籍':'中国'},ensure_ascii=False)
f.write(ret+'\n')
f.close()
import json
data = {'username':['李华','二愣子'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
print(json_dic2)
