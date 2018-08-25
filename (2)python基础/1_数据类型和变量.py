# -*- coding: utf-8 -*-
#数值类型
#1 整数	python可处理任意大小的整数
#2 浮点数 没有大小限制 但超出范围就是inf
#整数运算永远是精确地
#浮点数运算会有四舍五入的误差 
print(1.23e9);


#3 字符串
print('I\'m OK');
print("I'm OK");
print("Here is a \t tab");#转义tab
print(r'Here is a \t tab');#r''表示不转译tab
print('''line1line2line3''');

#4 bool值
print("True && True = "+str(True and True));
print("True && False = "+str(True and False));
print("False && False = "+str(False and False));

print("True || False = "+str(True or False));

print("not True = " + str(not True));

#5 null
print("python中的空值为: "+str(None));

#6 变量 要时刻记得，赋值操作只是在内存中生成了两个值，a->值所在的内存地址
a = 1;
b = "AAA";
c = True;

#7 常量 python中没有常量，只是习惯上的写法
PI = 3.14159265359

#8 python中的除法
print("10/3 = "+str(10 / 3));
print("10//3 = "+str(10 // 3)); #取整
print("10%3 = "+str(10 % 3)); #取余

print(r'Hello, "Bart"');