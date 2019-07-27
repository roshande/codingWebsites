def gcd(n1,n2):
	if n2 == 0 or n1 == 0:
		return n1+n2
	elif n1%2 == 0 and n2%2 == 0:
		return 2* gcd(n1/2,n2/2)
	elif n1>n2:
		return gcd(n2,n1%n2)
t = int(input())
while t > 0:
	n = int(input())
	arr = list(map(int,input().split()))
	
	t -= 1
