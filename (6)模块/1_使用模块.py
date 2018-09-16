#标记直接在Unix/Linux/Mac上运行
#!/usr/bin/env python3
#标记编码
#-*- coding: utf-8 -*-

#任何模块的第一个字符串都被视为模块的文档注释
' a test module '

#作者名字，标准模板中的一环
__author__  = 'Dalton Fang'

#导入模块
import sys

def test():
#argv是sys模块的一个特有参数，存储了命令行中的所有参数，它至少长度是1，最少保存了模块的名字
	args = sys.argv
	if len(args) == 1:
		print("Hello World!");
	elif len(args) == 2:
		print("Hello %s" % args[1]);
	else:
		print("Too many arguments");

#当我们用命令行运行此文件时，python解释器会将__name__置为__main__
#而如果在其它地方导入此模块时，if判断就会失败
#因此，通过这种方法就可以进行一些额外代码，最常见的就是运行测试
if __name__ == '__main__':
	test();