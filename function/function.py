#!/usr/local/bin python3
# -*- coding: utf-8 -*-

import math

class dummy:
    pass

#-------------------------------------------------------------------------------------------------------------------------
# function
#-------------------------------------------------------------------------------------------------------------------------
print(abs(-100))

#type convert
print(int('1'))
print(float('1.0'))
print(str(1))
print(bool(1))

a = abs
print(a(-1))

print(hex(255))

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x;
    else:
        return -x;

print(my_abs(-199))

def nop():
    pass # do nothing, 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。缺少了pass，代码运行就会有语法错误。



def quadratic(a,b,c):
    pass


#-------------------------------------------------------------------------------------------------------------------------
# function, default param
#-------------------------------------------------------------------------------------------------------------------------

######位置参数
print(abs(-10))  #abs 的参数就是一个位置参数

#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x,n=2): # default value
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。
print(power(2,n=3))

#negative sample of default param
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
## 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L;

print(add_end())
print(add_end())

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L;

print(add_end2())
print(add_end2())


#-------------------------------------------------------------------------------------------------------------------------
# function, number variable params
#-------------------------------------------------------------------------------------------------------------------------
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(calc(1,2))
print(calc(1,2,3,4,5))

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

print(calc(*[1,2,3,4]))
print(calc(*()))

#-------------------------------------------------------------------------------------------------------------------------
# function, keyword param
#-------------------------------------------------------------------------------------------------------------------------
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
    #no return returns None automatically

print(person('kevin', 30, city='chengdu'))

#Also, we can pass dict to key word parameter using **
print(person('kevin',30, **{'city':'chengdu','job':'anz'}))


#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
def person(name,age,**kw):
    if 'city' in kw:
        pass
        print('name:', name, 'age:', age, 'other:', kw)

#但是调用者仍可以传入不受限制的关键字参数：
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：

def person(name,age, *, city):
    print('name:', name, 'age:', age, 'city:', city)


print(person('kevin', 30, city='chengdu'))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(age, name, *args, city):
    print('name:', name, 'age:', age, 'city:', city)

print(person('kevin',30, *[1,2,3],city='chengdu'))


#-------------------------------------------------------------------------------------------------------------------------
# function, 参数组合
#-------------------------------------------------------------------------------------------------------------------------
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(arg1, arg2=0,*args, **kw):
    pass

def f2(arg1, arg2=0, *args, key):
    pass

def f3(arg1, arg2=0, *, key, **kw):
    pass




def product(x, *args):
    product = x
    for arg in args:
        product = product * arg
    
    return product

print(product(1))
print(product(1,*[2,3,4,5]))


#-------------------------------------------------------------------------------------------------------------------------
# function, recursive function
#-------------------------------------------------------------------------------------------------------------------------

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(10))


##尾递归
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

def move(n,a,b,c):
    pass



#-------------------------------------------------------------------------------------------------------------------------
# function, parameter type and return type
#-------------------------------------------------------------------------------------------------------------------------
def add(operand1:int, operand2:int) -> int:
    return operand1 + operand2

print(add(1,2))