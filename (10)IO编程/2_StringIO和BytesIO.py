#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#数据读写不一定是文件，也可以在内存中读写
#StringIO就是在内存中读取IO
#写
from io import StringIO
f = StringIO();
f.write('Hello!\nHi!\nGoodbye!');
print(f.getvalue());

#读
a = StringIO("A\nB\nC\n");
while True:
	line = a.readline();
	if line == "":
		break;
	print(line);

#如果要操作二进制数据，那么就要使用BytesIO
#写
from io import BytesIO
f = BytesIO();
f.write("中文".encode('utf-8'));
print(f.getvalue());

a = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87');
print(a.read());