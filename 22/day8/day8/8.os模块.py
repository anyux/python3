# os模块
# 操作系统打交道的
import os
# print(os.getcwd())
# 所谓工作目录并不是当前文件所在的位置
# 而是执行代码的时候我的目录

# print(__file__)
# os.chdir(os.path.dirname(__file__))
# print(os.getcwd())

# os.makedirs('dirname3/dirname4')
# os.rmdir('dirname3/dirname4')
# os.removedirs('dirname1/dirname2/dirname3/dirname4')

# print(os.stat(r'E:\S22\day8\1.讲在课前.py'))
# print(os.name)

# os.system('dir')  # 直接显示结果的
# ret = os.popen('dir')  # 返回值 返回的内容要通过read获取
# print(ret.read())
# print(os.environ)

# print(os.path.abspath('1.讲在课前.py'))
# print(os.path.split(r'E:\S22\day8\1.讲在课前.py'))
# print(os.path.split(r'E:\S22\day8'))
# print(os.path.dirname(r'E:\S22\day8'))
# print(os.path.basename(r'E:\S22\day8'))
# print(os.path.join('E:\S22','day8','1.讲在课前.py'))

print(os.path.getsize(r'E:\S22\day8\4.collections模块.py'))
print(os.path.getsize(r'E:\S22\day8\3.常用模块.py'))
print(os.path.getsize(r'E:\S22\day8\2.学习内容介绍.py'))
print(os.path.getsize(r'E:\S22\day8\6.random模块.py'))
print(os.path.getsize(r'E:\S22\day8'))

# E:\S22   4096
# 递归思想、堆栈思想
# 给定任意一个文件夹 使用python代码统计这个文件夹的大小


