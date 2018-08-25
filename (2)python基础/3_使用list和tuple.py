#!/usr/bin/env python3 		告诉Linux/OS X系统，这是一个python可执行程序，windows会自动忽略
# -*- coding: utf-8 -*- 	告诉python解释器，按照UTF-8编码读取源代码，否则中文可能会变成乱码

#list
classmates = ['张三','李四','王五'];
print(" 数组的字符串形式: "+str(classmates));
print(" 获取数组的长度方法: "+str(len(classmates)));
print(" 正向获取数组的元素: "+classmates[0]+":"+classmates[1]+":"+classmates[2]);
print(" 反向获取数组的元素: "+classmates[-1]+":"+classmates[-2]+":"+classmates[-3]);

#list是一个可变的有序表
#(1)向末尾添加元素
classmates.append("aa");
print(" 向末尾添加元素： "+str(classmates));

#(2)向指定索引位置添加元素
classmates.insert(1,"bb");
print(" 向指定索引位置添加元素： "+str(classmates));

#(3)删除list末尾的元素并返回
deleteOne = classmates.pop();
print(" 删除list末尾的元素： "+str(classmates) + "\n 返回的元素为："+deleteOne);

#(4)要删除指定索引的元素并返回
deleteAnother = classmates.pop(0);
print(" 删除list指定的元素： "+str(classmates) + "\n 返回的元素为："+deleteAnother);

#(5)将某一位置的元素替换
classmates[0] = "cc";
print(" 替换第一个元素后的数组： "+str(classmates));

#(6)list中的数据元素的类型可以不同
testlist = ["aa",2,True,["bb","cc"]];


#tuple 元祖，即数组中定义的每项内容的指向都不会改变
#(1)
tupleOne = (1,2,3);
print(" 第一个tuple: "+str(tupleOne));

#(2)只有一项的tuple
# X
tupleTwo = (1);
print(" 只有一项的tuple(错误示例): "+str(tupleTwo));
tupleTwo = (1,);
print(" 只有一项的tuple(正确示例): "+str(tupleTwo));

#(3)"可变"的tuple
tupleThree = (1,2,["a","b"]);
print(" 原来的tuple： "+str(tupleThree));
tupleThree[2][0] = "c";
tupleThree[2][1] = "d";
print(" 变化后的tuple： "+str(tupleThree));

#exercise
#请用索引取出下面list的指定元素：

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
];

# 打印Apple:
print("打印Apple:%s" % L[0][0]);
print("打印Apple:{0}".format(L[0][0]));
# 打印Python:
print("打印python:%s" % L[1][1])
# 打印Lisa:
print("打印python:%s" % L[2][2]);