#!/usr/local/bin python3
# -*- coding: utf-8 -*-

'''super() method usage samples
    https://realpython.com/python-super/
'''


#-------------------------------------------------------------------------------------------------------------------------
#super() returns a delegate object to a parent class, so you call the method you want directly on it: super().area().
#通过调用父类功能实现代码重用, 继承的同时其实已经可以重用父类代码,但是通过super可以实现对父类功能的增强/扩展
#-------------------------------------------------------------------------------------------------------------------------

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
class Square(Rectangle):
    
    def __init__(self,length):
        super().__init__(length, length)

class Cube(Square):

    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        return super().area() * self.length

#Here you have implemented two methods for the Cube class: .surface_area() and .volume(). 
# Both of these calculations rely on calculating the area of a single face, 
# so rather than reimplementing the area calculation, you use super() to extend the area calculation.
cube = Cube(3)
print(cube.volume())

#-------------------------------------------------------------------------------------------------------------------------
#带参数的super(subclass, obj) 第一个参数指定从那个类开始向上搜索,第二个参数指定一个类的实例对象
# While the examples above (and below) call super() without any parameters, 
# super() can also take two parameters: the first is the subclass, and the second parameter is an object that is an instance of that subclass.
#-------------------------------------------------------------------------------------------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print('call rectangle area')
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

    def area(self):
        print('square area')
        super().area()


#In Python 3, the super(Square, self) call is equivalent to the parameterless super() call. 
# The first parameter refers to the subclass Square, while the second parameter refers to a Square object which, in this case, is self. 

#! You can call super() with other classes as well:
class Cube(Square):
    def surface_area(self):
        face_area = super(Square, self).area() #从Square的父类开始搜索farea方法,找到第一个并使用
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length
#! In this example, you are setting Square as the subclass argument to super(), instead of Cube. 
#! This causes super() to start searching for a matching method (in this case, .area()) at one level above Square in the instance hierarchy, in this case Rectangle.

cube = Cube(3)
print(cube.volume())


#-------------------------------------------------------------------------------------------------------------------------
#多继承下的super
#-------------------------------------------------------------------------------------------------------------------------

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

#以上类继承了两个父类,并且都定义了area方法,如果调用会出现错误:

rp = RightPyramid(2,4)
#print(rp.area()) #AttributeError: 'RightPyramid' object has no attribute 'height'


#-------------------------------------------------------------------------------------------------------------------------
#Python中引入了method resolution order 概念来解决这个问题
#-------------------------------------------------------------------------------------------------------------------------

#Every class has an .__mro__ attribute that allows us to inspect the order, so let’s do that:
print(RightPyramid.__mro__) #(<class '__main__.RightPyramid'>, <class '__main__.Triangle'>, <class '__main__.Square'>, <class '__main__.Rectangle'>, <class 'object'>)

#切换继承类的顺序就可以解决上述问题, #!难道python按照继承顺序来搜索 super类的方法???
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area