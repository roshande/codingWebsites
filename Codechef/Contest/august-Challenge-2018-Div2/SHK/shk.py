import math

def operations(num):
	#num -= pow(2,int(math.log(num,2)))
	#clear msb
	org = num
	num |= num >> 1
	num |= num >> 2
	num |= num >> 4
	num |= num >> 8
	num |= num >> 16
	num |= num >> 32
	num = num >> 1
	org &= num
	
def operations1(num):
	if num&(num-1)==0 or num&(num+1)==0:
		return 1
	root = int(math.log(num,2))
	num = num - 2**root
	if num == 0:
		return 1
	root = int(math.log(num,2))
	return min(num - 2**(root),2**(root+1) - num)

testcases = int(input())
while testcases > 0:
	num = int(input())
	print(operations1(num))
	testcases -= 1
	
