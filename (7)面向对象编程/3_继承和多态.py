#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#继承
#可以继承父类的方法，也可以重写相同名称的
class Animal(object):
	def run(self):
		print("Animal is running");

class Dog(Animal):
	pass;

dog = Dog();
dog.run();

class Cat(Animal):
	def run(self):
		print("Cat is running");
cat = Cat();
cat.run();

#多态
def something_run(animal):
	animal.run();

print("dog1",something_run(dog));
print("cat1",something_run(cat));

#静态语言 VS 动态语言
#如果是像java这样的静态语言，那么函数定义中的参数是Animal类型的，那么就必须要穿入Animal的一个实例
#而python这样的动态语言就不需要，只需要传入一个实现了run方法的实例就可以了
#这就是动态语言的“鸭子类型”
#例如
class timer(object):
	def run():
		print("时间滴答滴答过去了");
something_run(timer);