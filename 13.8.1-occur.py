#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]
for char in reverse('golf'):
	print char
"""
[root@2 python_study]# python 13.8.1-occur.py 
f
l
o
g
"""
