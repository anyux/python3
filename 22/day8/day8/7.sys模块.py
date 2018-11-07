# 和python解释器打交道的
import sys
# print('3.6' in sys.version)
# print(sys.platform) # win32

# print(sys.path)
# 你的模块能不能被顺利的导入
# 取决于这个模块是否在你的sys.path路径中
# 路径的寻找是依据sys.path列表中的顺序查找的
# 找到一个符合条件的就停止了
import time
# print(sys.modules)
# 记载了我们已经导入的模块名以及这个模块的内存地址

# print(sys.argv)
# sys.exit()   # 退出
# if len(sys.argv)>1 and sys.argv[1] == 'alex'and sys.argv[2] == 'alex3714':
#     print('登陆成功')
# else:
#     user = input('user:')  # 阻塞
#     pwd = input('pwd:')
#     if user == 'alex' and pwd == 'alex3714': print('登陆成功')



