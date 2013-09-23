#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
print "refer"
a = [1,2,3]
print a
print id(a)
b = a
print id(b)
a[1]=6
print a
print b
print "copy"
a = [1,2,3]
b = a[:]
a[1] =6
print a
print b
"""
refer
[1, 2, 3]
3085248492
3085248492
[1, 6, 3]
[1, 6, 3]
copy
[1, 6, 3]
[1, 2, 3]
"""
import time
a = time.strtime('%Y-%m-%d',time.localtime(time.time()))
print a