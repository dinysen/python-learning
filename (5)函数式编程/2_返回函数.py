#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#函数作为返回值
def lazy_sum(*args):
	def sum():
		ax = 0;
		for n in args:
			ax += n;
	return sum;

#每次调用时，都会返回一个新的函数
f1 = lazy_sum(1,3,5,7,9);
f2 = lazy_sum(1,3,5,7,9);
print(str(f1 == f2));

#闭包
#在闭包的函数中使用的变量不能用会变化的变量，因为直接引用的是变量i
#当执行时，i都会被确定为最终得数
#例(反例):
def count():
	fs = [];
	for x in range(1,4):
		def f():
			return x*x;
		fs.append(f);
	return fs;
f1,f2,f3 = count();
print(str(f1()),str(f2()),str(f3()));

#例(正确方式：再写一个函数):
def count1():
	fs = [];
	def j(n):
		def f():
			return n*n;
		return f;
	for x in range(1,4):
		fs.append(j(x));
	return fs;
f1,f2,f3 = count1();
print(str(f1()),str(f2()),str(f3()));

#exercise
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():

	def _iter():
		n = 1;
		while True:
			yield n;
			n += 1;
	it = _iter();

	def f():
		return next(it);
	return f;

counterA = createCounter();
print(counterA(), counterA(), counterA(), counterA(), counterA());

counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')