def three3(num,cnt):
	if num < 333:
		return 333
	if cnt > 3:
		return num+1
	if num == 333:
		return 1333
	if cnt < 4:
		ten = 1
		temp_num = num
		while temp_num > 0:
			digit = int(num/ten)%10
			if digit != 3:
				if cnt >= 3:
					num += ten*(digit+1)
					break
				num = num + (3-digit)*(ten)
				cnt +=1
				if digit > 3:
					num += ten*10
					if int(num/(10*ten))%10 == 3:
						cnt +=1
				if cnt >= 3:break
			ten = ten*10
			temp_num = int(temp_num/10)
		return num

test = int(input())
while test > 0:
	num = input()
	cnt = 0
	for ch in num:
		if ch == '3':
			cnt +=1
	print(three3(int(num),cnt))
	test -=1
