def digitsum(n):
	m,t = 0,0
	while n>9:
		t += 1
		m += n%10
		n = n//10
	return m,t

d = {}
for i in range(1,10):
	for j in range(1,10):
		min_i = i
		t = 0
		for k in range(10):
			if min_i > digitsum(i+k*j)[0]:
				min_i,t = digitsum(i+k*j)
		d[i,j] = min_i,t
print(d)
