#!/usr/bin/env python3 		告诉Linux/OS X系统，这是一个python可执行程序，windows会自动忽略
# -*- coding: utf-8 -*- 	告诉python解释器，按照UTF-8编码读取源代码，否则中文可能会变成乱码

#ASCII编码：		1个字节	保存英文字符
#Unicode编码：	2个字节	保存英文与中文字符	英文字符的第一个字节补0即可
#UTF-8编码：		可变字节长度1-6个字节		保存几乎所有字符	英文字母是1个字节	汉字通常是3个字节

#计算机的字符串存储
# 内存[Unicode] <-> 硬盘||传输[UTF-8]
# 服务器[Unicode] <-> 浏览器[UTF-8]

#python3中，字符以Unicode方式存储
integer = ord("中");
print(" ord函数可将字符转为整数 ： ord('中')= "+str(integer));

text = chr(20065);
print(" chr函数可将整数转为对应字符 ： chr(20065)= "+str(text));

#b'XXX说明XXX已经被转换成字节，例如：
print(" '中文'被转换成字节为： "+str('中文'.encode("UTF-8")));

#反过来，如果从网络或者磁盘上读取了字节流，那么获取到的就是bytes，要进行解码
print(" 'ABC'用'ascii'解码： "+str(b'ABC'.decode('ascii')));
print(" '中XX'用'UTF-8'解码： "+str(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')));

#计算一个str包含多少字符，可使用len()函数
#计算bytes拥有多少字节，同样使用len()函数
print(" 计算'范德萨发生的'包含多少字符： "+str(len('范德萨发生的')));
print(" 计算'bXX'包含多少字节： "+str(len(b'\xe4\xb8\xad\xe6\x96\x87')));

#字符串格式化 使用%
# %d -> 整数, %f -> 浮点数, %s -> 字符串, %x -> 十六进制整数
print('%2d-%03d' % (3, 1));
print('%.2f' % 3.1415926);

# 上述还有种方法是使用format函数
test_str = 'Hello,{0},成绩提升{1:.1f}%'.format('小明',17.125);
print(' format函数测试: '+test_str);

#exercise
#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72;
s2 = 85;
r = ((s2 - s1)/s2)*100;
exe_str = '小明提升的成绩为 %.1f%% ' % r ;
exe_str2 = '小明提升的成绩为 {0:.1f}% '.format(r) ;
print(exe_str);