#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#利用快捷的方法生成列表
L1 = [x * x for x in range(1,11)];
print(str(L1));

d =  {"a":0,"b":1,"c":2};
L2 = [key+"="+str(value) for key,value in d.items()];
print(str(L2));

L3 = [x * x for x in range(1,11) if x%2 == 0];
print(str(L3));

L4 = [m+n for m in "ABC" for n in "XYZ"];
print(str(L4));

L5_test = ["Hello","World","IBM","Apple"];
L5 = [s.lower() for s in L5_test];
print(str(L5));

#exercise
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
#请让他能够顺利显示出来

L1_exe = ['Hello', 'World', 18, 'Apple', None];
L2_exe = [s.lower() for s in L1_exe if isinstance(s,str)];
print(L2_exe);
if L2_exe == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')