def fast_solution(A, B, m):
	n = len(A)
	sum_a = sum(A)
	sum_b = sum(B)
	d = sum_b- sum_a
	if d%2 ==1:
		return False
	d//=2
	count = counting(A,m)
	for i in xrange(n):
		if 0< B[i] -d and B[i]  -d <=m and count[B[i]-d]>0:
			return True
	return False

