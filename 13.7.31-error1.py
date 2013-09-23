#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
import string,sys

try:
	#f = open("/tmp/a.log")
	f = open("/tmp/pythonerror.log")
	s = f.readline()
	i = int(string.strip(s))
	print i
except IOError,(errno,strerror):
	print "I/O error(%s): %s" % (errno,strerror)
except ValueError:
	print "Could not convert data to an integer."
except:
	print "Unexpected error:",sys.exc_info()[0]
	raise
"""
[root@localhost python_study]# python 13.7.31-error1.py 
Could not convert data to an integer.
[root@localhost python_study]# python 13.7.31-error1.py 
12
"""