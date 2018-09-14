#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#错误处理
#try...except...finally
#由于一段语句可能抛出多个错误,那么就可以有多个except方法接收
#所有的错误的基类都是BaseException，所以BaseException可以捕获所有错误
#但是为了对应具体错误能够有具体措施，最好针对不同错误进行不同处理
#finally语句只要有，最后一定会执行，也可以咩有finally语句块
#try...except...finally可以在任何地方用

def foo():
	r = 10/0;

try:
	print("try");
	foo();
	print("result:",r);
except BaseException as e:
	print("base except =>" , e);
except ZeroDivisionError as e:
	print("except => ",e);
finally:
	print("finally...");
print("End");

#划重点
#python内置的logging模块可以非常容易地记录错误信息
#logging会记录下错误，然后程序也会正常执行，例如:
import logging;
def foo(s):
	return 10/int(s);

def bar(s):
	return foo(s)*2;

def main():
	try:
		bar(0);
	except Exception as e:
		logging.exception(e);

main();
print("End");
#通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

#抛出错误
class FooError(ValueError):
	pass;

def foo(s):
	n = int(s);
	if n == 0:
		pass;
#		raise FooError("invalid value:%s" % s);
#	return 10/n;

foo('0');

#最后一种抛出错误的方式
#就是在except语句块中，继续向上抛出错误
#except中只是用来记录错误发生的地点，继续向上抛出是因为它业务里处理不了这东西
try:
#	10/0;
	pass;
except ValueError:
	raise;

#exercise
#运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
from functools import reduce

def str2num(s):
#	return int(s)
	return float(s);

def calc(exp):
	ss = exp.split('+')
	ns = map(str2num, ss)
	return reduce(lambda acc, x: acc + x, ns)

def main():
	r = calc('100 + 200 + 345')
	print('100 + 200 + 345 =', r)
	r = calc('99 + 88 + 7.6')
	print('99 + 88 + 7.6 =', r)

main()
