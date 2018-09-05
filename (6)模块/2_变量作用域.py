#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#python中的私有变量一般用_和__表示
#并不是说这是python语法，只是编程习惯

#用法，例如：
#将外部可以访问的函数定义为public,内部函数使用private
def _private_1(name):
	return "Hello , %s " % name;

def _private_2(name):
	return "Hi , %s " % name;

def greeting(name):
	if(len(name) > 3):
		return _private_1(name);
	else :
		return _private_2(name);
