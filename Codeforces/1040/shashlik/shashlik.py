import math
n,k = list(map(int,input().split()))
skews = [1]
while skews[-1]<n:
	skews.append(skews[-1]+2*k+1)
if skews[-1] > n:
	print(len(skews[:-1]))
else:
	print(len(skews))
for skew in skews[:-1]:
	if skew < n:
		print(skew,end= ' ')
