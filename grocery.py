def grocery_store(A):
	n = len(A)
	size, result = 0,0
	for i in xrange(n):
		if A[i] ==0:
			size +=1
		else:
			size -=1
			result = max(result, -size)
	return result
