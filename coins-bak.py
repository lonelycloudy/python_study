#给定足够的 5角，2角，1角，5分，2分，1分这六种零钱,将1元(100)换成零钱,一共有多少种换法?
#http://xaajie.iteye.com/blog/461423
def split(n,j,result):  
	v=[200,100,50,20,10,5,2,1]  
	if n<0:  
		return 0  
	if n==0:  
		print "方案："+result  
		return 1  
	if j<0:  
		return 0  
	return split(n,j-1,result)+split(n-v[j],j,result+str(v[j])+"|")  
#split(200,200,"")