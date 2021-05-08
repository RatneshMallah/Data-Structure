__author__ = "Ratnesh Mallah"


def sumOfDigits(n):
	assert n>=0 and int(n)==n ,"The number must be positive integer" 
	if n==0:
		return n
	else:
		return n%10 + sumOfDigits(int(n/10))



print(sumOfDigits(12345))
print(sumOfDigits(4))
print(sumOfDigits(-12))