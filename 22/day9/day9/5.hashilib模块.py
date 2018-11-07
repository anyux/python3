# 登录
# 内存
# 文件
    # alex|alex3714
# 数据库 - 文件夹
    # 取数据 查数据的时候 更简便

# 账户不安全
# 密码不应该以明文的形式存储在文件、数据库里

# 加密
# 怎么加密？
# alex3714
# hashlib

# import hashlib
# md5_obj = hashlib.md5()  # 选择了md5算法   32位16进制的字符串0.0001 1
# s = input('>>>')
# md5_obj.update(s.encode('utf-8'))
# print(md5_obj.hexdigest())
# 按了下71
# alex3714|aee949757a2e698417463d47acac93df
# md5_obj.update(b'alex3714')
# md5_obj.update(bytes(s,encoding='utf-8'))
# 第一 使用相同的算法对同一个字符串进行摘要
# 在任意时刻 任意平台 任意语言结果总是不变的
# 第二 这个摘要过程不可逆
# 第三 对于不同的数据的计算结果总是不同的

# md5算法  —— 撞库
# 数字 字符串
# import hashlib
# username = input('>>>')
# md5_obj = hashlib.md5(username.encode('utf-8'))  # 选择了md5算法   32位16进制的字符串0.0001 1
# s = input('>>>')
# md5_obj.update(s.encode('utf-8'))
# print(md5_obj.hexdigest())

# 登录的时候
# 用户输入密码之后，再用相同的算法再摘要一次
# 和数据库、文件里的比对一下

# 先考虑安全
# 再考虑效率

# 校验文件一致性
import os
import hashlib
def get_md5(file,n = 10240):
    with open(file, 'rb') as f1:
        md5_obj = hashlib.md5()
        file_size = os.path.getsize(file)
        while file_size>0:
            md5_obj.update(f1.read(n))
            file_size -= n
        return md5_obj.hexdigest()


def compare(file1,file2):
    return get_md5(file1) == get_md5(file2)

print(compare(r'E:\S22\day9\3.正则模块.py',r'E:\S22\day9\3.正则模块.py.bak'))
# 如果文件5个G
# 按照字节

# import hashlib
# md5_obj1 = hashlib.md5()
# md5_obj1.update('hello,'.encode('utf-8'))
# md5_obj1.update('al'.encode('utf-8'))
# md5_obj1.update('ex'.encode('utf-8'))
# print(md5_obj1.hexdigest())
# 624346509f7ecf44f4b9d088b235f923


