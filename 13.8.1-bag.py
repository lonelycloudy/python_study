#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
class Bag:
	def __init__(self):
		self.data=[]
	def add(self,x):
		self.data.append(x)
	def addtwice(self,x):
		self.add(x)
		self.add(x)
bag = Bag()
bag.add(12)
bag.addtwice(23)
print bag.data
"""
[12, 23, 23]
"""

