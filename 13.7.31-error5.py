#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
try:
	raise NameError,'HiThere'
except NameError:
	print 'An exception flew by!'
	raise
"""
An exception flew by!
Traceback (most recent call last):
  File "13.7.31-error5.py", line 4, in <module>
    raise NameError,'HiThere'
NameError: HiThere
"""