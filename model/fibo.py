#/usr/bin/python
#-*-coding:utf-8-*-
"""
������˳�Python���������½��룬
��ǰ������һ�ж��壨�����ͺ�������ȫ����ʧ��
���:�ű�->������
ģ���ǰ���Python������������ļ�
�ļ�������ģ��������.py��׺��
ģ���ģ��������Ϊһ���ַ�����
������ȫ�ֱ���__name__�õ���

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
����������ֱ�Ӱ�fibo�еĺ������뵱ǰ�������
����ֻ��������ģ����fibo��
�����ͨ��ģ���������·�ʽ�������������
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






























