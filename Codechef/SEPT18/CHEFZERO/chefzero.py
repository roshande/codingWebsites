n,m,k = list(map(int,input().split()))
country = [0]*n
for i in range(n):
	country[i] = list(map(int,input().split()))
#print(country)
sumPopu = sum([sum(x) for x in country])
print(sumPopu)

