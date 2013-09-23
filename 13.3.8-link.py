#link table
a=['spam','eggs',100,1234]
print len(a)
##4
print a
##['spam', 'eggs', 100, 1234]
##slice link
print a[0]
##spam
print a[-2]
##100
print a[1:-1]
##['eggs', 100]
print a[:2]+['bacon',2*2]
##['spam', 'eggs', 'bacon', 4]
print 3*a[:3]+['Boe!']
##['spam', 'eggs', 100, 'spam', 'eggs', 100, 'spam', 'eggs', 100, 'Boe!']
##replace som items
a[0:2]=[1,12]
print a
##[1, 12, 100, 1234]
#remove some:
a[0:2]=[]
print a
##[100, 1234]
#insert some
a[1:1]=['betch','xyzzy']
print a
##[100, 'betch', 'xyzzy', 1234]
#insert (a copy of) itself at the beginning
a[:0]=a
print a
##[100, 'betch', 'xyzzy', 1234, 100, 'betch', 'xyzzy', 1234]
#inner link
q=[2,3]
p=[1,q,4]
print len(p)
##3
print p
##[1, [2, 3], 4]
print p[1]
##[2, 3]
print p[1][0]
##2
p[1].append('xtra')
print p
##[1, [2, 3, 'xtra'], 4]
print q
##[2, 3, 'xtra']