#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
import string
for x in range(1,11):
	print string.rjust(repr(x),2),string.rjust(repr(x*x),3),
	#Note trailing comma on previous line
	print string.rjust(repr(x*x*x),4)
"""
[root@localhost python_study]# python 13.7.31-sq.py 
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
"""
print '%2s' %('  ')
for x in range(1,11):
	print '%2d %3d %4d' % (x,x*x,x*x*x)