#!/usr/bin/env python3 		告诉Linux/OS X系统，这是一个python可执行程序，windows会自动忽略
# -*- coding: utf-8 -*- 	告诉python解释器，按照UTF-8编码读取源代码，否则中文可能会变成乱码

#循环
#(1)for in 循环
names = ["aa","bb","cc"];
for name in names:
	print(name);

#range()函数，生成从0到X的整数序列,可通过list转为数组
rangeTest = range(5);
print(str(list(rangeTest)));

rangeForUse = list(rangeTest);
sum = 0;
for x in rangeForUse:
	sum += x;
print("总计为:",sum);

#(2)while循环
total = 0;
num = 99;
while num > 0:
	total += num;
	num -= 2;
print("利用while语句的累加:",total);

#exercise
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam'];
for names in L:
	print("Hello,%s" % names,"!");

#break 利用break可提前结束循环
n = 1;
while n <= 100:
	if n > 10:
		break;
	print(n);
	n += 1;
print("End");

#continue 利用continue可跳过当前循环
n = 0;
while n < 10:
	n += 1;
	if n%2==0:
		continue;
	print(n);

#死循环程序
test = 0;
while test==0 :
	print("无限死循环");