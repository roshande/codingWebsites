recipes = []
n = int(input())
for _ in range(n):
	recipes.append(tuple(map(int,input().split())))
#print(recipes)
for _ in range(int(input())):
	k,*aliens = tuple(map(int,input().split()))
	down_recipes = [0]*n
	#print(aliens)
	for alien in aliens:
		for i in range(n):
			if recipes[i][0] <= alien and recipes[i][1] >= alien:
				down_recipes[i] = 1
	print(sum(down_recipes))
