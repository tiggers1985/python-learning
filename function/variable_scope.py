#!/usr/local/bin python3
# -*- coding: utf-8 -*-

# https://www.programiz.com/python-programming/global-local-nonlocal-variables

x = "global"

def foo():
    #global x #
    x = x * 3 # 如果不使用global关键字, 则python 会查找local variable x 并进行赋值,由于没有找到 local variable x而抛出错误
    print(x) #即使不使用global,print 也可以访问 全局变量
foo()

'''
Traceback (most recent call last):
  File "variable_scope.py", line 9, in <module>
    foo()
  File "variable_scope.py", line 7, in foo
    x = x * 2
UnboundLocalError: local variable 'x' referenced before assignment
'''