#!/usr/local/bin python3
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------------------------------------------------
# basic
#-------------------------------------------------------------------------------------------------------------------------

print("hello")

a=100
if a>=0:
    print(a)
else:
    print(-a)

print(r'\'\t')


print('''111
222
''')

#age=input("enter your age")
age=20
if int(age)>=18:
    print('adult')
else:
    print('teenager')

#-------------------------------------------------------------------------------------------------------------------------
# string format
#-------------------------------------------------------------------------------------------------------------------------
print('hello, %s' % 'world')
#append leading space or 0 if padding character not specified
print('%2d-%02d' % (3,1))
#3-01
print('%.2f' % 3.1412)
#3.14
print('hello {0}, your scored improved {1:.1f}%'.format('kevin', 17.25))


s1 = 72
s2 = 85
r = (85/72 - 1) * 100
print(r)
print('%.1f%%' % r)
#18.1%

#-------------------------------------------------------------------------------------------------------------------------
# list []
#-------------------------------------------------------------------------------------------------------------------------
classmates = ['kevin', 'tody']
print(len(classmates))
print(classmates)
print(classmates[-2])

classmates.append('jemy')
classmates.insert(2, 'jim')
#pop last element
classmates.pop()

print(classmates)

classmates[2]='sara'
print(classmates)

l = ['kevin', 1, 30.2]
l.append(['a','b'])
print(l)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0], L[1][1], L[2][2])

#-------------------------------------------------------------------------------------------------------------------------
# tuple(), tuple can't be changed after initialization which is different to list
#-------------------------------------------------------------------------------------------------------------------------

#empty tuple
t = ()

t = (1,2)
print(t)

#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)

print(len(t))


#-------------------------------------------------------------------------------------------------------------------------
# dict(map)/set
#   Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#   set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#-------------------------------------------------------------------------------------------------------------------------
dict = {'kevin':80, 'bob':100}
print(dict['kevin'])

dict['alice']=100
print(dict['alice'])

dict['alice']=50 #override
print(dict['alice'])


#print(dict['notexist']) #KeyError: 'notexist


if 'notexist' in dict: # dict.get() return None if not exist
    print(dict['notexist'])
else:
    print('key not exist')


dict.pop('bob') #remove item

#key = ['test','hhh']
#dict[key] = 'xx' #TypeError: unhashable type: 'list'


#要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print(s)

s.add(4)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(3)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s2 = set([3,4,5])

print(s & s2)
print(s | s2)