#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# StringIO
#-------------------------------------------------------------------------------------------------------------------------

#很多时候，数据读写不一定是文件，也可以在内存中读写。

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')

print(f.getvalue())

f2 = StringIO('hello \n hi! \n byebye')

while True:
    s = f2.readline()
    if s == '':
        break
    print(s)
