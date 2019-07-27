for _ in range(int(input())):
	arr = []
	for _ in range(5):
		arr.append(map(int,input().split()))
	sum0,sum1 = 0,0
	for num1,num2 in arr:
		sum1 += num2
		sum0 += num1
	#print(sum0,sum1)
	if sum0%5==0:
		if sum1%7 == 0 or sum1%3 == 0:
			print("Yes")
			continue
	elif sum1%5 == 0:
		if sum0%7 == 0 or sum0%3 == 0:
			print("Yes")
			continue
	print("No")
		
