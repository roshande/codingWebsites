def count3(num):
	num = str(num)
	cnt = 0
	for ch in num:
		if ch == '3':
			cnt +=1
		if cnt == 3:
			return True
	return False

def count3_(num):
	cnt = 0
	while num > 0:
		if num%10 == 3:
			cnt +=1
		if cnt == 3:
			return True
		num = int(num/10)
	return False

test = int(input())
while test > 0:
	num = int(input())
	num += 1
	while not count3_(num):
		num +=1
	print(num)
	test -=1
