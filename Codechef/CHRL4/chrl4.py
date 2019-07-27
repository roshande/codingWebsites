def backhome(arr,n,k,cost,index = 0):
	if index == n-1:
		return cost
	
	for i in range(1,k):
		new_cost = backhome(arr,n,k,index+i,cost*arr[index + i])
		if new_cost < cost:
			cost = new_cost
	return cost

def backhome(arr,n,k):
	cost = [[0]*n]*k
	for i in range(n):
		for j in range(k):
			cost[i][j] = arr[i]*cost[i-j][0]
		
def backhome3(cost,n,k):
	maxbig =1e10
	reach = [maxbig]*n
	for r in range(n):
		reach[r] = min([reach[r-i]*cost[r-i] for i in range(1,k) if r-i < n])
	return reach[-1]

t = int(input())
while t > 0:
	n,k = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	print(backhome3(arr,n,k))
	t-=1
