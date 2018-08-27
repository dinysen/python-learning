#!/usr/bin/env python3 		告诉Linux/OS X系统，这是一个python可执行程序，windows会自动忽略
# -*- coding: utf-8 -*- 	告诉python解释器，按照UTF-8编码读取源代码，否则中文可能会变成乱码

#dict 在其它语言中被称为map
d = {"aa":95,"bb":100,"cc":105};
print(d["aa"]);

#放入内容
d["dd"] = 110;
print(d["dd"]);

#判断key在dict中是否存在
print(str("dd" in d));

#可通过dict的get方法在key值不存在时返回自己定义的值
d.get("dd")
print(str(d.get("ee")),str(d.get("ee","default_value")));

#删除key,并返回这个key对应的值
print(str(d.pop("dd")));

#set 是一组key的集合，每个key不能重复,但是它不存储value,set也是无序的
#初始化set
s = set([1,2,3]);
print(str(s),str(list(s)));

#添加元素
s.add(4);
s.add("4");
print(str(s));

#删除元素
s.remove("4");
print(str(s));


#set的交集
s1 = set([1,2,3,4]);
s2 = set([3,4,5,6]);
s3 = s1 & s2;#交集
s4 = s1 | s2;#并集
print(s3,s4);

#尝试将list放入set
testList = [[1,2],2,3];
#sTest = set(testList);
#print(sTest);

#tuple作为一个不可变对象，是否能加入set
testTuple = (1,);
testList2 = [testTuple,2];
sTest2 = set(testList2);
print(sTest2);

testTuple2 = (1,[1,2]);
testList3 = [testTuple2]
sTest3 = set(testList3);
print(sTest3);

