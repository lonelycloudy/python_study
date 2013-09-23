#!/usr/local/python/bin/python
#-*-coding:utf8-*-
import string
import pickle

a = '10'
print a
print string.atoi(a)
x = '{my:1,you;2}'
f = open('/tmp/pickle.log','r+')
pickle.dump(x,f)
"""
[root@localhost python_study]# cat /tmp/pickle.log 
S'{my:1,you;2}'
p0
"""
f = open('/tmp/pickle.log','rb')
x = pickle.load(f)
print x
"""
{my:1,you;2}
"""