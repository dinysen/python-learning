#!/usr/env/bin/ python3
#-*- coding:utf-8 -*-

#序列化
#就是将变量从内存中变成可存储的或者可传输的
#pickle.dumps 是将任意一个对象序列化
#pickle.dump 是将对象转成一个file-like对象
import pickle;
with open("pickle.txt","ab") as f:
	d = dict(name='Dalton',age=26,score=88);
	print(pickle.dumps(d));
	pickle.dump(d,f);

#反序列化的方法
#pickle.loads() 将任意的bytes反序列化
#pickle.load() 将一个file-like object反序列化
with open("pickle.txt","rb") as f:
	d = pickle.load(f);
	print(d);

#JSON格式
#python数据结构与JSON对照
# {} <=> dict
# [] <=> list
# "string" <=> str
# 1234.56 <=> int/float
# true/false <=> True/False
# null <=> None
import json;
b = dict(name="Dalton",age=20,gender="男");
json_str = json.dumps(b);

a = json.loads(json_str);
print(a);

#将类实例转换为json对象
class Student(object):
	def __init__(self,name,age,gender):
		self.name = name;
		self.age = age;
		self.gender = gender;

def stu2student(obj):
	return {
		"name" : obj.name,
		"age" : obj.age,
		"gender" : obj.gender
	}

stu = Student("Dalton3",18,"男");
stu_json = json.dumps(stu,default=stu2student);
#此方法为通用方法，对于那些一般的class都能用，除了有__slots__属性的不行
stu_json_2 = json.dumps(stu,default=lambda x : x.__dict__);
print(stu_json);
print(stu_json_2);

def dict2Stu(std):
	return Student(std["name"],std["age"],std["gender"]);
stu_load = json.loads(stu_json,object_hook=dict2Stu);
print(stu_load);

#exercise
#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
#ascii不是真正的中文
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s);