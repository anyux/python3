import collections

# 使用模块必须先导入 # 需要注意的是 已知的所有模块名都不可以作为python文件名
# 每一个模块都有一个大致的功能
# collections给我们提供了一些额外的数据类型

# str int list dict tuple set float  内置数据类型
# 每一个类都是一个数据类型 自定义数据类型
a = 'a'   # 实例化 str('a')
# python一切皆对象
# a = 1

# from math import sqrt
# collecctions模块是扩展我们数据类型的一个模块
# tuple元组
p = (1,2)  # 坐标
#sqrt(p[0]**2 + p[1]**2) # 代码的可读性差

# 可命名元祖
# Point = collections.namedtuple('point',['x','y'])
# p = Point(1,2)
# print(p)
#
# print(p.x)
# print(p.y)
#
# from math import sqrt
# sqrt(p.x**2 + p.y**2)  # 程序会变得更明确，可读性更高

# 在存储数据的基础上 严格的维持了一个秩序，数据的进出顺序
# queue 队列 先进来的先出去  —— 售票
# 栈         先进来的后出去 ——  计算机的计算、算法
# import queue # 队列
# q = queue.Queue()
# l = list()
# q.put(1)  # 放
# q.put(2)  # 放
# print(q.get()) # 取

# import collections
#
# dq = collections.deque()
# dq.append(1)
# dq.append(2)
# print(dq)
# print(dq.pop())
# print(dq)
# dq.appendleft(5)
# print(dq.popleft())
# print(dq)

# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d.keys())

# from collections import OrderedDict
# d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(d.keys())

# from collections import defaultdict

# dd = defaultdict(list)
# print(dd)
# dd['aaaaaaaaa'].append(1)
# print(dd)
# def func():return 5
# # dd = defaultdict(func)
# dd = defaultdict(lambda : 5)
# print(dd)
# dd['aaaaaaaaa']
# print(dd)
# dd['aaaaaaaaa'] = 20
# print(dd)

# a = 1
# class B():pass
# def c():pass
# print(callable(a))
# print(callable(B))
# print(callable(c))

# from collections import namedtuple
# Point = namedtuple('point',['x','y'])
# print(Point)
# p = Point(1,2)
# print(type(p))
#
# class A:pass
# print(A)
# a = A()
# print(type(a))