# 常用模块
    # time
        # 时间戳
        # 结构化时间
        # 格式化时间
    # os 和操作系统相关的
        # 文件和目录
        # 路径path
        # 调用系统命令
        # 跨平台的符号
        # 环境变量
        # 和工作目录相关的
    # sys 和解释器相关的
        # sys.argv 执行py文件时候传入的参数
        # sys.path
        # sys.modules
    # random
        # 生成随机数
        # 随即抽取
        # 乱序
    # collections
        # deque
            # 适合多insert的程序
        # namedtuple
            # 增强元组的可读性
        # defaultdict
            # 可以给字典设置一个默认值
            # 在设置的时候必须传 可调用的对象
    # 正则表达式
        # 元字符
            # .
            # \w \d \s \W \D \S
            # ^ $
            # [] [^]
            #() |
        # 量词
            # ?
            # +
            # *
            # {n}
            # {n,}
            # {n,m}
        # 默认贪婪匹配
        # 量词后面?表示惰性匹配
    # re
    #     findall 匹配所有，返回列表
    #     serch   匹配第一个，返回对象，如果没匹配到None
    #             获取结果 对象.group()


# import queue
# q = queue.Queue() # 队列
# q.put(1)
# print(q)

# from collections import deque
# dq = deque()
# dq.append(1)
# dq.insert()   # 插入数据的平均速度是比列表快的,差异很大
# # dq[i]       # 索引平均速度要比列表慢,差异不太大
# print(dq)



# 练习题

# 发红包
# import random
# print(random.randint(1,200))

# 计算文件夹大小
import os
lst = ['E:\S22']
total_size = 0
while lst: # lst= ['E:\S22\day8','E:\S22\.idea']
    base_dir = lst.pop()   # 'E:\S22\day9'
    ret = os.listdir(base_dir)
    print(ret)
    for name in ret:
        abspath = os.path.join(base_dir,name)
        if os.path.isfile(abspath):
            total_size += os.path.getsize(abspath)
        elif os.path.isdir(abspath):  #
            lst.append(abspath)  # lst= ['E:\S22\day8','E:\S22\.idea','E:\S22\day9\test']










