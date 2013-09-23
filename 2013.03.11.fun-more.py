#/usr/bin/python
#-*-coding:utf-8
def fib2(n):	#return Fibonacci series up to n
	"""	Return a list containing the Fibonacci series up to n."""
	result=[]
	a,b=0,1
	while b<n:
		result.append(b)	#see bellow
		a,b=b,a+b
	return result
f100=fib2(100)	#call it
print f100		#write the result
'''
[root@localhost python_study]# python 2013.03.11.fun-more.py 
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
'''
def ask_ok(prompt,retries=4,complaint='Yes or no,please!'):
	while True:
		ok=raw_input(prompt)
		if ok in ('y','ye','yes'):	return 1
		if ok in ('n','no','nop','nope'):	return 0
		retries=retries-1
		if retries <0:	raise IOError,'refusenik user'
		print complaint
ask_ok('Do you really want to quit?')
#ask_ok('OK to overwrite the file?',2)
'''
[root@localhost python_study]# python 2013.03.11.fun-more.py 
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Do you really want to quit?y
[root@localhost python_study]# python 2013.03.11.fun-more.py 
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Do you really want to quit?n
[root@localhost python_study]# python 2013.03.11.fun-more.py 
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Do you really want to quit?dd
Yes or no,please!
Do you really want to quit?dd
Yes or no,please!
Do you really want to quit?dd
Yes or no,please!
Do you really want to quit?de
Yes or no,please!
Do you really want to quit?de
Traceback (most recent call last):
  File "2013.03.11.fun-more.py", line 25, in <module>
    ask_ok('Do you really want to quit?')
  File "2013.03.11.fun-more.py", line 23, in ask_ok
    if retries <0:      raise IOError,'refusenik user'
IOError: refusenik user		
'''

