import time
# time.sleep(1)  # 让你当前执行的程序 阻塞1s

# 时间的几种表示格式
# print(time.time())
# # 1530330328 unix时间戳时间
# # 为什么要有时间戳时间 —— 计算机用的float
# # 格式化时间 —— 人用的 年月日时分秒 str
# print(time.strftime('%Y'))  # year
# print(time.strftime('%m'))  # month
# print(time.strftime('%d'))  # day
#
# print(time.strftime('%H'))  # hour
# print(time.strftime('%M'))  # Minute
# print(time.strftime('%S'))  # Second
#
# print(time.strftime('%c'))  # year
# print(time.strftime('%m/%d/%Y %H:%M'))  # year

# 时间戳时间float —— 给机器看的
# 结构化时间 —— 中间的过渡
# 格式化 %s —— 给人看的

# print(time.localtime().tm_mday)

# 2018-6-30 11:49
# 2018/6/30 11:49
# 30/6/18 11:49

# 转换关系

# timestamp = time.time()
# print(timestamp)
# ts2 = 3000000000
# print(time.localtime())
#
# struct_time = time.localtime(ts2)
# print(time.strftime('%m/%d/%Y %H:%M',struct_time))

# struct_time = time.strptime('2020','%Y')
# print(time.mktime(struct_time))
# print(time.strptime('2020','%Y'))