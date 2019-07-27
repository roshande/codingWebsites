for t in range(int(input())):
	n = int(input())
	playlist = list(map(int,input().split()))
	k = int(input())
	johny = playlist[k-1]
	smallest = 0
	for i in range(n-1):
		smallest = i
		for j in range(i+1,n):
			if playlist[smallest] > playlist[j]:
				smallest = j
		if smallest != i:
			playlist[smallest],playlist[i] = playlist[i],playlist[smallest]
		if johny == playlist[i]:
			print(i+1)
			break
	else:
		print(n)
