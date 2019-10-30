#!/usr/local/bin python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------------
# use unittest lib for UT
#-------------------------------------------------------------------------------------------------------------------------

import unittest

from MyDict import Dict

class TestDict(unittest.TestCase): #我们需要编写一个测试类，从unittest.TestCase继承。
    def setUp(self): #execute for each test method
        print('setUp...')

    def tearDown(self): # execute for each test method
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self): #!以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


#RUN UT option1
if __name__ == '__main__':
    unittest.main()

#option 2 另一种方法是在命令行通过参数-m unittest直接运行单元测试  python3 -m unittest mydict_test