#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#实例属性和类属性
#类属性是绑定在类上的属性，类属性可以被所有实例访问到
#如果类属性与实例属性名称相同，那么实例属性的优先级比较高
class Student(object):
	name = "Delton";

s = Student();
print(s.name);
print(Student.name);

s.name = 'Michael';
print(s.name);
print(Student.name);

del s.name;
print(s.name);
print(Student.name);

#exercise
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
	count = 0;
	def __init__(self,name):
		Student.count += 1;
		self.name = name;

if Student.count != 0:
	print('测试失败!')
else:
	bart = Student('Bart')
	if Student.count != 1:
		print('测试失败!')
	else:
		lisa = Student('Bart')
		if Student.count != 2:
			print('测试失败!')
		else:
			print('Students:', Student.count)
			print('测试通过!')