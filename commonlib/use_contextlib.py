#!/usr/local/env python3
# -*- coding: utf-8 -*-

'''
python 中通过 with语句 简化了 try... finally... 文件访问调用
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。

实现上下文管理是通过__enter__和__exit__这两个方法实现的。
'''

#-------------------------------------------------------------------------------------------------------------------------
# 通过实现 __enter__() / __exit__() , 实现with形式调用, 类似于 C#实现 IDispose接口
#-------------------------------------------------------------------------------------------------------------------------
class Query:

    def __init__(self,name):
        self.name = name
    

    def __enter__(self):
        print('begin')
        return self #
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('error')
        else:
            print('end')
    
    def query(self):
        print('query info about %s' % self.name)


with Query('kevin') as q:
    q.query()

#-------------------------------------------------------------------------------------------------------------------------
# contextmanager decorator
#-------------------------------------------------------------------------------------------------------------------------
#! 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：

from contextlib import contextmanager 

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query(name)
    yield q #@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
    print('end')

'''
contextmanager接受一个generator(上例包含yeild的方法就是generator)
'''

with create_query('kevin') as q:
    q.query()


#很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield # return generator
    print('</%s>' % name)

with tag('html'):
    print('hello')

'''
'__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', 
'__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', 
'__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__',
 '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__wrapped__']
'''
print(type(tag))
print(dir(tag))

'''
代码的执行顺序是：

with语句首先执行yield之前的语句，因此打印出<h1>；
yield调用会执行with语句内部的所有语句，因此打印出hello和world；
最后执行yield之后的语句，打印出</h1>。
因此，@contextmanager让我们通过编写generator来简化上下文管理。
'''


#-------------------------------------------------------------------------------------------------------------------------
# closing decorator
#-------------------------------------------------------------------------------------------------------------------------
#如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen
import sys
sys.path.append('../')

proxies = {'http':'http://yank2:Admin20!910@gblproxy.intranetlb-sg.anz:80',
           'https':'https://yank2:Admin20!910@gblproxy.intranetlb-sg.anz:80'}

with closing(urlopen('http://max.global.anz.com/',proxies=proxies)) as page:
    for line in page:
        print(line)

'''
closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
它的作用就是把任意对象变为上下文对象，并支持with语句。
'''