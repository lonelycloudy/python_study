#/usr/bin/python
#-*-coding:utf-8-*-
"""
如果你退出Python解释器重新进入，
以前创建的一切定义（变量和函数）就全部丢失了
因此:脚本->解释器
模块是包括Python定义和声明的文件
文件名就是模块名加上.py后缀。
模块的模块名（做为一个字符串）
可以由全局变量__name__得到。

"""
#Fibonacci numbers module
def fib(n):
	a,b=0,1
	while b<n:
		print b,
		a,b=b,a+b
def fib2(n):
	result=[]
	a,b=0,1
	while b<n:
		result.append(b)
		a,b=b,a+b
	return result
'''
[root@localhost model]# python 
Python 2.7 (r27:82500, Apr 13 2012, 16:56:11) 
[GCC 4.1.2 20080704 (Red Hat 4.1.2-52)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import fibo
这样做不会直接把fibo中的函数导入当前的语义表
；它只是引入了模块名fibo。
你可以通过模块名按如下方式访问这个函数：
>>> fibo.fib(100)
1
1
2
3
5
8
13
21
34
55
89
>>> fibo.__name__
'fibo'
>>> fibo.fib2(23)
[1, 1, 2, 3, 5, 8, 13, 21]
'''	






























