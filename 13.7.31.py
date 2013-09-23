#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
#The argument to repr() may be an Python object:
x = 10*3.25
y = 200*200 
print repr((x,y,('spam','eggs')))
#reverse quotes are convenient in interactive sessions:
print `x,y,('spam','eggs')`