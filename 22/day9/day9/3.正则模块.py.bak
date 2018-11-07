import re

# ret = re.search('^\d', '2b3ca1bc')
# print(ret.group())
# ret = re.match('\d', '2b3ca1bc')
# print(ret.group())
# 只会匹配以某个正则规则开头地字符串
# findall ：取所有，返回一个列表
# search ： 取匹配的第一个，匹配到返回一个对象，取值都是用group
# match ：  取以。。开始的第一个，匹配到返回一个对象，取值都是用group

# ret = re.split('\|','alex|alex3714')
# ret = re.split('\d+','alex2222egon3wusir4')   # 分割
# ret = re.sub('\d+','|','alex2222egon3wusir4') # 替换
# ret = re.subn('\d+','|','alex2222egon3wusir4')# 替换，并返回替换的次数
# print(ret)

# re.search('\d\*\d', '1+2-3+4-30').group()
# \d\*\d编译计算机能理解的
# 再去对字符串进行匹配

# obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
# ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
# print(ret.group())  #结果 ： 123
# ret = obj.findall('abc123ee7163has93629') #正则表达式对象调用search，参数为待匹配的字符串
# print(ret)

# ret = re.finditer('\d', 'ds3sy4784a')
# print(ret)
# print(next(ret).group())
# for i in ret:
#     print(i.group())


# findall
    # 匹配所有
    # 返回列表，值
# search
    # 匹配第一个
    # 返回对象，group
# match
    # 匹配从头开始的第一个
    # 返回对象，group
# split
    # 分割
    # 返回列表，值
# sub/subn
    # 替换
    # 返回字符串/元组
# compile
    # 编译 ：在多次使用同一个正则时提高效率
    # 返回正则表达式的对象
    # 可以任意选择想用的方法
# finditer
    # 提高的是空间的效率，节省内存空间
    # 返回一个迭代器
    # 通过for或者next取值
    # 取到的每一个值是一个匹配到的对象，通过group取值


import re

# ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# print(ret)  # 正则表达式findall对分组有优先显示
# ret = re.findall('www.baidu.com|www.oldboy.com', 'www.oldboy.com')
# print(ret)

import re


# ret = re.search("<(?P<tag>\w+)>\w+</(?P=tag)>","<h1>hello</h1>")
# print(ret)
# print(ret.group('tag'))
#
# ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
# print(ret)
# print(ret.group(1))
# ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
# print(ret.group('tag_name'))  #结果 ：h1
# print(ret.group())  #结果 ：<h1>hello</h1>


# html中
# 所有的文字要想有格式
# 必须把文字写在一个标签里
# <a> sdkaghkdhhafld</a>


# ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']

# 有的时候 有一些我们不需要的东西，要通过匹配他的形式把它去掉
# ret = re.findall('\d+(?:\.\d+)?',"1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)

# ret = re.findall('\d+\.\d+|(\d+)',"1-2*(60+(-40.35/5)-(-4*3))")
# print(ret)
# ret.remove('')
# print(ret)

# re.findall()


# 正则指引
  # python
