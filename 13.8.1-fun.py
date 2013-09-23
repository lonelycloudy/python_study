#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
class Myfun:
	i=1
	def f(self):
		return 'hello,world'
	#f=2 will reload function 
x = Myfun()
xf = x.f
while x.i<3:
	x.i =x.i+1
	print xf()
print Myfun.f(x)
"""
[root@2 python_study]# python 13.8.1-fun.py 
hello,world
hello,world
hello,world
"""
"""
while True:
	print xf()
hello,world
..........
"""