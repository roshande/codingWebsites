for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print(1,1)
	else:
		denom = '1' + ''.join('0'*int(n/2))
		print(1,denom)
