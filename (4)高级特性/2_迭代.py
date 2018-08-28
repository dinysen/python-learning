#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#对于可迭代对象，通过for ... in ...进行迭代
#对map的三种迭代
d = {"a":0,"b":1,"c":2};
for key in d:
	print(key,d.get(key));

for value in d.values():
	print(value);

for key,value in d.items():
	print(key,value);

#对字符串也可进行迭代
for ch in "ABC":
	print(ch);

#如何判断一个对象是否可迭代呢
from collections import Iterable
print(str(isinstance("ABC",Iterable)));

#如何进行下标循环呢,利用enumerate函数
for i,value in enumerate("ABC"):
	print(i,value);

for x,y in [(1,"A"),(2,"B"),(3,"C")]:
	print(x,y);

#exercise
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
	min = 0;
	max = 0;
	if len(L) == 0:
		return (None,None);
	for i,value in enumerate(L):
		if i==0:
			min = value;
			max = value;
		if value<=min:
			min = value;
		if value>= max:
			max = value;
	return (min,max);

if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!');
else:
    print('测试成功5!')