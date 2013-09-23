#/usr/bin/python
#-*-coding:utf-8-*-
"""
默认值在函数定义段被解析
"""
i=5
def f(arg=i):
	print arg
i=6
f()
'''
[root@localhost python_study]# python 2013.03.11-func-default.py 
5
重要警告：默认值只会解析一次。当默认值是一个可变对象，
诸如链表、字典或大部分类实例时，会产生一些差异。
例如，以下函数在后继的调用中会积累它的参数值：
'''
def f(a,L=[]):
	L.append(a)
	return L
print f(1)
print f(2)
print f(5)
"""
[root@localhost python_study]# python 2013.03.11-func-default.py 
[1]
[1, 2]
[1, 2, 5]	
如果你不想在不同的函数调用之间共享参数默认值，
可以如下面的实例一样编写函数：
"""	
def f(a,L=None):
	if L is None:
		L=[]
	L.append(a)
	return L
print f(1)
print f(2)
print f(5)
'''
[root@localhost python_study]# python 2013.03.11-func-default.py
[1]
[2]
[5]
'''












