#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#generator
#第一种方式 将列表生成式中的[]换成()
g = (x*x for x in range(10))
print(g);

for n in g:
	print(str(n));

#第二种方式 利用函数生成
#要注意的是，普通的函数试运行到return语句终止
#而到了生成式中，一次next运行到yield终止，下一次从yield开始运行
def fib(max):
	n,a,b = 0,0,1;
	while n<max:
		yield(b);
		a,b = b,a+b;
		# t = (b,a+b);
		# a = t[0]; b = t[1];
		n += 1;
	return "done";

f = fib(6);
#for x in f:
#	print(str(x));

#要想从Generator中获取函数的返回值，那么就要通过捕获错误的方式来实现
while True:
	try:
		x = next(f);
		print("g:",x);
	except StopIteration as e:
		print("Generator returned:"+e.value);
		break;


#exercise
#杨辉三角定义如下
#		   1
#         / \
#        1   1
#       / \ / \
#      1   2   1
#     / \ / \ / \
#    1   3   3   1
#   / \ / \ / \ / \
#  1   4   6   4   1
# / \ / \ / \ / \ / \
#1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：

#这个别人写的
def triangles():
	L = [1];
	while True:
		yield L;
		L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1];


#这是我写的
#def triangles():
#	i = 0;#i是行数
#	last_L = [0];
#	while True : 
#		j,j_max = 0,i+1;
#		L = [];
#		while j < j_max:
#			if j==0 or j==j_max - 1:
#				L.append(1);
#			else:
#				L.append(last_L[j-1]+last_L[j]);
#			j += 1;
#		last_L = L;
#		i+= 1;
#		yield L;

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')



