#!/usr/local/python/bin/python
#-*-coding:utf-8-*-
#f = open('/tmp/a.log','rb');
f = open('/tmp/a.log','r+');
#print f
"""
<open file '/tmp/a.log', mode 'w' at 0xb7fb8c28>
"""
#print f.read()
"""
hello,world!
"""
#print f.readline()
#print f.readline()
"""
this is the first line:hello,world!
this is the second line:come on man 
"""
#print f.readlines()
"""
['this is the first line:hello,world!\n', 'this is the second line:come on man \n']
"""
f.write("The third line:is write by code")
print f.readlines()
"""
['The third line:is write by code']
"""
f.seek(4)#Go to the 6th byte in the file
print f.read(1)
f.seek(-3,2)#Go to the 3rd byte before the end
print f.read(1)
f.close()
f.read()






