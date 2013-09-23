#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
def this_fails():
	x=1/0
try:
	this_fails()
except ZeroDivisionError,detail:
	print 'Handing run-time erro:',detail
##Handing run-time erro: integer division or modulo by zero
