#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
class MyCounter:
	"A Simple example class"
	i=123456
	r=33
	def __init__(self,realpart,imagpart):
		self.data=[]
		self.i = imagpart 
		self.r = realpart 
	def f(self):
		return 'hello,world'
x = MyCounter(3.0,-4.5)
x.counter = 1;
while x.counter < 10:
	x.counter = x.counter * 2
print x.counter
del x.counter
print "D"
print x.counter
"""
16
D
Traceback (most recent call last):
  File "13.8.1-object.py", line 20, in <module>
    print x.counter
AttributeError: MyCounter instance has no attribute 'counter'
"""