for t in range(int(input())):
	n,m,x,y = list(map(int,input().split()))
	if n==2 and m==2:
		print("Chefirnemo")
	elif n==1:
		if (m-1)%y == 0 :
			print("Chefirnemo")
		else:
			print("Pofik")
	elif m==1:
		if (n-1)%x == 0:
			print("Chefirnemo")
		else:
			print("Pofik")
	elif (n-1)%x == 0  and (m-1)%y == 0 or (n-2)%x == 0 and  (m-2)%y==0:
		print("Chefirnemo")
	else:
		print("Pofik")
