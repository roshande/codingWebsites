import math

for _ in range(int(input())):
    n, k = map(int,input().split())
    t = math.log(n*(k-1)//2 + 1)/math.log(k)
    print(t)
    t = math.floor(t)
    print(t)
    if n < k**(t+1) + 2*(k**t-1)/(k-1):
        print("Alice")
    else:
        print("Bob")
