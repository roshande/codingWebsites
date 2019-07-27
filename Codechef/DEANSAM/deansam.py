n = int(input())
arr = list(map(int,input().split()))
minsum = arr[0]
for i in range(n):
	for j in range(i,n):
		minsum = min(minsum,sum(arr[i:j]))
print(minsum)
