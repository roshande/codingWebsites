for _ in range(int(input())):
    s = int(input())
    attacks = list(map(int, input().split()))
    defense = list(map(int, input().split()))
    probables = []
    for i in range(s):
        if attacks[(i-1)%s]+ attacks[(i+1)%s] < defense[i]:
            probables.append(i)
    if len(probables) == 0:
        print(-1)
    else:
        print(max([defense[i] for i in probables]))
