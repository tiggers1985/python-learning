#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#-------------------------------------------------------------------------------------------------------------------------
# __str__()/ __repr__() similar to toString()
#-------------------------------------------------------------------------------------------------------------------------

class Student(object):
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return 'student name %s' % self._name

s = Student('kevin')

print(s) # print out formated text, rather than <__main__.Student object at 0x109afb310>

#implement repr method to print out object directly
Student.__repr__ = Student.__str__
# s #interactive mode


#-------------------------------------------------------------------------------------------------------------------------
# __iter__()
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
#-------------------------------------------------------------------------------------------------------------------------

class fib(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化两个计数器a，b
    
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    
    def __next__(self): # for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100 :
            raise StopIteration()
        else:
            return self.a

print('-----fib-------')
for i in fib():
    print(i)


#-------------------------------------------------------------------------------------------------------------------------
# __getitem__ 类似于C#的索引器
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素,要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
#-------------------------------------------------------------------------------------------------------------------------


class fib(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化两个计数器a，b
    
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    
    def __next__(self): # for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100 :
            raise StopIteration()
        else:
            return self.a
    
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b = b, a + b
        return n

f = fib()
print(f[3])
print(f[8])

#实现类似于list的切片功能
#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

class fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start # start attr
            stop = n.stop #! stop attr
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f2 = fib()
print(f2[3:10])

#此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


#-------------------------------------------------------------------------------------------------------------------------
# __getattr__
#-------------------------------------------------------------------------------------------------------------------------
#调用不存在的属性时 python会抛出 AttributeError: 'Student' object has no attribute 'score'
#如果希望返回默认值活着返回友好的信息,可以实现 __getattr__

class Student(object):
    def __init__(self):
        self.name = ''

    #!注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        else:
            raise AttributeError

s = Student()
print(s.score)


#基于 __getattr__()实现链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().user)



#-------------------------------------------------------------------------------------------------------------------------
# __call__(self,params...)
#-------------------------------------------------------------------------------------------------------------------------
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

class Student(object):
    def __init__(self):
        pass

    def __call__(self):
        print('direct call against instance')

s = Student()
print(s())