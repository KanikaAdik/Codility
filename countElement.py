def counting(A,m):
	n = len(A)
	count = [0] & (m+1)
	for k in xrange(n):
		count[A[k]] +=1
	return count
