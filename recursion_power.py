__author__ = "Ratnesh Mallah"


def power(n,m):
	assert m>=0 and int(m)==m , "The exponent must be positive integer!"
	if n==0 or m==1:
		return n
	if m==0:
		return 1
	else:
		return n * power(n,m-1)


print(power(2,4))
print(power(2,1))
print(power(2,0))
print(power(0,2))
print(power(-5,2))
print(power(5.4,2))
print(power(2,-2))

