def binarysearch(array,k):
	if len(array)==1:
		if array[0]==k:
			return 0
		else:
			return -1
	else:
		low=0
		high=len(array)-1
		while low<=high:
			mid=high - (high-low)/2
			if array[mid]==k:
				return k
			elif array[mid]>k:
				high=mid-1
			else:
				low=mid+1
		return -1

n = int(input())
array = list(map(int,input().strip().split(' ')))
q = int(input())
array.sort()
print("hi")
for a0 in range(q):
	print("hi")
	k= int(input())
	print(binarysearch(array,k)+1)
