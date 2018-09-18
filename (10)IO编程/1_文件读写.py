#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#读文件
try:
	f = open('D:/develop/phython/workspace/python-learning/(1)第一个python程序/test.py','r');
	s = f.read();
	print(s);
finally:
	#文件用完后必须关闭文件流，所以最好使用try...finally...
	f.close();

#另一种写法 利用with语句，可以详细参考下文档并给出示例
with open('D:/develop/phython/workspace/python-learning/(1)第一个python程序/test.py','r') as f:
	print(f.read());

#文件的读取方式
#1.read() 一次性读取所有内容，要注意文件过大会导致内存溢出
#2.read(size) 反复读取size大小的文件流，在不知道文件大小的情况下是保险的选择
#3.readlines() 如果是配置文件，调用readlines最方便
with open('D:/develop/phython/workspace/python-learning/(1)第一个python程序/test.py','r') as f:
	for line in f.readlines():
		print(line.strip());

#file-like Object
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
#除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

#读取二进制文件
with open('E:/图片/壁纸/14521620577052.jpg','rb') as f:
	print(f.read());