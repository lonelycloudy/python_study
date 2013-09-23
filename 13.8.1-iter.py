#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
for element in [1,2,3]:
	print element
for element in (4,5,6):
	print element
for key in {'one':1,'two':2}:
	print key
for char in "789":
	print char
for line in open("/tmp/a.log"):
	print line
"""
1
2
3
4
5
6
two
one
7
8
9
The third line:is write by code
"""
s = 'abc'
it = iter(s)
print it
a=0
while(a < 4):
	a=a+1
	print it.next()
"""
<iterator object at 0xb7ed7a8c>
a
b
c
Traceback (most recent call last):
  File "13.8.1-iter.py", line 33, in <module>
    print it.next()
StopIteration
"""
