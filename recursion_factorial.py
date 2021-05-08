__author__ = "Ratnesh Mallah"

def factorial(n):
	assert n>=0 and int(n)==n, "Input must be positive integer"
	if n in [0,1]:
		return n
	return n * factorial(n-1)



print(factorial(24))
print(factorial(1))
print(factorial(-1))