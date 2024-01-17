#number a is a divisor of n then n/a is also a divisor
#one of thse two divisors is less than or equal to \/n

def divisors(n):
	i =1
	result =0
	while(i*i <n):
		if (n%i ==0):
			result +=2
		i+=1
	if (i*i ==n):
		result +=1
	return result

#preimality tst
def primality(n):
	i =2
	while(i*i <=n):
		if (n%i ==0):
			return False
		i+=1
	return True


#reversing coin
def coins(n):
	result =0
	coin =[0] * (n+1)
	for i in xrange(1, n+1):
		k =i 
		while(k<=n):
			coin[k] = (coin[k] +1) %2
			k+=1
		result +=coin[i]
	return result

