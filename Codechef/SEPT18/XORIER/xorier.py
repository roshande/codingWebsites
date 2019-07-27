def equal_array(arr1,arr2):
	cnt = 0
	for num1 in arr1:
		for num2 in arr2:
			if num1>>2 != num2>>2:
				cnt +=1
	return cnt

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int,input().split()))
	total = 0
	n = [[] for i in range(4)]
	for num in arr:
		n[num%4].append(num)
	print(n)
	total = len(n[0])*(len(n[0])-1)//2
	total += len(n[1])*(len(n[1])-1)//2
	total += len(n[2])*(len(n[2])-1)//2
	total += len(n[3])*(len(n[3])-1)//2
	total += equal_array(n[0],n[2])
	total += equal_array(n[1],n[3])
	'''#Brute Force
	d = []
	for i in range(n):
		for j in range(i+1,n):
			num = arr[i]^arr[j]
			if num> 2 and num%2 == 0:
				d.append([arr[i],arr[j]])
				total +=1
	print(d)
	'''
	print(total)
