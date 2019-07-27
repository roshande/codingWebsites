N, c = map(int,input().split())
print(1,N//2)
s = int(input())
prev = N//2
cost = 0
next_ = 0
while True:
    next_ = (next_ + prev)//2
    if s == 1:
        cost += c
        print(2)
        print
    elif s == 0:
        print(1,)
