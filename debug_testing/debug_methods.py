#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# use print to output debug messages
#-------------------------------------------------------------------------------------------------------------------------
print('-------------------------------------')

def foo(s):
    n = int(s)
    print('s value %s' % s) 
    return 10 / n
#垃圾信息比较多,需要删除

#-------------------------------------------------------------------------------------------------------------------------
# use assert,  启动Python解释器时可以用-O参数来关闭assert,关闭后，你可以把所有的assert语句当成pass来看。
#-------------------------------------------------------------------------------------------------------------------------
print('-------------------------------------')

def foo(s):
    n = int(s)
    #如果断言失败，assert语句本身就会抛出AssertionError, 并输出指定的消息
    assert n != 0, 'n is zero!' 
    return 10 / n

def main():
    foo(1)

main()

#-------------------------------------------------------------------------------------------------------------------------
# use logging
#-------------------------------------------------------------------------------------------------------------------------
print('-------------------------------------')

import logging

n = int('1')
logging.info('n = %d' % n)
print(10 / n )


#-------------------------------------------------------------------------------------------------------------------------
# pdb debug  python3 -m pdb err.py
#   输入命令l来查看代码
#   输入命令n可以单步执行代码：
#   任何时候都可以输入命令p 变量名来查看变量
#   输入命令q结束调试，退出程序
#-------------------------------------------------------------------------------------------------------------------------
print('-------------------------------------')

#-------------------------------------------------------------------------------------------------------------------------
# use pdb.set_trace()
#-------------------------------------------------------------------------------------------------------------------------
#这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

#这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停, 可以用命令p查看变量，或者用命令c继续运行
print(10/n)