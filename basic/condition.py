#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# codition if/else/while/for loop
#-------------------------------------------------------------------------------------------------------------------------

age = 3
if age>= 18:
    print('adult')
    print('again')
elif age>=10:
    print('older than 10')
else:
    print('teenager')

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
t=()
if t:
    print('non empty tuple')
else:
    print('False')


# int() type conversion
#height = int(input(''))
#weight = int(input(''))
#BMI=float(weight/(height*height))


for name in ['kevin','jim','jemy']:
    print(name)


sum = 0
for i in range(101):#range last element not inclued
    sum = sum + i

print(sum)

sum = 0
n = 99
while n>0:
    sum = sum + n
    n = n -2

print(sum)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print('hello,%s' % l)

#break
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)