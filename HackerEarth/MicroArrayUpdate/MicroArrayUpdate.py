n = int(input())
for a0 in range(n):
    k = list(map(int,input().strip().split(' ')))
    #print(k)
    array = list(map(int,input().strip().split(' ')))
    #print(array)
    print(k[1]-min(array))
