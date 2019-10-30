#!/usr/local/env python3
# -*- coding: utf-8 -*-

#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

from protected_student import Student

stu = Student('k',30)

print(type(stu))
print(type(abs))

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

def fn():
    pass


print(type(fn) == types.FunctionType)

#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
print(isinstance(stu, Student))


