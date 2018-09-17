#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#需要先引入unittest模块
import unittest;
import logging;
logging.basicConfig(level=logging.INFO);


from mydict import Dict;

#test_开头的方法在调用单元测试时才会被执行
class TestDict(unittest.TestCase):

	#在每调用一个测试方法之前都会执行
	def setUp(self):
		print("aa");

	def test_init(self):
		d = Dict(a=1,b='test');
		self.assertEqual(d.a,1);
		self.assertEqual(d.b,'test');
		self.assertTrue(isinstance(d,dict));

	def test_keyerror(self):
		d = Dict();
		#希望下面的语句能够抛出对应的错误
		with self.assertRaises(KeyError):
			value = d['empty'];

	def test_attrerror(self):
		d = Dict();
		with self.assertRaises(AttributeError):
			value = d.empty;

	#在每调用一个测试方法之后都会执行
	def tearDown(self):
		print("测试结束");

#这是最简单的，但不是最推荐的
#最推荐的方法是在命令行通过-m unittest直接运行单元测试，因为这样可以批量运行
if __name__ == '__main__':
	unittest.main();