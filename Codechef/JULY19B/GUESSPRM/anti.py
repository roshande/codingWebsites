numbers = []
with open("input") as f:
    numbers = list(map(int, f.read().splitlines()))
print(len(numbers))
M = 10
term = False
for P in numbers:
    if term:
        break
    m = M
    while True:
        q, num = map(int, input().split())
        if q not in (1,2) or m < 0:
            print(-1)
            term = True
            break
        if q == 2:
            if P == num:
                print("Yes")
                break
            else:
                print("No")
                term = True
                break
        print(num*num % P)

