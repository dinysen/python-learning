#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#exercise
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
#(1)显示%,需要转译
percent = (85 - 72)/85 *100 ;
print("小明成绩提升了%.1f%%" % percent );

#exercise
#请用索引取出下面list的指定元素：

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
];

# 打印Apple:
print("打印%s" % L[0][0]);
print("打印{0}".format(L[0][0]));
# 打印Python:
print("打印%s" % L[1][1]);
print("打印{0}".format(L[1][1]));
# 打印Lisa:
print("打印%s" % L[2][2]);
print("打印{0}".format(L[2][2]));

#exercise
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
bmi = 80.5 / (1.75*1.75);
if bmi < 18.5:
	print("过轻,bmi = %d" % bmi);
elif 18.5 <= bmi < 25:
	print("正常,bmi = %d" % bmi);
elif 18.5 <= bmi < 25:
	print("过重,bmi = %d" % bmi);
elif 18.5 <= bmi < 25:
	print("肥胖,bmi = %d" % bmi);
else :
	print("严重肥胖,bmi = %d" % bmi);

# exercise
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数

import math;
def quadratic(a, b, c):
	if not isinstance(a,(int,float)):
		raise TypeError("a必须为数字");
	if not isinstance(a,(int,float)):
		raise TypeError("b必须为数字");
	if not isinstance(a,(int,float)):
		raise TypeError("c必须为数字");
	res = b*b-4*a*c;
	res_sqrt = math.sqrt(res);
	if res < 0:
		return "无实数解";
	elif res == 0:
		return "任意实数解";
	else:
		r1 = (res_sqrt-b)/(2*a);
		r2 = (-res_sqrt-b)/(2*a);
		return r1,r2;

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

#exercise
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
#def product(x, y):
#	return x * y
def  product(*args):
	if len(args) == 0:
		raise TypeError("传入参数错误");
	x = 1;
	for n in args:
		x *= n;
	return x;

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

#exercise
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
	while s[:1]==' ':
		s = s[1:];
	while s[-1:]==' ':
		s = s[:-1];
	return s;

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

#exercise
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
	if(len(L) == 0):
		return None,None;
	min = L[0];
	max = L[0];
	for x in L:
		min = x if x < min else min;
		max = x if x > max else max;
	return min,max;

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

#exercise
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
#请让他能够顺利显示出来

L1_exe = ['Hello', 'World', 18, 'Apple', None];
L2_exe = [x.lower() for x in L1_exe if isinstance(x,str)];
if L2_exe == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

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
def triangles():
	n = [1];
	while True:
		yield n;
		n = [1]+[ n[x]+n[x+1] for x in range(len(n)-1) ]+[1];

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

#exercise
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    first_letter = name[0].upper();
    other_letter = [ x.lower() for x in name[1:] ];
    return first_letter+"".join(other_letter);
print(str(list(map(normalize,['adam','LISA','barT']))));

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce;
def prod(L):
    a = reduce(lambda x,y : x*y,L);
    return a;

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    dot_index = s.index(".");
    n = 1;
    multi = 1;
    while n<dot_index:
        multi *= 10;
    L_int = map(int,s.pop(dot_index));
    L = reduce(lambda x,y : x*10+y,L_int);
    L /= multi;

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

