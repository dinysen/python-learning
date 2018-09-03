#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#装饰器
def now():
	print("2015-3-25");

#函数对象有个__name__属性，可以获取函数的名称
print(now.__name__);

#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数
def log(func):
	def wrapper(*args,**kw):
		print(" call %s() " % func.__name__);
		return func(*args,**kw);
	return wrapper;

# now = log(now);
@log
def now():
	print("2015-3-25");

now();

import functools;
#如果log需要传递参数，就有
#为了避免函数的__name__属性指向错误,
#需要在wrapper函数上增加@functools.wraps(func)属性
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("%s %s() " % (text,func.__name__));
			return func(*args,**kw);
		return wrapper;
	return decorator;

#now = log("execute")(now)
@log("execute")
def now():
	print("2015-3-25");

print(now.__name__);

now();


#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time;
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (fn.__name__, 10.24));
		return fn(*args,**kw);
	return wrapper;

 # 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else :
	print("测试成功");

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def log2(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		print("begin call");
		result = fn(*args,**kw);
		print("end call");
		return result;
	return wrapper;

@log2
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
fast(11, 22)

#再思考一下能否写出一个@log的decorator，使它既支持： 这个还是得用判断咧。。

#@log
#def f():
#    pass
#又支持：

#@log('execute')
#def f():
#    pass
