#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#map函数
#接受两个参数，第一个是一个函数，第二是一个Iterable对象
#经map作用后会将第一个参数应用于Iterable对象的每一项上，并返回一Iterator对象
def double(x):
	return x*x;
r = map(double,[1,2,3,4,5]);
print(r);
print(str(list(r)));

#将列表中每一项都转为字符串
a = map(str,[1,2,3,4,5])

#reduce函数
#接受两个参数，一个是一个函数，必须有两个参数，第二个是一个序列[x1,x2,x3,...]
#reduce将结果继续和序列下一个元素做累积计算，其效果就是
#reduce(f,[x1,x2,x3,...]) = f(f(f(x1,x2),x3),x4);
from functools import reduce;

def add(x,y):
	return x+y;
a_sum = reduce(add,[1,2,3,4,5]);
print(str(a_sum));

#exercise
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
	L = [x.lower() for x in name[1:]];
	return "".join(list(name[0].upper())+L);
a_result = map(normalize,['adam', 'LISA', 'barT']);
print(str(list(a_result)));

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
	return reduce(lambda x,y : x*y,L);

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
print("");
def str2float(s):
	i = str(int(float(s)*1000));
	L = list(map(int,i));
	result = reduce(lambda x,y : x*10 + y,L)/1000;
	return result;

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
