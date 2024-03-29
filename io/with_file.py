#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# read file
#   read()  read all
#   read(size)  read size bytes
#   readline() read one line one time
#   readlines()  read all lines
#-------------------------------------------------------------------------------------------------------------------------

try:
    f = open('../readme.md', 'r')
    print(f.read()) # read all
except IOError as e:
    print('error ', e)
finally:
    f.close()


#但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法, 类似于 C# 的 using
with open('../readme.md','r') as f: 
    print(f.read())

with open('../readme.md','r') as f:
    for line in f.readlines():
        print(line)


#-------------------------------------------------------------------------------------------------------------------------
# binary file 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
#-------------------------------------------------------------------------------------------------------------------------

with open('img.JPG','rb') as f:
    print(f.read())

#-------------------------------------------------------------------------------------------------------------------------
# encoding
#-------------------------------------------------------------------------------------------------------------------------
with open('../readme.md','r', encoding='utf-8', errors='ignore') as f: 
    print(f.read())


#-------------------------------------------------------------------------------------------------------------------------
# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# w write, will overwride existing file
# a append
#-------------------------------------------------------------------------------------------------------------------------

with open('test.md','a') as f: 
    f.writelines('hello world')

