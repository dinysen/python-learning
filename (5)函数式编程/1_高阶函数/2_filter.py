#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#filter函数用于过滤序列
#它与map函数一样将诶手两个参数，第一个是一个函数，第二个是一个Iterable对象
#将定义的函数应用于序列每一项上，返回True保留，返回False删除

#例：保留所有偶数
L = filter(lambda x : (x%2 == 0) , [1,2,3,4,5,6,7,8] );
print(str(list(L)));

#筛选出所有素数
#计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
#首先，列出从2开始的所有自然数，构造一个序列：
#2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#不断筛下去，就可以得到所有的素数。

def odd_iter():
	n = 1;
	while True:		
		n += 2;
		yield n;

def filter_odd(n):
	return lambda x :  x%n > 0 ;

def primes():
	yield 2;
	it = odd_iter();
	while True:
		n = next(it);
		yield n;
		it = filter(filter_odd(n),it);

for x in primes():
	if x < 1000:
		print(x);
	else:
		break;

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

#人家的
def is_palindrome(n):
	str_reverse = int(str(n)[::-1]);
	return n == str_reverse;

#我的
def is_palindrome(n):
	n_str = str(n);
	n_len = len(n_str);
	for i,value in enumerate(n_str):
		if not n_str[i] == n_str[-i-1]:
			break;
		if i == n_len-1:
			return True;
	return False;


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

