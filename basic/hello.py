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