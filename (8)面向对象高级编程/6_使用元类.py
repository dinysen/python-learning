#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#元类
#python中的类与函数都是动态创建的
#也就意味着在运行时，我们能够通过某种方法动态的创建类
#这个方法就是type()函数
#例
def fn(self,name='Delton'):
	print("Hello,%s" % name);

#type()函数的第一个参数是class的名称
#第二个参数是父类，注意python支持多重继承，所以要注意tuple单元素的写法
#第三个参数就是定义内部方法
Hello = type('Hello',(object,),dict(hello=fn));
h = Hello();
h.hello();
h.hello('Alice');



