#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (1)位置参数 函数中一个钉子一个坑就是位置函数
def power(x,n):
	s = 1;
	while  n>0 : 
		n -= 1;
		s *= x;
	return s;

print(str(power(5,3)));

# (2)默认参数 可以用来简化重载函数的代码实现,必须是必选参数在前，默认参数在后
def power_default(x,n=2):
	s = 1;
	while n>0:
		n -= 1;
		s *= x;
	return s;
print(str(power_default(5)));

# 带默认参数的函数的调用方式有两种
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll("张三","男","8"); #按顺序填写
enroll("李四","女",city = "上海"); #手动设置值

# 默认参数必须指向不可变对象
def add_end(L = []):
	L.append("END");
	return L;
print(str(add_end()));
 #这里就会出现错误，因为L的值已经在上一次调用中被改变了
print(str(add_end()));

#纠正上述函数
def add_end_right(L = None):
	if L is None:
		L = [];
	L.append("END");
	return L;
print(str(add_end_right()));
print(str(add_end_right()));

# (3)可变参数
def calc(*numbers):
	s = 0;
	for x in numbers:
		s += x;
	return s;
print(calc(1,3,5,7));
print(calc());

# 如果已经拥有一个list或tuple，想要调用可变参数函数咋办呢
testList = [1,2,3,4];
print(calc(*testList));

# (4)关键字参数
# 注：关键字参数获取的dict只是传入参数值的一份拷贝，对关键词参数做处理不会影响原来的值
def person(name,age,**kw):
	print("name: ",name,"age: "+str(age),"kw: "+str(kw));

person("张三",10,gender="M",city="上海");

testDict = {"gender":"F","city":"北京"};
person("李四",18,**testDict);

# (5)命名关键词参数
# 限定可变参数中必须包含的参数值
# 普通写法
def person_changeable(name,age,*,city,job):
	print(name,age,city,job);
person_changeable("张三",10,city="上海",job="码农");

# 如果函数直接包含可变参数,命名关键字后必须加入变量名，与位置参数不同
# 命名关键字中也可使用默认值
def person_changeable2(name,age,*args,city = "北京",job):
	print(name,age,city,job);
person_changeable2("张三",10,job = "码农");


# (6)参数组合
# 必须按照 必选参数 - 默认参数 - 可变参数 - 命名关键字参数 - 关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 通过tuple和dict，也可以调用上述参数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

#exercise
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
#def product(x, y):
#	return x * y

def product(*args):
	if len(args) == 0:
		raise TypeError("不可以不传入参数");
	s = 1;
	for x in args:
		if not isinstance(x,(int,float)):
			raise TypeError("每一项都应该是数字");
		s *= x;
	return s;

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')