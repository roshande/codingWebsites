def subsequence(arr,n,m):
	cnt = 0
	for i in range(n):
		for j in range(i+1,n+1):
			if sum(arr[i:j])%m == 0:
				cnt +=1
	return cnt

t = int(input())
while t>0:
	n,m = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	print(subsequence(arr,n,m))
	t-=1
