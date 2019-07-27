from random import randint

print(4)
for _ in range(4):
	n = randint(1,10)
	print(n)
	arr = []
	for i in range(n):
		arr.append(randint(1,100))
	for num in arr:
		print(num,end=' ')
