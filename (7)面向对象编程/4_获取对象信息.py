#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#使用type方法可以获取实例所属的类型
#例如：
print(type(123));
print(type("str"));
print(type(None));
print(type(abs));

class Animal(object):
	pass;
class dog(Animal):
	pass;
print(type(dog));

#比较两个变量的type类型是否相同
print(type(123)==type(456));
print(type(123)==int);
print(type('abc')==type('123'));
print(type('abc')==str);
print(type('abc')==type(123));

#如果是一个函数，那么可以尝试使用内置的types模块中定义的常量
import types;
print(type(dog) == types.FunctionType);
print(type(abs) == types.BuiltinFunctionType);
print(type(lambda x : x) == types.LambdaType);
print(type((x for x in range(10))) == types.GeneratorType);

#使用isinstance,优先使用
#可以获取继承链上所有对象的类型
#例如 object->Animal->Dog->Husky
class Animal(object):
	pass;
class Dog(Animal):
	pass;
class Husky(Dog):
	pass;
dog = Dog();
print(isinstance(dog,Dog));
print(isinstance(dog,Animal));
print(isinstance(dog,Husky));

#能用type判断的基本类型也可以用isinstance判断
print(isinstance('123',str));
print(isinstance(lambda x : x,types.LambdaType));
print(isinstance((x for x in range(10)),types.GeneratorType));
def fn():
	pass;
print(isinstance(fn,types.FunctionType));
print(isinstance(abs,types.BuiltinFunctionType));

#判断几种类型中的一种
print(isinstance([1,2,3],(list,tuple)));

#使用dir
#可以获取一个对象的所有属性和方法
#类似__XXX__的属性和方法在python中都是有特殊用途的
#比如__len__返回长度，len(XX)就是调用XX对象的__XX__方法
#例如:
len('1234');
'1234'.__len__();

#如果希望len函数也能用在自己创建的对象上，则需要在对象上创建__len__方法
#例如：
class test_len(object):

	def __init__(self,len):
		self.__len = len;

	def __len__(self):
		print("obj's length %s " % self.__len);
		return self.__len;

len_obj = test_len(5);
print(len(len_obj));

#仅仅能够通过dir方法获取属性和方法是不够的
#我们还要能够使用
#那么就需要利用setattr,getattr,hasattr
#需要注意的事，我们只有在不确定一个实例是否有这些属性的时候才使用这三个方法
class MyObject(object):
	def __init__(self):
		self.x = 9;

	def power(self):
		return self.x * self.x;

obj = MyObject();
print(hasattr(obj,'x'));
print(hasattr(obj,'y'));
print(setattr(obj,'y',19));
print(hasattr(obj,'y'));
print(getattr(obj,'y'));
print(obj.y);

#获取一个属性，如果属性不存在，那么就返回设置的默认值
print(getattr(obj,'z',404));

#下面是获得对象的方法
print(hasattr(obj,'power'));
fn = getattr(obj,'power');#fn就指向obj.power
print(fn());