from collections import Counter

for _ in range(int(input())):
    n = int(input())
    S = Counter(input())
    R = Counter(input())
    if S == R:
        print("YES")
    else:
        print("NO")
