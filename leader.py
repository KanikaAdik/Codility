#slow

def slowLeader(A):
	n =len(A)
	leader =-1
	for k in xrange(n):
		candidate = A[k]
		count =0
	for i in xrange(n):
		if (A[i[ == candidate):
			count +=1
	if (count>n//2):
		leader = candidate
	return leader

def fastLeader(A):
	n = len(A)
	leader = -1
	A.sort()
	candidate = A[n//2]
	count =0
	for i in xrange(n):
		if (A[i] == candidate):
			count +=1
	if (count> n//2):
		leader = candidate
	return leader


def golderLeader(A):
	n = len(A) 
	size =0
	for k in xrange(n):
		if (size ==0):
			size +=1
			value = A[k]
		else:
			if (value !=A[k]):
				size -=1
			else:
				size +=1
	candidate =-1
	if size>0
		candiddate = value
	leader = -1
	count =0
	for k in xrange(n):
		if (A[k] == candidate):
			count+=1
	if (count> n//2)
		leader =candidate
	return leader
