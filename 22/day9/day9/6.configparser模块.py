# 登录文件 userinfo
#
# open(file_path)

# /user/local/app

# import configparser
#
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes',
#                      'file_path':r'E:\S22\day9\userinfo'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
# with open('example.ini', 'w') as f:
#     config.write(f)

import configparser

config = configparser.ConfigParser()
# print(config.sections())
config.read('example.ini')
# print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True

# print(config['bitbucket.org']["user"])  # hg
# print(config['DEFAULT']['Compression']) #yes
# print(config['topsecret.server.com']['Compression']) #yes
# print(config['topsecret.server.com']['ForwardX11'])  #no
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key,config['bitbucket.org'][key])
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value

