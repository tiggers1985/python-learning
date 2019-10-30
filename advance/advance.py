#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# slice
#-------------------------------------------------------------------------------------------------------------------------

#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
print([1,2,3,4][0:3])

#如果第一个索引是0，还可以省略：
print([1,2,3,4][:3])

#类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print([1,2,3,4][-1:])
print([1,2,3,4][-3:-1])
print('slice tuple', (1,2,3,4)[1:3])

L = list(range(100)) # start from 0 to 100, 100 omitted
print(L[:10]) # start default to 0

# step
print(L[:10:2])
print(L[:]) # copy list

#slice for string
print('abcdefg'[:5]) # trim end


def trim(s):
    if len(s)>0:
        return s[1:][:-1]
    else:
        return s

print(len(trim(' abc ')))
print(trim(' ')=='')

#-------------------------------------------------------------------------------------------------------------------------
# iteration
#-------------------------------------------------------------------------------------------------------------------------
#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

#!important
#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['a','b','c']):
    print(i,value)


#-------------------------------------------------------------------------------------------------------------------------
# 列表生成式 list comprehensions, 语法  [] 内编写生成表达式
#-------------------------------------------------------------------------------------------------------------------------
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

print([x*x for x in range(1,11)])
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x*x for x in range(1,11) if x%2==0])
# two layers loop
print([m+n for m in 'abc' for n in 'xyz'])

import os
print([dir for d in os.listdir('.')])

print([k+'=' + v for k,v in {'x': 'A', 'y': 'B', 'z': 'C' }.items()])

print([item for item in ['Hello', 'World', 18, 'Apple', None] if isinstance(item,str)])


#-------------------------------------------------------------------------------------------------------------------------
# generator () 内编写生成表达式
#-------------------------------------------------------------------------------------------------------------------------
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

print((x*x for x in range(10))) #<generator object <genexpr> at 0x1022ef630>

g = (x*x for x in range(10)) #<class 'generator'>
print(type(g))
for i in g:
    print(i)

#call next(g) to print next value, but need to handl StopIteration error

def fib(max):
    n,a,b = 0, 0, 1
    while n< max:
        print(b)
        a,b = b, a + b
        n = n +1
    return 'done'


#仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
#也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib(max):
    n,a,b = 0, 0, 1
    while n< max:
        yield b #这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
                #这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
                # 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
        a,b = b, a + b
        n = n +1
    return 'done'


print(fib(10))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

o = odd()
print(next(o))
print(next(o))


g = fib(6)
while True:
    try:
        x = next(g)
        print('next:', x)
    except StopIteration as e:
        print('generator return value', e.value)
        break


def triangles():
    pass


#-------------------------------------------------------------------------------------------------------------------------
# iterator
#-------------------------------------------------------------------------------------------------------------------------

#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
print(isinstance(1,Iterable))

from collections import Iterator
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance((x for x in range(10)), Iterator)) #
print(isinstance('abc',Iterator)) # false

### 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

#你可能会问，为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。


#小结
#凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1,2,3,4]:
    pass

#equals to

it = iter([1,2,3,4])
while True:
    try:
        x = next(it)
    except StopIteration:
        break


 