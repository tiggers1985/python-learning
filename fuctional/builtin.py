#!/usr/local/bin python3
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------------------------------------------------
# map/reduce
#-------------------------------------------------------------------------------------------------------------------------

# map, apply passed fun on each of the item in iterator

def f(x):
    return x*x

for i in map(f, [1,2,3,4]):
    print(i)

for i in list(map(str, [1,2,3,4])):
    print(i)

#reduce, apply passed fun on each of the item and using the last result as function parameter, passed function must accept 2 parameters
#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
#序列求和
def add(x,y):
    return x + y

print(reduce(add,[1,2,3,4,5,6]))



def str2int(s):
    def fn(x,y):
        return x * 10 + y

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    return reduce(fn, map(char2num,s))

print(str2int('222345'))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int2(s):
    return reduce(lambda x,y: x *10 +y, map(lambda x: DIGITS[x], s))

print(str2int2('222345'))


#-------------------------------------------------------------------------------------------------------------------------
# filter
#-------------------------------------------------------------------------------------------------------------------------
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# is odd
for i in filter(lambda x: x%2==1, [1,2,3,4,5,6,7.8]):
    print(i)

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
l = list(filter(lambda x: x%2==1, [1,2,3,4,5,6,7.8]))
print(l)


#-------------------------------------------------------------------------------------------------------------------------
# sorted
#-------------------------------------------------------------------------------------------------------------------------
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，
# 我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。


#Python内置的sorted()函数就可以对list进行排序：
print(sorted([1,2,4,5,6,7, 3]))

#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([1,2,-3], key=abs))