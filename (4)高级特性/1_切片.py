#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#切片语法 [][a:b:c]
# a开始index
# b结束index，但不包括b的索引
# c每隔多少个取

L = ['michael','sarah','tracy','bob','jack'];

print(str(L[0:2]));
print(str(L[0:]));#不填写b代表b=0
print(str(L[:2]));#不填写a代表a=0
print(str(L[::2]))#每两个取一个

L1 = list(range(100));
print(str(L1[0:10]));
print(str(L1[-10:]));
print(str(L1[10:20]));
print(str(L1[:]));#什么都不填代表原样复制一个list

#tuple同理，只不过返回的是tuple
#str同理，字符串的切片操作相当于java中的substring方法

#exercise
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
#这是我写的
def trim(s):
	s_test = set([' ']);
	start = 0;
	end = len(s);
	i = 1;
	while i<end:
		s_str = s[start:i];
		str_set = set(s_str);
		if len(s_test | str_set)>1:
			break;
		else :
			i += 1;
	start = i - 1;

	j=-1;
	while j>-end:
		s_str = s[j:];
		str_set = set(s_str);
		if len(s_test | str_set)>1:
			break;
		else :
			j -= 1;
	end = j+end+1;
	return s[start:end];

#这是人家写的，你自己看着办吧
def trim(s):
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s

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



