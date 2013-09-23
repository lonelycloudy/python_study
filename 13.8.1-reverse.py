#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
class Reverse:
	"Iterator ofr looping over a sequence backwards"
	def __init__(self,data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index-1
		return self.data[self.index]
for char in Reverse('Spam'):
	print char
"""
[root@2 python_study]# python 13.8.1-reverse.py 
m
a
p
S
"""
