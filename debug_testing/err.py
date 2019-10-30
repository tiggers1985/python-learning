#!/usr/local/bin python3
# -*- coding: utf-8 -*-

'''
sample to demo error traceback
'''

def foo(s):
    return 10/ int(s)

def bar(s):
    return foo(s) *2

def main():
    bar('0')

main()

#trace back
#Traceback (most recent call last):
#  File "err.py", line 10, in <module>
#    main()
#  File "err.py", line 8, in main
#    bar('0')
#  File "err.py", line 5, in bar
#    return foo(s) *2
#  File "err.py", line 2, in foo
#    return 10/ int(s)
#ZeroDivisionError: division by zero