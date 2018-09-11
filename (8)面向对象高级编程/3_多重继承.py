#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#例:
class Animal(object):
	pass;

class Mammal(Animal):
	pass;

class Bird(Animal):
	pass;

class RunnableMixIn(object):
	pass;

class FlyableMixIn(object):
	pass;

class Dog(Mammal,RunnableMixIn):
	pass;

class Parrot(Bird,FlyableMixIn):
	pass;