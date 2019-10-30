#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# 动态绑定 实例/类的属性,方法
#-------------------------------------------------------------------------------------------------------------------------

#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass

stu = Student()
stu.name = 'kevin'
print(dir(stu))
print(stu.name)

#还可以尝试给实例绑定一个方法：
def set_age(self,age):
    self.age = age

from types import MethodType
stu.set_age=MethodType(set_age, stu) # 给实例绑定一个方法

stu.set_age(25)
print(stu.age)

#但是，给一个实例绑定的方法，对另一个实例是不起作用的(对实例的更改并不会影响其它实例):

#为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score = score

Student.set_score = set_score
Student.attr = 'Student'

print(dir(stu)) # newly binded method is available for exising instance
print(dir(Student()))



#-------------------------------------------------------------------------------------------------------------------------
# 使用__slots__ 限制动态绑定属性
#-------------------------------------------------------------------------------------------------------------------------


class Student(object):
    __slots__ = ('name','age') # use tuple to limit the dynamic attrs

s2 = Student()
s2.name = 'kevin'
print(s2.name)
#s2.sex = 'male' #AttributeError: 'Student' object has no attribute 'sex'

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduatedStu(Student):
    __slots__ = ('grade') #除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。