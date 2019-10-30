#!/usr/local/env python3
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------------------------------------------------
# return function
#-------------------------------------------------------------------------------------------------------------------------

# function as function return value

#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ret = 0
        for n in args:
            ret = ret + n
        print(ret)
        return ret
    return sum

f = lazy_sum(1,2,3)
print(f)
print(f())

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
print(lazy_sum(1,2)==lazy_sum(1,2)) # False

###闭包 !!!!!!!!!!!!!!!!!!!!!!


#-------------------------------------------------------------------------------------------------------------------------
# anonymous function
#-------------------------------------------------------------------------------------------------------------------------

print(list(map(lambda x: x*x, [1,2,3,4,5,6])))

# lambda x: x*x equals to
def f(x):
    return x*x

#关键字lambda表示匿名函数，冒号前面的x表示函数参数。 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。