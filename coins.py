#http://xaajie.iteye.com/blog/461423,python,73682
def coins(n,j,result):  
	v=[200,100,50,20,10,5,2,1]  
	if n<0: 
		return 0  
	if n==0:  
		print "method:"+result  
		return 1  
	if j<0:  
		return 0  
	return coins(n,j-1,result)+coins(n-v[j],j,result+str(v[j])+"|")
coins(200,200,"")