for _ in range(int(input())):
    for _ in range(int(input())):
        i,n,q = list(map(int, input().split()))
        orig_up = n//2
        if i == q:
            print(orig_up)
        else:
            print(n - orig_up)

