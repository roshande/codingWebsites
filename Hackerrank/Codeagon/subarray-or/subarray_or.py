def arrayor(arr):
	arror = 0
	for num in arr:
		arror = arror|num
	return arror

n = int(input())
arr = list(map(int,input().split()))
sumor = sum(arr)
for i in range(n):
	for j in range(i+1,n):
		sumor += arrayor(arr[i:j+1])
print(sumor)
