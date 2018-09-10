#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#使用装饰器property来减少类中封装属性用到的set和get方法
#例如：
class Student(object):

	@property
	def birth(self):
		return self._birth;

	@birth.setter
	def birth(self,birth):
		if birth < 0:
			raise AttributeError("年份不能小于0");
		else:
			self._birth = birth;

	@property
	def age(self):
		return 2018 - self._birth;

s = Student();
s.birth = 1992;
print(s.age,s.birth);

#exercise
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):

	@property
	def width(self):
		return self._width;

	@width.setter
	def width(self,width):
		self._width = width;

	@property
	def height(self):
		return self._height;

	@height.setter
	def height(self,height):
		self._height = height;

	@property
	def resolution(self):
		return self._width * self._height;

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
	print('测试通过!')
else:
	print('测试失败!')
	