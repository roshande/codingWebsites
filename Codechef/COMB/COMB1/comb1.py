for _ in range(int(input())):
    l, r = map(int,input().split())
    print((r-l+1)*(r+l-1))
