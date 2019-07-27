n,q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cum_strength = [0]
for i in range(n):
    cum_strength.append(cum_strength[-1] + A[i]*B[i])
for _ in range(q):
    l,r = map(int,input().split())
    print(cum_strength[r] - cum_strength[l-1])
