#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#排序算法 sorted
#同样接收两个参数，第一个参数是一个序列，第二个参数是一个key函数

L1 = sorted([1,-2,3,-8,5]);
print(str(list(L1)));

#例：按绝对值从小到大排序
L2 = sorted([1,-2,3,-8,5],key=abs);
print(str(list(L2)));

#如果要反向排序，可以加入reverse=True参数
L3 = sorted([1,-2,3,-8,5],key=abs,reverse=True);
print(str(list(L3)));

#exercise
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0].lower();

L4 = sorted(L, key=by_name)
print(str(list(L4)));

def by_score(t):
	return t[1];
L5 = sorted(L, key=by_score,reverse=True);
print(str(list(L5)));