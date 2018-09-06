#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#面向对象编程
#类和实例

#括号中的object是继承自什么类
class Student(object):

	#相当于构造函数，变量前的__代表这个属性为private属性
	#__init__函数的self参数代表实例化对象本身
	def __init__(self,name,score):
		self.__name = name;
		self.__score = score;

	#属性前的__代表私有变量，在python3中会解释成_Student__XX属性
	#需要注意的是，就算你在实例中添加了一个__XX的属性，与上面那个也不是同一个属性了
	#一个属性一般对应着get与set方法，通过变量访问限制保护，代码更加健壮
	#还能够再set方法中直接添加限制条件
	def set_score(self,score):
		if 0<=score<=100:
			self.__score = score;
		else :
			raise ValueError("错误的分数");

	#内部方法可以直接通过self来获得实例的内部参数
	def get_score(self):
		return self.__score;

	

stu = Student("dalton",99);
stu.get_score();

#exercise
#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student2(object):
	def __init__(self, name, gender):
		self.__name = name;
		self.__gender = gender;

	def set_gender(self,gender):
		if ("male"!=gender and "female"!=gender) :
			raise ValueError("性别不对");
		else:
			self.__gender = gender;

	def get_gender(self):
		return self.__gender;

bart = Student2('Bart', 'male');
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female');
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')