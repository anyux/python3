#!/usr/bin/env python
# -*- coding:utf-8 -*-
# l1 = []
# for i in range(1,23):
#     l1.append('python%s期' % i)
# print(l1)

# l = [i for i in range(1,11)]
# # [变量（加工后的变量) for 变量 in iterable] 遍历模式
# # print(l)
# l2 = ['python%s期' % i for i in range(1,23)]
# print(l2)

# [变量（加工后的变量) for 变量 in iterable] 遍历模式

# l1 = []
# for i in range(1,31):
#     if i % 3 ==0:
#         l1.append(i)
# print(l1)
# [变量（加工后的变量) for 变量 in iterable] 遍历模式
# [变量（加工后的变量) for 变量 in iterable if 条件] 筛选模式

# l2 = [i for i in range(1,31) if i % 3 == 0]
# print(l2)
# l2_obj = (i for i in range(1,31) if i % 3 == 0)
# print(l2_obj)
# for i in l2_obj:
#     print(i)
# print(l2)
# 列表推导式：简单，一行搞定。
# 特别复杂的数据列表推导式无法实现，只能用其他方式实现。
# 列表推导式不能排错。
# 列表推导式与生成器表达式区别
# 1 ,列推直观能看出，但是占内存
# 2，生成器表达式不易看出，但是节省内存。

# 1 构建列表： 十以内的所有的元素的平方。
# print([i*i for i in range(1,11)])
# 2, 30以内所有能被3整除的数的平方
# print([i*i for i in range(1,31) if i % 3 == 0])
# 3，[3,6,9] 组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]
# print([[i-2, i-1, i] for i in [3,6,9]])
# 4,
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
print([i for l in names for i in l if i.count('e') == 2])

l = ['您好', '3.64',
'请问您是xxx同学的家长吗', '6.25',
'是的有什么事情吗', '6.15',
'您好我是学大教育的x老师', '5.06',
'这次给给您打电话主要是想了解一下孩子上学期的协议情况', '5.86',
'针对于上学期的学习状况', '5.37',
'我们学校邀请您和孩子周末过来听一下针对性的辅导课好吧好吧', '5.36',
'可以我想问一下都有什么课程呢', '5.65',
'呃主要是有英语和语文', '4.35',
 '你看', '3.77',
 '到时候咱们再联系好吧', '6.10',
 '好的', '6.45',
 '恩再见', '4.84']
# 上面这个列表帮我转成下面这种格式
# [{"onebest":"您好", "speed":"6.060606"},
# {"onebest":"我这是中国电信的客户代表请问您是幺五幺幺零幺五六六六幺号码的长期使用者吗", "speed":"5.479452"},
# {"onebest":"是的", "speed":"5.405406"},
# {"onebest":"为啥谢谢您长期以来的支持",  "speed":"5.529954"},
# {"onebest":"交银退掉", "speed":"4.938272"},
# {"onebest":"考虑了解生活小贴士服务美元四月","speed":"4.672897"},
# {"onebest":"你们可以收到天气情况活动", "speed":"5.529954"},
# {"onebest":"我建议", "speed":"4.347826"},
# {"onebest":"生活中了就是周转现在开通后","speed":"4.024768"},
# {"onebest":"发到您的", "speed":"8.510638"},
# {"onebest":"都会","speed":"4.255319"},
# {"onebest":"现在","speed":"6.451613"},
# {"onebest":"可以享有就是看吗", "speed":"5.161290"},
# {"onebest":"可以","speed":"6.451613"},
# {"onebest":"改天先生那是的",  "speed":"4.046243"},
# {"onebest":"另外再见",  "speed":"5.479452"}
# ]
# print([{"onebest":l[i],"speed":l[i+1]} for i in range(len(l)) if i % 2 == 0])
# x = {
#     'name':'alex',
#     'Values':[{'timestamp':1517991992.94,
#          'values':100,},
#         {'timestamp': 1517992000.94,
#         'values': 200,},
#         {'timestamp': 1517992014.94,
#          'values': 300,},
#         {'timestamp': 1517992744.94,
#          'values': 350},
#         {'timestamp': 1517992800.94,
#          'values': 280}
# 		],}
# 将上面的数据通过列表推导式转换成下面的类型：
# [[1517991992.94, 100], [1517992000.94, 200], [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
