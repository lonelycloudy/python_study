#!/usr/bin/python
#-*-coding:utf-8-*-
"""
��������ͨ�������ؼ��ֵ���ʽ�����ã����硰keyword = value�������磬���µĺ�����
"""
def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
	print "-- This parrot wouldn't",action,
	print "if you put",voltage,"Volts through it."
	print "-- Lovely plumage,the",type
	print "--It's",state,"!"
"""
���������µ���һ��������:	
"""	
#parrot(1000)
'''
[root@localhost python_study]# python 2013.03.11-param.py 
-- This parrot wouldn't voom if you put 1000 Volts through it.
-- Lovely plumage,the Norwegian Blue
--It's a stiff !
'''
#parrot(action='V00000M',voltage=1000000)
'''
[root@localhost python_study]# python 2013.03.11-param.py 
-- This parrot wouldn't V00000M if you put 1000000 Volts through it.
-- Lovely plumage,the Norwegian Blue
--It's a stiff !
'''
parrot('a thousand',state=' pushing pu th daisies')
'''
[root@localhost python_study]# python 2013.03.11-param.py 
-- This parrot wouldn't voom if you put a thousand Volts through it.
-- Lovely plumage,the Norwegian Blue
--It's  pushing pu th daisies !
'''






















































	