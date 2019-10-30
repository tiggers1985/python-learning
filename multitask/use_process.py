#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# multiprocessing  模块就是跨平台版本的多进程模块
#-------------------------------------------------------------------------------------------------------------------------
from multiprocessing import Process
import os

#!为什么下面这个print方法被执行了两次??????????????????

print('----------------- %s -----' % os.getpid()) #! will run twice in main/sub process
def run_proc(name):
    print('run child process %s(%s)...' %(name, os.getpid()))

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    p =Process(target=run_proc, args=('test',)) #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
    print('child process will start...')
    p.start()
    p.join() #wait join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。 
    print('child process end.')