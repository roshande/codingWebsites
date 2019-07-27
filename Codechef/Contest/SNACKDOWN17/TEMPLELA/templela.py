for _ in range(int(input())):
	n = int(input())
	h = list(map(int,input().split()))
	#reverseStarted = False
	if n%2 == 0:
		print("no")
		continue
	for i in range(n//2):
		if h[i] != h[-(i+1)] or h[i] != (i+1):
			break
	else:
		print("yes")
		continue
	print("no")
	'''for i in range(1,n):
		if h[i-1] +1 == h[i] or (h[i-1] == h[i] +1 and reverseStarted):
			continue
		elif h[i-1] == h[i]+1 and not reverseStarted:
			reverseStarted = True
		else:
			reverseStarted = False
			break
	if not reverseStarted :
		print("no")
		continue
	print("yes")
	'''
