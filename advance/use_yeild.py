#!/usr/local/env python3
# -*- coding: utf-8 -*-

'''
The yield statement suspends function’s execution and sends a value back to caller, 
but retains enough state to enable function to resume where it is left off. 
When resumed, the function continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, 
rather them computing them at once and sending them back like a list.
'''

def simpleGenerator():
    yield 1
    yield 2

for val in simpleGenerator():
    print(val)



'''
Return sends a specified value back to its caller whereas Yield can produce a sequence of values. 
We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. A generator function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return. 


If the body of a def contains yield, the function automatically becomes a generator function.

'''

#generator function, which is similar to normal function except contains yeild

# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 
  
# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point

for num in nextSquare():
    if num > 100:
         break
    else:
        print(num)