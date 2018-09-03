#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#匿名函数
#lambda x : x*y; 
#只能有一行表达式

#exercise
#请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1



L = list(filter(lambda n : n%2 == 1, range(1, 20)))
print(str(L));