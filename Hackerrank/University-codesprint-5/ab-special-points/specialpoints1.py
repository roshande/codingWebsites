n,m,a,b = list(map(int,input().split()))
if m == n*(n-1)//2:
    print(0)
    exit()
adjlist = [0]*n
reachable = [[0]*n]*n
for _ in range(m):
    u,v = list(map(int,input().split()))
    adjlist[u-1] += 1
    adjlist[v-1] += 1
    reachable[u][v] = 1
    reachable[v][u] = 1
for i in range(n):
	for v in range(n):
        	for k in range(n):
			if reachable[i][v] == 1 and reachable[v][k] == 1:
				reachable[i][k] = 1
cnt = 0
#print(reachable)
#prixxxxxxnt(adjlist)
for v in range(n):
	for i in range(n):
		for j in range(n):
			if reachable[v][i] == 1 and reachable[v][j] == 1 and a*adjlist[i] < adjlist[v] and adjlist[v] < b*adjlist[j]:
				cnt += 1
				break
		else:
			continue
		break
print(cnt)
'''#Connected:
minadj,maxadj = n,0
for i in range(n):
	minadj = min(minadj,len(adjlist[i])
	maxadj = max(maxadj,len(adjlist[i])
cnt = 0
for i in range(n):
	if a*minadj < len(adjlist[i]) and len(adjlist[i]) < b*maxadj:
		cnt += 1
print(cnt)
'''
'''reachable = [[0]*n]*n
adj = [0]*n
for i in range(m):
	u,v = list(map(int,input().split()))
	reachable[u-1][v-1] = 1
	reachable[v-1][u-1] = 1
	adj[u-1] += 1
	adj[v-1] += 1
for i in range(n):
	for j in range(i+1,n):
		for k in range(j+1,n):
			if reachable[i][j] == 1 and reachable[j][k] == 1:
				reachable[i][k] = 1
				reachable[k][i] = 1
cnt = 0
for i in range(n):
	for j in range(n):
		if reachable[i][j] == 1:
			if a*adj[j] < adj[i]:
				for k in range(n):
					if reachable[i][k] == 1 and adj[i] < b*adj[k]:
						cnt += 1
			elif adj[i] < b*adj[j]:
				for k in range(n):
					if reachable[i][k] == 1 and a*adj[k] < adj[i]:
						cnt += 1
for k in range(n):
			if reachable[i][j] == 1 and reachable[i][k] == 1 and a*adj[j] < adj[i] < b*adj[k]:
				cnt += 1
print(cnt)
'''
