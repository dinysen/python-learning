#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 自己定义一个函数，使用def
def my_abs(x):
	if x<0:
		return -x;
	else:
		return x;

print(my_abs(-99));

# 空函数 可用作占位符
def empty():
	pass;

# 对错误情况进行处理
def advanced_my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError("传入的参数类型错误");
	if x < 0:
		return -x;
	else:
		return x;
inputOne = 1;
print(advanced_my_abs(inputOne));

# 一个函数拥有多个返回值，返回值的类型为tuple
import math;

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle);
	ny = y - step * math.sin(angle);
	return nx,ny

r =  move(100,100,60,math.pi / 6);
print(r);

x,y = move(100,100,60,math.pi / 6);
print(x,y);

# exercise
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数
def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError("a必须为数字");
	if not isinstance(b,(int,float)):
		raise TypeError("b必须为数字");
	if not isinstance(c,(int,float)):
		raise TypeError("c必须为数字");
	M = b*b-4*a*c;
	if M == 0:
		return "任意实数解";
	elif M < 0:
		return "无解";
	else:
		r1 = (-b + math.sqrt(M))/(2*a);
		r2 = (-b - math.sqrt(M))/(2*a);
	return r1,r2;

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')