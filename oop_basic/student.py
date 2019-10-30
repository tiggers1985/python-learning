#!/usr/local/env python3
# -*- coding: utf-8 -*-

#class后面紧接着是类名，即Student，类名通常是大写开头的单词，
# 紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    pass

stu=Student()

print(stu)

#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
stu.name = 'kevin'
stu.age = 30
print(stu.age)

#-------------------------------------------------------------------------------------------------------------------------
# 指定类的构造函数以及参数
#-------------------------------------------------------------------------------------------------------------------------

#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):
    # 特殊方法“__init__”前后分别有两个下划线！！！  注意到__init__方法的第一个参数永远是self，
    #表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    #有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
    def __init__(self,name,age): 
        self.name = name
        self.age = age

    def print(self):
        print('name: %s, age: %s' % (self.name, self.age))
    

stu2 = Student('kevin', 30) # 如果不传参数会报 TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
print(stu2)
print(stu2.print())

#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。



