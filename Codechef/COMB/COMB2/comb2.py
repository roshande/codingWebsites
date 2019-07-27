n, k = map(int,input().split())
ratings = list(map(int,input().split()))
friends = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    friends[x-1][y-1] = 1
    friends[y-1][x-1] = 1
    #print(friends)

wins = [0]*n
for i in range(n):
    for j in range(i+1,n):
        if friends[i][j] == 0:
            wins[i] += int(ratings[i] > ratings[j])
            wins[j] += int(ratings[i] < ratings[j])

print(*wins, sep = ' ')
#print(ratings)
#print(friends)
