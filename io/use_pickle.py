#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
#-------------------------------------------------------------------------------------------------------------------------

import pickle

d = {'name':'bob', 'age':30}

#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like-object
print(pickle.dumps(d))

with open('./dict.dmp', 'wb') as f:
    pickle.dump(d, f)

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
with open('./dict.dmp', 'rb') as f:
    d = pickle.load(f)
    print(d)

#!important Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
#! 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

#-------------------------------------------------------------------------------------------------------------------------
# JSON
#-------------------------------------------------------------------------------------------------------------------------

import json

d2 = {'name':'bob', 'age':30}
print(json.dumps(d2))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d3 = json.loads(json_str)
print(d3)

#-------------------------------------------------------------------------------------------------------------------------
# json pickling user defined class, 自定义类实现pickling 约定 https://docs.python.org/3/library/json.html#json.dumps
#-------------------------------------------------------------------------------------------------------------------------

class Student(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age


s = Student('kevin', 30)

#print(json.dumps(s)) # TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age
    }

print(json.dumps(s, default=student2dict)) #指定序列化转换函数

def dict2stu(d):
    return Student(d['name'],d['age'])

json_str = '{"name":"kevin", "age": 30}'
stu = json.loads(json_str, object_hook=dict2stu)
print(stu.age)
