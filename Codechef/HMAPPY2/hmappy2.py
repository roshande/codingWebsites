def gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(max(a,b)%min(a,b), min(a,b))

def lcm(a,b):
    return a*b/gcd(a,b)

for _ in range(int(input())):
    n,a,b,k = list(map(int,input().split()))
    if n//a + n//b - 2*(n//lcm(a,b)) >= k:
        print("Win")
    else:
        print("Lose")
