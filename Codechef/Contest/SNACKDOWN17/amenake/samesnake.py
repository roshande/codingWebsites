for i in range(int(input())):
	s1 = list(map(int,input().split()))
	s2 = list(map(int,input().split()))
	m = (s1[3]-s1[1])/(s1[2]-s1[0])
	if ((s2[1]-s1[1])/(s2[0]-s1[0]) - m ) * ((s2[3]-s1[1])/(s2[2] - s1[0]) - m ) > 0:
		print("no")
	else:
		print("yes")
