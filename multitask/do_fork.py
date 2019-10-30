#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# fork
#-------------------------------------------------------------------------------------------------------------------------
import os

print('process (%s) start ...' % os.getpid())
## Only works on Unix/Linux/Mac:
pid = os.fork() #普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# fork 调用之后的代码执行两次
print('pid:', pid)
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

