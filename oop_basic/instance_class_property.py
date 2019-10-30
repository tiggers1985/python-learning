#!/usr/local/env python3
# -*- coding: utf-8 -*-


#给实例绑定属性的方法是通过实例变量，或者通过self变量：
#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

class Student(object):
    class_property = 'Student'


print(Student().class_property)