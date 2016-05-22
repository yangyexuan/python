def fib1(n):
	memo = {0:0, 1:1}
	return fastfib(n,memo)

def fastfib(n,memo):
	global numcalls
	numcalls += 1
	#print ('fib called with %s',n)
	if not n in memo:
		memo[n] = fastfib(n-1, memo) + fastfib(n-2, memo)
	return memo[n]

numcalls = 0
n = 20
res = fib1(n)
print ('fib1 called %s,result is %s' %(numcalls,res))

def fib(n):
	global numcalls
	numcalls += 1
	#print ('fib called with %s',n)
	if n <=1:
		return n
	else:
		return fib(n-1) + fib(n-2)

numcalls = 0
n = 20
res = fib(n)
print ('fib called %s , result is %s' %(numcalls, res))