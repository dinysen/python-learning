#!/usr/env/bin python3 
#-*- coding: utf-8 -*-

#看到类似__XX__这种变量或属性就要长个心眼，这种在python中是有特殊用途的
#__slots__规定类的实例只能添加固定的属性
#__len__定义len()函数调用的结果

#__str__定义print()函数调用的结果
#__repr__定义调试时显示的内容，一般与__str__是相同的

class Student(object):

	def __init__(self,name,age):
		self._name = name;
		self._age = age;

	def __str__(self):
		return 'Student\'s name is %s ' % self._name;

	__repr__ = __str__;

print(Student('Michael',18));

#__iter__让class的实例可被用作for..in..循环
#它会自动调用实例的__next__方法，所以要实现两个方法
#直到遇到StopIteration()错误为止
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1;

	def __iter__(self):
		return self;

	def __next__(self):
		self.a,self.b = self.b , self.a+self.b;
		if self.a > 1000:
			raise StopIteration();
		return self.a;

for i in Fib():
	print(i);

#__getitem__让实例像list和tuple一样可以使用下标来取值
#要注意的是，n光是int类型是不够的，它也有可能是一个切片，甚至作为dict的一个key可以使str类型
#所以要正确实现一个__getitem__方法是有许多工作要做的
class Fib(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a ,b = 1, 1;
			for x in range(n):
				a , b = b , a+b;
			return a;
		elif isinstance(n,slice):
			#还有步长和负数的情况
			start = n.start if n.start != None else 0;
			stop = n.stop;
			a , b = 1,1;
			l = [];
			for x in range(stop):
				a , b = b , a+b;
				if x >= start:
					l.append(a);
			return l;


f = Fib();
print(f[100]);
print(f[5:10]);