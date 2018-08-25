#!/usr/bin/env python3 		告诉Linux/OS X系统，这是一个python可执行程序，windows会自动忽略
# -*- coding: utf-8 -*- 	告诉python解释器，按照UTF-8编码读取源代码，否则中文可能会变成乱码

#条件判断
age = 20;
if age >= 18:
	print("年龄为",age);
	print("第一个判断");
elif age == 10:
	print("年龄为",age);
	print("第二个判断");
elif age == 9:
	print("年龄为",age);
	print("第三个判断");
else:
	print("啥都不是",age);

#常见错误	
#需要注意输入的字符为字符串类型，需要手动转换，也可能遇到用户随意输入中英文的问题
inputAge = int(input("请输入你的年龄:"));
if inputAge>=18:
	print("你的年龄为：",inputAge);
	print("符合条件");
elif 15<=inputAge<=18:
	print("你的年龄为",inputAge);
	print("还差两年,不行哟");
else:
	print("你还是个孩子呢");

#exercise
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
height = 1.75;
weight = 80.5;
bmi = weight/(height*height);
if bmi<18.5:
	print("过轻-bmi为%.1f" % bmi);
elif 18.5<=bmi<=25:
	print("正常-bmi为%.1f" % bmi);
elif 25<=bmi<=28:
	print("过重-bmi为%.1f" % bmi);
elif 28<=bmi<=32:
	print("肥胖-bmi为%.1f" % bmi );
else:
	print("严重肥胖-bmi为%.1f" % bmi);