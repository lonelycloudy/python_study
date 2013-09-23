#!/usr/local/python/bin/python
#!-*-coding:utf-8-*-
class MyTest:
	"A Simple example class"
	i=123456
	r=33
	def __init__(self,realpart,imagpart):
		self.data=[]
		self.i = imagpart 
		self.r = realpart 
	def f(self):
		return 'hello,world'
x = MyTest(3.0,-4.5)
print x.r
print x.i
print x.f()
"""
3.0
-4.5
[]
hello,world
"""