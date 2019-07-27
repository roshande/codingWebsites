for _ in range(int(input())):
	n = int(input())
	ans = 0
	x = (n//5)
	p = 1
	while x > 0:
		ans += x
		p+=1
		x = (n//(5**p))
	print(ans)
