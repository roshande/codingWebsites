for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	mindiff = abs(arr[1] - arr[0])
	for i in range(n-1):
		for j in range(i+1,n):
			if mindiff > abs(arr[i] - arr[j]):
				mindiff = abs(arr[i] - arr[j])
	print(mindiff)
