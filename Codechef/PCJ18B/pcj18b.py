def odd_squares(n):
	squares = 0
	for i in range(1,n+1,2):
		squares += (n-i+1)*(n-i+1)
	return squares

test = int(input())
while test > 0:
	n = int(input())
	print(odd_squares(n))
	test -=1
