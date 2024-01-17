def slow_solution(A, B, m):
	n = len(A)
	sum_a = sum(A)
	sum_b = sum(B)
	for i in xrange(n)
		for j in xrange(n):
			change = B[j[- a[i]
			sum_a += change
			sum_b+= change
			if sum_a == sum_b:
				return True
			sum_a -= change
			sum_b += change
	return False
