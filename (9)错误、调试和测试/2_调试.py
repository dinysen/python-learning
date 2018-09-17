#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#调试的方法
#1.用print将变量打印出来
#用print()最大的坏处是将来还得删掉它，所以有第二种方法

#2.断言assert
#assert 后面的表达式的意思是
#它应该为True程序才能正常运行下去
#否则就抛出异常

#其实assert的方法相比print()好不到哪里去
#不过在运行时可以用-O 关闭 ，如 python -O 2_调试.py
def foo(s):
	n = int(s);
	assert n!= 0,'n is zero!'
	return 10/s;

#foo('0');

#3.logging
#使用logging的好处是可以输出到文件
#可以指定日志级别，指定后只输出此级别的日志
#级别分4种，DEBUG,INFO,WARNING,ERROR
#每一级别只会显示自己及自己等级之上的日志级别
import logging
logging.basicConfig(level=logging.DEBUG)

s = '0';
n = int(s);
logging.info("info : n = %d"%n);
logging.warning("warn : n = %d"%n);
print(10/n);

#后米还有两种用pdb来进行调试的方法，我看效率太低，算了
#后续还是换成Visual Studio Code进行开发吧，安装个python插件