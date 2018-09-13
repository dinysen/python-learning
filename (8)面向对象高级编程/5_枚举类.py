#!/usr/bin/env/ python3
#-*- coding: utf-8 -*-

#定义一个枚举类常量
from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'));

for name,member in Month.__members__.items():
	print(name,' => ',member,',',member.value);

for name in Month.__members__:
	print("=>",name);

#如果需要更精确的控制枚举类型，则可以使用Enum的派生类
from enum import Enum,unique
#unique装饰器可以保证类变量中没有重复的值
@unique
class Weekday(Enum):
	Sun = 0;
	Mon = 1;
	Tue = 2;
	Wed = 3;
	Thu = 4;
	Fri = 5;
	Sat = 6;
print(Weekday.Sun);
print(Weekday["Sun"]);
print(Weekday.Sun.value);
print(Weekday(1));
#print(Weekday(7));
for name,value in Weekday.__members__.items():
	print(name,'=>',value);

#exercise
#把Student的gender属性改造为枚举类型，可以避免使用字符串：
class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self, name, gender):
		self.name = name
		if isinstance(gender,Gender):
			self.gender = gender;
		else:
			raise TypeError("gender参数不为Gender类型");

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
	print('测试通过!')
else:
	print('测试失败!')