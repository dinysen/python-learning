#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
def iter_odd():
    n=1;
    while True:
        n+=2;
        yield n;

def _filter(n):
    return lambda x : x%n > 0;

def aishi():
    yield 2;
    it = iter_odd();
    while True:
        g = next(it);
        yield g;
        it = filter(_filter(g),it);

for x in aishi():
    if x < 1000:
        print(x);
    else:
        break;



#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    return n == int(str(n)[::-1]);

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#exercise
#利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():

	def plus_step():
		n = 1;
		while True:
			yield n;
			n +=1;
	it = plus_step();

	def reFun():
		return next(it);
	return reFun;

counterA = createCounter();
print(counterA(), counterA(), counterA(), counterA(), counterA());

counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
