# 1.简单配置方式
# 2.logger对象的配置方式

import logging
# logging.debug('debug message')    # 调试模式
# logging.info('info message')      # 基础正常的信息
# logging.warning('warning message') # 警告信息
# logging.error('error message')    # 错误信息
# logging.critical('critical message') # 批判的 严重错误

# 默认不打印debug，和info
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
#
# logging.debug('你好')    # 调试模式
# logging.info('info message')      # 基础正常的信息
# logging.warning('warning message') # 警告信息
# logging.error('error message')    # 错误信息
# logging.critical('critical message') # 批判的 严重错误

# basicConfig
# 1.中文的乱码
# 2.不能同时向屏幕和文件中输入


import logging
# 吸星大法
# 创建一个logger对象
# 创建一个屏幕管理对象
# 创建一个文件管理对象
# 创建一个格式对象1
# 创建一个格式对象2

# 屏幕管理对象 + 创建一个格式对象1
# 文件管理对象 + 创建一个格式对象2
# logger对象
    # 屏幕管理对象
    # 文件管理对象

# logger = logging.getLogger()
# sh = logging.StreamHandler()
# fh = logging.FileHandler('test2.log',encoding='utf-8')
# fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# sh.setFormatter(fomatter)
# fh.setFormatter(fomatter)
# sh.setLevel(logging.WARNING)
# fh.setLevel(logging.INFO)
#
# logger.addHandler(sh)
# logger.addHandler(fh)
# logger.setLevel(logging.DEBUG)

# logger.debug('你好')    # 调试模式
# logger.info('info message')      # 基础正常的信息
# logger.warning('warning message') # 警告信息
# logger.error('error message')    # 错误信息
# logger.critical('critical message') # 批判的 严重错误

