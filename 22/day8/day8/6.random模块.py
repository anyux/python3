import random
# random 随机
# 随机

# l = [1,2,3,'a']
# 从4项随机选两个

# 从4项随机选一个，选两次
# 2，2

# 6位 数字+大小写字母的 验证码
# 数字 0,9
# 字母 a-z A-Z   # chr()
# 字母怎么来的？？？
# 每一次每一位上的值可能是字母也可能是数字？

# print(chr(65))
# print(chr(97))
# 0-9    数字
# 65-90  大写字母
# 97-122 小写字母
# 从数字 大小写字母中随机的选取一个
# def random_code(num,alpha=True):
#     import random
#     code = ''
#     for i in range(num):
#         choice = str(random.randint(0,9))
#         if alpha:
#             alpha_lower = chr(random.randint(65,90))
#             alpha_upper = chr(random.randint(97,122))
#             choice = random.choice([choice,alpha_lower,alpha_upper])
#         code += choice
#     return code
#
# print(random_code(4,False))






