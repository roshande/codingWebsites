for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	for i in range(1,n):
		arr[i] += arr[i-1]
	for i in range(n):
		if i+1+arr[i] >= n:
			print(i+1)
			break
