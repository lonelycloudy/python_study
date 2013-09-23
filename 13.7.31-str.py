#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
import string 
print string.ljust('1234567',3)[0:2]
print string.zfill('12',5)
"""
12
00012
"""
print string.zfill('-3.14',7)
print string.zfill('3.14159265359',7)
"""
-003.14
3.14159265359
"""
import math
print 'The value of PI is approximately %5.3f.' % math.pi
"""
The value of PI is approximately 3.142.
"""
table = {'Sjoerd':4127,'Jack':4098,'Dcab':7628}
for name,phone in table.items():
	print '%-10s==>%10d' % (name,phone)
"""
Dcab      ==>      7628
Jack      ==>      4098
Sjoerd    ==>      4127
"""
table = {'Sjoerd':4127,'Jack':4098,'Dcab':8637678}
print 'Jack:%(Jack)d; Sjoerd:%(Sjoerd)d; Dcab:%(Dcab)d' % table
"""
Jack:4098; Sjoerd:4127; Dcab:8637678
"""



