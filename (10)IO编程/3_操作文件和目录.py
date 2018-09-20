#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#操作文件和目录
import os
#如果是posix代表Linux，Unix或Mac OS X
#如果是nt代表Windows
print(os.name);

#windows下没有这方法，说明os有的方法还是得根据系统来搞得
#print(os.uname());

#环境变量
#在操作系统中定义的环境变量，全部保存在os.environ这个变量中
#print(os.environ);
#这东西返回的就是一个map
print(os.environ.get('PATH'));

#操作文件和目录
print(os.path.abspath('.'));
path = os.path.join('D:/develop/phython/workspace/python-learning/(10)IO编程','bb');
#删除文件夹
os.rmdir(path);
#创建文件夹
os.mkdir(path);

#合并路径与拆分路径
#os.path.join() 和 os.path.split()
#用这两个方法的目的是能够正确处理不同系统下的路径分隔符问题
#这两个方法只是单纯的对字符串做操作，不涉及操作系统方法
path2 = os.path.split(path);
print(path2);

postfix = os.path.splitext(path+"%s" % "\\aa.txt");
print(postfix[0],postfix[1]);

#对文件做操作
open("test.txt","a");
os.rename('test.txt','test.py');
#删掉文件
os.remove('test.py');
#如果要复制文件，使用shutil中的copyfile()函数
#shutil中还有许多实用函数，可以看做是os模块的补充

#获取当前目录下的所有目录
print([x for x in os.listdir(".") if os.path.isdir(x) ]);

#列出所有.py文件
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py" ]);

#exercise
#利用os模块编写一个能实现dir -l输出的程序。
print([dirpath for dirpath in os.walk("D:/develop/phython/workspace/python-learning")]);


#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。