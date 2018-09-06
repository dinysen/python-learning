#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#面向对象编程
#类和实例

#括号中的object是继承自什么类
class Student(object):

	#相当于构造函数，变量前的__代表这个属性为private属性
	#__init__函数的self参数代表实例化对象本身
	def __init__(self,name,score):
		self.__name = name;
		self.__score = score;

	#内部方法可以直接通过self来获得实例的内部参数
	def get_score(self):
		print("这个人的成绩是:%s分" % self.__score);

stu = Student("dalton",99);
stu.get_score();