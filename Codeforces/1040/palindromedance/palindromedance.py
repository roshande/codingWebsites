d = [0,0]
n,d[0],d[1] = list(map(int,input().split()))
dress = list(map(int,input().split()))
cost = 0
mid = n//2
if n%2 == 1:
	mid +=1
for i in range(mid):
	if dress[i] in {0,1} and dress[n-i-1] in {0,1}:
		if dress[i] == dress[n-i-1]:
			continue
		else:
			print(-1)
			break
	elif dress[i] in {0,1}:
		#dress[n-i-1] = dress[i]
		cost += d[dress[i]]
	elif dress[n-i-1] in {0,1}:
		#dress[i] = dress[n-i-1]
		cost += d[dress[n-i-1]]
	else:
		if i== mid-1 and n%2 == 1:
			cost += min(*d)
		else:
			cost += 2*min(*d)
else:
	print(cost)
