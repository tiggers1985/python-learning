#!/usr/local/env python3
# -*- coding: utf-8 -*-

'''
https://www.geeksforgeeks.org/coroutine-in-python/

协程，又称微线程，纤程。英文名Coroutine。

协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

def A():
    print('1')
    print('2')
    print('3')

def B():
    print('x')
    print('y')
    print('z')
假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：

1
2
x
y
3
z
但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。


Python对协程的支持是通过generator实现的。

在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

Python 2.5之后 yeild也可以作为表达式来使用

'''

def fn():
    print('started ...')
    while True:
        line = (yield) # 等待 send() 方法被调用,并发送一个值
        print(line)
    print('end ...')

f = fn()

# This will start execution of coroutine and  
# Prints first line "Searchig prefix..." 
# and advance execution to the first yield expression 
f.send(None)
#f.__next__() 
#!调用 send(None) 和 __next__() 方法都可以启动生成器

f.send('hi')

f.close()


# Python3 program for demonstrating 
# closing a coroutine 
  
def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    try :  
        while True: 
                name = (yield) 
                if prefix in name: 
                    print(name) 
    except GeneratorExit: 
            print("Closing coroutine!!") 
  
corou = print_name("Dear") 
corou.__next__() 
corou.send("Atul") 
corou.send("Dear Atul") 
corou.close()


def consumer():
    r = ''
    while True:
        n = yield r #返回值
        if not n: #判断 n 和 r 是否相同来决定是否消费
            return
        print('consumer consuming %s....' % n)
        r = '200 OK'

def produce(c):
    c.send(None) # 首先调用c.send(None)启动生成器
    
    n = 0
    while n<5:
        n = n+1
        print('producer producing %s ...' % n)
        r = c.send(n)
        print('producer consumer return %s' % r)
    
    c.close() #关闭协程

c = consumer()
produce(c)