stack = [0] *N
size =0

def push(x):
	global size
	stack[size] =x
	size +=1

def pop():
	global size
	size -=1
	return stack[size]
