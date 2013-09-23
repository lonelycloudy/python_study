#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
try:
	raise KeyboardInterrupt
finally:#run whatever exception occur:relase file link resource,network connection
	print 'Goodbye,world!'
"""
Goodbye,world!
Traceback (most recent call last):
  File "13.7.31-error7.py", line 4, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
"""
