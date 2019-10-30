#!/usr/local/env python3
# -*- coding: utf-8 -*-

'''
asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。

asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。


python 只会在解释器当前进程中执行代码,所谓的异步其实就是通过协程模型的中断机制来实现多个任务在同一个线程中执行,
切换到高级语言中类似于将io操作封装到一个协程中,其它操作放到另外的协程中实现高cpu利用率
'''

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(10) #协程中断,等待返回值
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()