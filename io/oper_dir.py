#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# use os module
#-------------------------------------------------------------------------------------------------------------------------
#操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

import os

print(os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.uname) #要获取详细的系统信息，可以调用uname()函数

#print(os.environ) # 在操作系统中定义的环境变量
print(os.environ.get('CLASSPATH')) #要获取某个环境变量的值，可以调用os.environ.get('key')

#-------------------------------------------------------------------------------------------------------------------------
# use os module
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
#-------------------------------------------------------------------------------------------------------------------------

# 查看、创建和删除目录可以这么调用：
print(os.path.abspath('.'))

#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.join('/a/b/c','e/f')) 


dir = './dir1'
if not os.path.exists(dir):
    print('create dir %s' % dir)
    os.mkdir(dir)

if os.path.exists(dir):
    print('remove dir %s' % dir)
    os.rmdir(dir)


print([print(x) for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

