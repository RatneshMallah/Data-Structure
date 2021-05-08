__author__ = "Ratnesh Mallah"

def gcd(m,n):
	assert int(m)==m and int(n)==n, "The numbers must be integers"
	if m<n:
		n,m = m,n
	if m<0:
		m = m*-1
	if n<0:
		n = n*-1 
	if m%n ==0:
		return n
	return gcd(n, m%n)





print(gcd(42,18))



"""
EX:
42,18

48/18 = ans 2 expo 12
18/12 = ans 1 exp 6
"""