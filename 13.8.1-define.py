#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
#Function defined outside the class

def f1(self,x,y):
	return min(x,y)
class C:
	f = f1
	def g(self):
		return 'hello,world'
	h=g
x = C()
xf1 = x.f
print xf1(23,10)
print x.h()
"""
10
hello,world
"""