#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#动态语言的特性就是在生成实例后，能够直接给实例添加新属性和方法
#例：
class Student(object):
	pass;

s = Student();
s.name = 'Delton';
def getName(stu):
	return stu.name;

from types import MethodType;
s.getName = MethodType(getName,s);
print(s.getName());

#但是对一个实例绑定方法后，对另一个实例不起作用
#例:
s2 = Student();
print(hasattr(s2,"getName"));

#为了给所有实例都绑定方法，可以给class绑定方法
def getName(self):
	print("这是父类的方法");
	return self.name;

Student.getName = getName;
s2.name = "Hello";
print(s2.getName());

#但是如果我们想要限制给实例添加的属性时如何处理?
#在类当中使用__slots__属性
#例：
class Student2(object):
	__slots__ = ('name','age');#意思是只允许添加name和age属性

s3 = Student2();
s3.name = 'AAA';
s3.age = 'bbb';

#如果子类没有__slots__属性，说明父类的__slots__属性对子类没有影响
class subStu(Student2):
	pass;
sub = subStu();
sub.score = '5136';

#如果子类设置了__slots__属性，那么可添加的属性就是父类与子类的并集
class subStu2(Student2):
	__slots__ = ('score');

sub2 = subStu2();
sub2.score = 'a';
sub2.name = 'destiny';
