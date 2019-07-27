for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    acc = [0]*n
    cnt = 0
    if A[0]%2 == 1:
        acc[0] = 1
    for i in range(1,n):
        acc[i] = acc[i-1]
        if A[i]%2 == 1:
            acc[i] += 1
    for i in range(n):
        if A[i]%2 == 0:
            cnt += A[-1] - acc[i]
    print(cnt)
