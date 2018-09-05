#!/usr/bin/env python3
# -*- coding : utf-8 -*-

#偏函数
import functools
int2 = functools.partial(int,base=2);
int_test = int2("01000000");
print(str(int_test));

#functools.partial的作用就是，把一个函数的某些参数给固定住(也就是设置默认值),返回一个新的函数
#已经固定住的参数，也可以在函数调用时传入其他值
int_test_2 = int2("01000000",base=10);
print(str(int_test_2));

#创建偏函数，其实就是接收 函数对象、*args、**kw 三个参数
int2 = functools.partial(int,base=2);#遇到这种就是关键字参数固定
=> int(XX,{base:2});

int3 = functools.partial(int,10);#遇到这种就是移到可变参数第一位
=> int(10,XX);