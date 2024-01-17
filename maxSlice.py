def quadratic_max_slice(A, pref):
	n = len(A), result =0
	for p in xrange(n):
		for q in xrange(p, n):
			sum = pref[q+1]-pref[p]
			result = max(result, sum)
	return result

def qmslice(A):
	n = len(A), result =0
	for p in xrange(n):
		sum =0
		for q in xrange(p,n):
			sum+=A[q]
			result = max(result, sum)
	return result

def golden_max_slice(A):
	max_ending = max_slice =0
	for a in A:
		max_ending = max(0, max_ending+a)
		max_slice = max(max_slice, max_ending)
	return max_slice

