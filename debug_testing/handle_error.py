#!/usr/local/bin python3
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------------------------------------------------
# try/except
# python exception hierarchy https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#-------------------------------------------------------------------------------------------------------------------------

try:
    print('try...')
    r = 10/0
    print(r)
except ValueError as e:
    print('value error:', e)
except ZeroDivisionError as e:
    print('exception:', e)
else: #此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
    print('no error')
finally:
    print('finally')

#BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- GeneratorExit
# +-- Exception
#      +-- StopIteration
#      +-- StopAsyncIteration
#      +-- ArithmeticError
#      |    +-- FloatingPointError
#      |    +-- OverflowError
#      |    +-- ZeroDivisionError
#      +-- AssertionError
#      +-- AttributeError
#      +-- BufferError
#      +-- EOFError
#      +-- ImportError
#      |    +-- ModuleNotFoundError
#      +-- LookupError
#      |    +-- IndexError
#      |    +-- KeyError
#      +-- MemoryError
#      +-- NameError
#      |    +-- UnboundLocalError
#      +-- OSError
#      |    +-- BlockingIOError
#      |    +-- ChildProcessError
#      |    +-- ConnectionError
#      |    |    +-- BrokenPipeError
#      |    |    +-- ConnectionAbortedError
#      |    |    +-- ConnectionRefusedError
#      |    |    +-- ConnectionResetError
#      |    +-- FileExistsError
#      |    +-- FileNotFoundError
#      |    +-- InterruptedError
#      |    +-- IsADirectoryError
#      |    +-- NotADirectoryError
#      |    +-- PermissionError
#      |    +-- ProcessLookupError
#      |    +-- TimeoutError
#      +-- ReferenceError
#      +-- RuntimeError
#      |    +-- NotImplementedError
#      |    +-- RecursionError
#      +-- SyntaxError
#      |    +-- IndentationError
#      |         +-- TabError
#      +-- SystemError
#      +-- TypeError
#      +-- ValueError
#      |    +-- UnicodeError
#      |         +-- UnicodeDecodeError
#      |         +-- UnicodeEncodeError
#      |         +-- UnicodeTranslateError
#      +-- Warning
#           +-- DeprecationWarning
#           +-- PendingDeprecationWarning
#           +-- RuntimeWarning
#           +-- SyntaxWarning
#           +-- UserWarning
#           +-- FutureWarning
#           +-- ImportWarning
#           +-- UnicodeWarning
#           +-- BytesWarning
#           +-- ResourceWarning


#-------------------------------------------------------------------------------------------------------------------------
# use logging 
#-------------------------------------------------------------------------------------------------------------------------
print('-------------------------------------')
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()

#-------------------------------------------------------------------------------------------------------------------------
# raise error
#-------------------------------------------------------------------------------------------------------------------------
print('-------------------------------------')

class MyError(ValueError):
    pass

def fn(s):
    n = int(s)
    if n == 0:
        raise MyError('invalid value %s' % s)
    return 10/n

#fn('0')

#只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。


def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e: #捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
        print('ValueError!')
        raise #raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型： raise ValueError('input error!')

bar()