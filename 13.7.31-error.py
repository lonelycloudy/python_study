#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
while True:
	try:
		x=int(raw_input("Please enter a number:"))
		break
	except ValueError:
		print "Oops! That was no valid number. Try again..."
"""
Please enter a number:k
Oops! That was no valid number. Try again...
Please enter a number:3
"""
