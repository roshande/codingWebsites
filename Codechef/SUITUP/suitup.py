test = int(input())
while test > 0:
	S = input()
	maxD = 0
	first = [0]*26
	last = [0]*26
	for i in range(len(S)):
		numAlpha = ord(S[i]) - 97
		if first[numAlpha] == 0:
			first[numAlpha] = i+1
			last[numAlpha] = i+1
		elif last[numAlpha] != 0:
			last[numAlpha] = max(last[numAlpha],i+1)
		maxD = max(maxD, last[numAlpha] - first[numAlpha])

	print(maxD)

	test -=1
