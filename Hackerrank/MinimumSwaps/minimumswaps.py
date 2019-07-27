def minimumswaps1(arr):
	n,swaps = len(arr),0
	for i in range(n):
		smallest  = i
		for j in range(i+1,n):
			if arr[smallest] > arr[j]:
				smallest = j
		if smallest != i:
			arr[i],arr[smallest] = arr[smallest],arr[i]
			swaps+=1
	return swaps

def minimumswaps(arr):
	n,swaps = len(arr),0
	dct = {}
	for i in range(n):
		if i+1 != arr[i]:
			dct[arr[i]] = i

	for i in range(n):
		if i+1 != arr[i]:
			arr[i],arr[dct[i+1]] = arr[dct[i+1]],arr[i]
			swaps += 1
	return swaps

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	print(minimumswaps1(arr))
