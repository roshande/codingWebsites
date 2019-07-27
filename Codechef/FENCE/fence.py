def brute_minimum_fences(n,m):
    field = [[1]*(m+2) for _ in range(n+2)]
    for _ in range(k):
        r,c = map(int, input().split())
        field[r][c] = 0
    fences = 0
    #print(field)
    for i in range(1,n+1):
        for j in range(1,m+1):
            #around plant at field[i][j]
            if field[i][j] == 0:
                #print()
                fences += field[i-1][j] - field[i][j] # up
                #print(i,j,fences)
                fences += field[i][j-1] - field[i][j] # left
                #print(i,j,fences)
                fences += field[i+1][j] - field[i][j] # down
                #print(i,j,fences)
                fences += field[i][j+1] - field[i][j] # right
                #print(i,j,fences)
    print(fences)

def minimum_fences(field_set,n,m):
    count = 0
    for s in field_set:
        count += 0 if (s[0]+1,s[1]) in field_set else 1
        count += 0 if (s[0]-1,s[1]) in field_set else 1
        count += 0 if (s[0],s[1]-1) in field_set else 1
        count += 0 if (s[0],s[1]+1) in field_set else 1
    return count

for _ in range(int(input())):
    n,m,k = list(map(int, input().split()))
    field= []
    for _ in range(k):
        r,c = map(int, input().split())
        field.append((r,c))
    count = minimum_fences(frozenset(field),n,m)
    print(count)
