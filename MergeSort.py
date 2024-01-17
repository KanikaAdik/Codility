#time complexity - O9nlogn)

def distinct(A):
	n = len(A)
	A.sort()
	result =1
	for k in xrange(1,n):
		if A[k] !=A[k-1]:
			result +=1
	return result

