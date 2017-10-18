# Fibonacci Sequence using recursion
def fibo1(n):
	if n == 1 or n == 2:
		return 1
	return fibo1(n-1) + fibo1(n-2)


# Using normal loop
def fibo2(n):
        a, b = 1, 1
	for i in range(n-1):
		a, b = b, a+b
	return a 

# change in the print fibo1/fibo2 for the desired function to call
# for i in range (1,11):
#	print (fibo1(i))


# Fibonacci sequence using Generator
def fibo3():
	a, b = 1, 1
	while True:
		yield a
		a, b = b, a+b
n = 0
for i in fibo3():
	if n>=10:
		break;
	print (i)
	n += 1
	



