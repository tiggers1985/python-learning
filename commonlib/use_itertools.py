#!/usr/local/env python3
# -*- coding: utf-8 -*-

'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
'''

import itertools
from typing import Iterable

#1. 无限”迭代器

#for n in itertools.count(1):
#    print n

print(isinstance('abc', Iterable))
#for c in itertools.cycle('abc'):
#    print(c)

for n in itertools.repeat('repeat 3 times',3):
    print(n)


#2. itertools提供的几个迭代器操作函数更加有用：

for c in itertools.chain('abc', 'def'): #chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
#实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('aaabbbccddeacd', lambda c: c.upper()):
    print(key, list(group))

