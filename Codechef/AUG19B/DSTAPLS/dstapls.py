def is_different(n,k):
    if n % (k*k) ==0:
    #if k == 1 or k*k == n:
        return False
    else:
        return True

for _ in range(int(input())):
    n,k = map(int, input().split())
    if is_different(n,k):
        print("YES")
    else:
        print("NO")

