for _ in range(int(input())):
    n,x = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(n-1):
        u,v = map(int, input().split())
        A[u-1][v-1] = 1
        A[v-1][u-1] = 1


