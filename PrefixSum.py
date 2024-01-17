
A = [2,3,4,5,6]

#total of first n+1 vlaues
def prefix_sums(A):
	n = len(A)
	P = [0] * (n+1)
	for k in xrange(1, n+1):
		P[k] = P[k-1] +A[k-1]
	return P

#total of last k values suffix sum
def count_total(P, x, y):
	return P[y+1] - P[x]


A = [2,3,7,5,1,3,9]
pos = [0,1,2,3,4,5,6]
k = 4 #spot location of k start 
m = 6 #no of moves to collect max no of mushrooms 
#mushroom picker should not chnage direction more than once, Best strategy O(m2)  
#make m movies in one direction,m-p moves in opposite direction 
#sol (n+m) - using prefix sums 
#if we make p moves in one direction max oppposite location 

#maximal opposite location of mushroom picker
# m picker collects all m between these extremes
# total no of colelcted m in constant time using prefix sums



def mushrooms(A, k, m):
	n = len(A)
	result =0
	pref = prefix_sums(A)
	for p in xrange(min(m, k) +1):
		left_pos = k -p 
		right_pos = min(n-1, max(k,k +m -2*p))
		result = max(result, count_total(pref, left_pos, right_pos))
	for p in xrange(min(m,k) +1):
		right_pos = k+p
		left_pos = max(0, min(k,k-(m-1*p)))
		result = max(result, count_total(pref, left_pos, right_pos))
	return result

