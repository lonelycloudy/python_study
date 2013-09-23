#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
class BaseClass:
	def __init__(self):
		self.data = [1]
	def s_i(self,x):
		return 'Parent',x
		
class DerivedClass(BaseClass):
	def __init__(self):
		self.data = [2]
	def s_i(self,x):
		return 'Child',x

dev = DerivedClass()
print dev.s_i(11)
base = BaseClass()
print base.s_i(22)
"""
('Child', 11)
('Parent', 22)
"""