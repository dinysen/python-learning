#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#迭代器
#Iterable对象与Iterator对象

#可直接作用于for循环的是Iterable对象
#如list,tuple,dict,set,str
#generator,包括生成器与带yield的function

#可使用isinstance判断是否是Iterable对象
from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable));
print(isinstance("ABC",Iterable));
print(isinstance((x for x in range(10)),Iterable));
print(isinstance({},Iterable));
print(isinstance(100,Iterable));
print(isinstance(set(),Iterable));

#可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator
#Iterator对象是一个惰性计算的对象
print(isinstance([],Iterator));
print(isinstance((x for x in range(10)),Iterator));
print(isinstance(set(),Iterator));
print(isinstance({},Iterator));

#将list,tuple,dict,set等Iterable变成Iterator可使用iter()函数
print(isinstance(iter([]),Iterator));
print(isinstance(iter({}),Iterator));

#exercise
#杨辉三角变种定义如下
#		   1
#         / \
#        3   3
#       / \ / \
#      5   6   5
#     / \ / \ / \
#    7   11  11   7

#把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
	L = [1];
	while True:
		yield L;
		L = [L[0]+2]+[ L[i]+L[i+1] for i in range(len(L) - 1) ]+[L[0]+2];
n=1;
g = triangles();
while n<10:
	print(str(next(g)));
	n += 1;