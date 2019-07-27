for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    s = 0
    for i in range(int(n/2)):
        s += (arr[-i-1] - arr[i])
    print(s)
