for _ in range(int(input())):
	n,m = list(map(int,input().split()))
	completed = list(map(int,input().split()))
	chef,assistant = [],[]
	change = 0
	for i in range(n):
		if not i+1 in completed:
			if change == 0:
				chef.append(i+1)
				change = 1
			else:
				assistant.append(i+1)
				change = 0
	for x in chef:
		print(x,end=' ')
	print()
	for x in assistant:
		print(x,end=' ')
	print()
